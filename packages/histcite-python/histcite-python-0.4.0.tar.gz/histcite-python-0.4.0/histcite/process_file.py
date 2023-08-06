import os
import re
import pandas as pd
from typing import Literal, Callable
from histcite.parse_reference import ParseReference
from histcite.recognize_reference import RecognizeReference


class ProcessWosFile:
    @staticmethod
    def extract_first_author(au_field: pd.Series) -> pd.Series:
        return au_field.str.split(pat=';',n=1,expand=True)[0].str.replace(',',' ')


class ProcessCssciFile:
    @staticmethod
    def process_org(cell: str) -> str:
        org_set = set(re.findall(r'](.*?)(?:/|$)', cell))
        org_list = [i.replace('.', '') for i in org_set]
        return '; '.join(org_list)


class ProcessScopusFile:
    pass


class ProcessGeneralFile:
    @staticmethod
    def read_all_file(read_file_func: Callable[[str], pd.DataFrame], file_name_list: list[str]) -> pd.DataFrame:
        if len(file_name_list) > 1:
            return pd.concat([read_file_func(file_name) for file_name in file_name_list], ignore_index=True, copy=False)
        elif len(file_name_list) == 1:
            return read_file_func(file_name_list[0])
        else:
            raise FileNotFoundError('No valid file in the folder')
    
    @staticmethod
    def generate_ref_df(cr_series: pd.Series, source_type: Literal['wos', 'cssci', 'scopus']) -> pd.DataFrame:
        parsed_cr_cells = [ParseReference(doc_index, cell, source_type).parse_cr_cell() for doc_index, cell in cr_series.items()]
        reference_df = pd.concat([pd.DataFrame.from_dict(cell) for cell in parsed_cr_cells if cell], ignore_index=True)
        return reference_df

class ReadFile:
    @staticmethod
    def _read_csv(file_path: str, use_cols: list, sep: str = ',') -> pd.DataFrame:
        try:
            df = pd.read_csv(
                file_path,
                sep=sep,
                header=0,
                on_bad_lines='skip',
                usecols=use_cols,
                dtype_backend="pyarrow")
            return df
        except ValueError:
            file_name = os.path.basename(file_path)
            raise ValueError(f'File {file_name} is not a valid csv file')


class ProcessFile:
    def __init__(self, folder_path: str, source_type: Literal['wos', 'cssci', 'scopus']):
        self.folder_path = folder_path
        self.source_type = source_type
        if source_type == 'wos':
            self.file_name_list = [i.split('.')[0] for i in os.listdir(folder_path) if i[:9] == 'savedrecs']
        elif source_type == 'cssci':
            self.file_name_list = [i for i in os.listdir(folder_path) if i[:3] == 'LY_']
        elif source_type == 'scopus':
            self.file_name_list = [i.split('.')[0] for i in os.listdir(folder_path) if i[:6] == 'scopus']
        else:
            raise ValueError('Invalid source type')

        self.file_name_list.sort()
        if source_type == 'wos':
            self.file_name_list = [i+'.txt' for i in self.file_name_list]
        elif source_type == 'scopus':
            self.file_name_list = [i+'.csv' for i in self.file_name_list]

    def _read_wos_file(self, file_name: str) -> pd.DataFrame:
        use_cols = ['AU', 'TI', 'SO', 'DT', 'CR', 'DE', 'C3',
                    'NR', 'TC', 'Z9', 'J9', 'PY', 'VL', 'BP', 'DI', 'UT']
        file_path = os.path.join(self.folder_path, file_name)
        df = ReadFile._read_csv(file_path, use_cols, '\t')
        df.insert(1, 'First_AU', ProcessWosFile.extract_first_author(df['AU']))
        df['source file'] = file_name
        return df

    def _read_cssci_file(self, file_name: str) -> pd.DataFrame:
        file_path = os.path.join(self.folder_path, file_name)
        with open(file_path, 'r') as f:
            text = f.read()

        if text[:16] != '南京大学中国社会科学研究评价中心':
            raise ValueError(f'File {file_name} is not a valid cssci file')
        body_text = text.split('\n\n\n', 1)[1]
        contents = {}
        original_fields = ['来源篇名', '来源作者', '基    金', '期    刊', '机构名称', '第一作者', '年代卷期', '关 键 词', '参考文献']
        for field in original_fields:
            if field != '参考文献':
                field_pattern = f'【{field}】(.*?)\n'
                contents[field] = re.findall(field_pattern, body_text)
            else:
                field_pattern = '【参考文献】\n(.*?)\n?'+'-'*5
                contents[field] = re.findall(field_pattern, body_text, flags=re.S)

        df = pd.DataFrame.from_dict(contents)

        # 重命名列标签
        column_mapping = {
            '来源篇名': 'TI',
            '来源作者': 'AU',
            '基    金': 'FU',
            '期    刊': 'SO',
            '机构名称': 'C3',
            '第一作者': 'First_AU',
            '年代卷期': 'PY&VL&BP&EP', 
            '关 键 词': 'DE',
            '参考文献': 'CR'}
        df.rename(columns=column_mapping, inplace=True)

        df['AU'] = df['AU'].str.replace('/', '; ')
        df['DE'] = df['DE'].str.replace('/', '; ')
        df['PY'] = df['PY&VL&BP&EP'].str.extract(r'^(\d{4}),', expand=False)
        df['C3'] = df['C3'].apply(ProcessCssciFile.process_org)
        df['CR'] = df['CR'].str.replace('\n', '; ')
        df['NR'] = df['CR'].str.count('; ')
        df.insert(2, 'First_AU', df.pop('First_AU'))
        df['source file'] = file_name
        return df

    def _read_scopus_file(self, file_name: str) -> pd.DataFrame:
        use_cols = ['Authors', 'Author full names', 'Title', 'Year', 'Source title', 'Volume', 'Issue',
                    'Page start', 'Page end', 'Cited by', 'DOI', 'Author Keywords', 'References', 'Document Type', 'EID']
        file_path = os.path.join(self.folder_path, file_name)
        df = ReadFile._read_csv(file_path, use_cols)
        
        # 重命名列标签
        column_mapping = {
            'Authors': 'AU',
            'Author full names': 'AF',
            'Title': 'TI',
            'Year': 'PY',
            'Source title': 'SO',
            'Volume': 'VL',
            'Issue': 'IS',
            'Page start': 'BP',
            'Page end': 'EP',
            'Cited by': 'TC',
            'DOI': 'DI',
            'Author Keywords': 'DE',
            'References': 'CR',
            'Document Type': 'DT',
            }
        df.rename(columns=column_mapping, inplace=True)
        
        df['NR'] = df['CR'].str.count('; ')
        df.insert(1, 'First_AU', df['AU'].str.split(pat=';', n=1, expand=True)[0])
        df['source file'] = file_name
        return df

    def concat_df(self):
        """concat multi dataframe and drop duplicate rows"""
        if self.source_type == 'wos':
            docs_df = ProcessGeneralFile.read_all_file(self._read_wos_file, self.file_name_list)
            docs_df['DI'] = docs_df['DI'].str.lower()
        elif self.source_type == 'cssci':
            docs_df = ProcessGeneralFile.read_all_file(self._read_cssci_file, self.file_name_list)
            docs_df['TI'] = docs_df['TI'].str.lower()
        elif self.source_type == 'scopus':
            docs_df = ProcessGeneralFile.read_all_file(self._read_scopus_file, self.file_name_list)
            docs_df['TI'] = docs_df['TI'].str.lower()
        else:
            raise ValueError('Invalid source type')

        # drop duplicate rows
        original_num = docs_df.shape[0]
        if self.source_type == 'wos':
            check_cols = ['UT']
        elif self.source_type == 'cssci':
            check_cols = ['TI', 'First_AU']
        elif self.source_type == 'scopus':
            check_cols = ['EID']
        else:
            raise ValueError('Invalid source type')
        docs_df.drop_duplicates(subset=check_cols, ignore_index=True, inplace=True) 
        current_num = docs_df.shape[0]
        print(f'共读取 {original_num} 条数据，去重后剩余 {current_num} 条')
        docs_df.insert(0, 'doc_index', docs_df.index)
        self.docs_df = docs_df

    def process_reference(self):
        """extract total references and generate dataframe"""
        cr_series = self.docs_df['CR']
        if self.source_type == 'wos':
            reference_df = ProcessGeneralFile.generate_ref_df(cr_series, 'wos')
            reference_df = reference_df.astype({'PY':'int64[pyarrow]'})
        elif self.source_type == 'cssci':
            reference_df = ProcessGeneralFile.generate_ref_df(cr_series, 'cssci')
            reference_df['TI'] = reference_df['TI'].str.lower()
        elif self.source_type == 'scopus':
            reference_df = ProcessGeneralFile.generate_ref_df(cr_series, 'scopus')
            reference_df['TI'] = reference_df['TI'].str.lower()
        else:
            raise ValueError('Invalid source type')
        # appear duplicate reference in some docs' references
        reference_df.drop_duplicates(ignore_index=True, inplace=True)
        reference_df.insert(0, 'ref_index', reference_df.index)
        reference_df['local'] = 0
        self.reference_df = reference_df

    @staticmethod
    def __reference2citation(reference_field: pd.Series) -> pd.Series:
        citation_field = pd.Series([[] for i in range(len(reference_field))])
        for doc_index, ref_list in reference_field.items():
            if ref_list:
                for ref_index in ref_list:
                    citation_field[ref_index].append(doc_index)
        return citation_field

    def process_citation(self):
        """recognize citation relationship"""
        if self.source_type == 'wos':
            reference_field = self.docs_df.apply(lambda row: RecognizeReference.recognize_wos_reference(
                self.docs_df, self.reference_df, row.name), axis=1)
        elif self.source_type == 'cssci':
            reference_field = self.docs_df.apply(lambda row: RecognizeReference.recognize_cssci_reference(
                self.docs_df, self.reference_df, row.name), axis=1)
        elif self.source_type == 'scopus':
            reference_field = self.docs_df.apply(lambda row: RecognizeReference.recognize_scopus_reference(
                self.docs_df, self.reference_df, row.name), axis=1)
        else:
            raise ValueError('Invalid source type')

        citation_field = self.__reference2citation(reference_field)
        lcr_field = reference_field.apply(len)
        lcs_field = citation_field.apply(len)
        self.docs_df['reference'] = [
            ';'.join([str(j) for j in i]) if i else None for i in reference_field]
        self.docs_df['citation'] = [
            ';'.join([str(j) for j in i]) if i else None for i in citation_field]
        self.docs_df['LCR'] = lcr_field
        self.docs_df['LCS'] = lcs_field