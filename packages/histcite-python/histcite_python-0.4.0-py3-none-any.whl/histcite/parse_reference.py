import re
from dataclasses import dataclass
from typing import Optional, Literal, Union, Any

@dataclass
class WosField:
    First_AU: Optional[str]
    PY: Optional[int] = None
    J9: Optional[str] = None
    VL: Optional[str] = None
    BP: Optional[str] = None
    DI: Optional[str] = None


@dataclass
class CssciField:
    First_AU: Optional[str]
    TI: str
    SO: Optional[str] = None
    PY: Optional[str] = None
    VL: Optional[str] = None


@dataclass
class ScopusField:
    First_AU: Optional[str]
    TI: str
    SO: Optional[str] = None
    VL: Optional[str] = None
    IS: Optional[str] = None
    BP: Optional[str] = None
    EP: Optional[str] = None
    PY: Optional[str] = None


class ParseReference:
    def __init__(self, doc_index, cr_cell: str, source_type: Literal['wos', 'cssci', 'scopus']):
        sep = '; '
        try:
            self.cr_list = cr_cell.split(sep)
            self.cr_count = len(self.cr_list)
        except AttributeError:
            self.cr_count = 0
        else:
            self.doc_index = doc_index
            self.source_type = source_type

    @staticmethod
    def _parse_wos_cr(cr: str) -> Optional[WosField]:
        if 'Patent No.' in cr:
            return None
        
        AU, raw_PY, J9, VL, BP, DI = None, None, None, None, None, None
        if ', DOI ' in cr:
            # contain only one DOI
            if 'DOI [' not in cr:
                DI_match = re.search(r'DOI (10.*)$', cr)
                DI = DI_match[1] if DI_match else None
            # contain two or more DOI
            else:
                DI_match = re.search(r'DOI \[(.*)\]', cr)
                DI = DI_match[1] if DI_match else None
            cr = re.sub(r', DOI.*', '', cr)
        
        # always contain another language
        if '[' in cr:
            return None
        
        BP_match = re.search(r', P([A-Za-z]?\d+)$', cr)
        if BP_match:
            BP = BP_match[1]
            cr = cr.replace(f', P{BP}', '')

        cr = re.sub(r'[,\.] PROCEEDINGS(?=, )','',cr,flags=re.I)
        if VL_match := re.search(r', V([\d-]+)$', cr):
            VL = VL_match[1]
            sub_pattern = r', V[\d-]+$'
        
        elif re.search(r', VOLS? ', cr, re.I):
            VL_match = re.search(r', VOLS? ([\w\- ]+)$', cr, re.I)
            VL = VL_match[1] if VL_match else None
            sub_pattern = r', V[Oo][Ll][Ss]?.*'
        
        elif VL_match := re.search(r'(?<=[A-Z\.]), V([\w\. ]+)$', cr):
            VL = VL_match[1]
            sub_pattern = r'(?<=[A-Z\.]), V[\w\. ]+$'

        else:
            sub_pattern = None
        
        if sub_pattern:
            cr = re.sub(sub_pattern, '', cr)

        dot_count = cr.count(', ') 
        if dot_count == 2:
            AU, raw_PY, J9 = cr.split(', ')
        elif dot_count > 2:
            PY_pattern = r', (\d{4}), '
            if re.search(PY_pattern, cr):
                AU, raw_PY, J9 = re.split(PY_pattern, cr, 1)
        else:
            return None
        
        if DI:
            DI = DI.lower()
            if len(re.findall(', ', DI)) == 1:
                try:
                    DI1, DI2 = DI.replace('doi ', '').split(', ')
                except:
                    print(DI)
                    return None
                if DI1 == DI2:
                    DI = DI1
                else:
                    DI = None
        
        if raw_PY and re.match(r'^\d{4}$', raw_PY):
            PY = int(raw_PY)
        else:
            PY = None
        return WosField(AU, PY, J9, VL, BP, DI)

    @staticmethod
    def _parse_cssci_cr(cr: str) -> Optional[CssciField]:
        """only parse chinese reference"""
        dot_pattern = re.compile(r'(?<!\d)\.(?!\d)|(?<=\d)\.(?!\d)|(?<!\d)\.(?=\d)|(?<=\d{4})\.(?=\d)|(?<=\d)\.(?=\d{4})')
        
        # 中文参考文献
        if re.search(r'[\u4e00-\u9fa5]', cr):
            dot_count = len(dot_pattern.findall(cr))

            # 中间部分双圆点
            if re.search(r'[^\d]\.{2,}', cr):
                return None

            # 学位论文
            elif ":学位论文." in cr:
                try:
                    _, AU, TI, other = cr.split('.')
                except:
                    return None
                else:
                    TI = TI.replace(':学位论文', '')
                    SO, PY = other.split(',')
                    PY = PY.split(':')[0]
                    return CssciField(AU, TI, SO, PY, None)

            # 国家标准
            elif 'GB/T' in cr:
                if cr[-3:] == "出版社":
                    _, AU, other = cr.split('.', 2)
                    TI, SO = other.rsplit('.', 1)
                    return CssciField(AU, TI, SO, None, None)
                else:
                    _, AU, TI = cr.split('.', 2)
                    return CssciField(AU, TI, None, None, None)

            # 规范
            elif re.search(r':DB\d{2}/T', cr):
                _, AU, other = cr.split('.', 2)
                TI, PY = other.rsplit('.', 1)
                return CssciField(AU, TI, None, PY, None)

            # 报刊
            elif re.search(r'\.\d{1,2}\.\d{1,2}(?:\(|$)', cr):
                try:
                    _, AU, TI, SO, other = re.split(dot_pattern, cr, 4)
                except:
                    return None
                else:
                    return CssciField(AU, TI, SO, None, None)

            # 专利1
            elif re.search(r'\.CN\d{9}[A-Z]$', cr):
                TI = cr.split('.', 1)[1]
                return CssciField(None, TI, None, None, None)
            # 专利2
            elif re.search(r'^\d+\.一种', cr):
                date_pattern = re.compile(r'\d{4}\-\d{1,2}\-\d{1,2}')
                TI = cr.split('.', 1)[1]
                date = date_pattern.search(cr)
                if date:
                    PY = date[0].split('-')[0]
                else:
                    PY = None
                TI = date_pattern.sub('', TI).strip('.()')
                return CssciField(None, TI, None, PY, None)

            # 网络文献
            elif re.search(r'\.\d{4}$', cr):
                if dot_count == 3:
                    _, AU, TI, PY = re.split(dot_pattern, cr)
                elif dot_count == 4:
                    _, AU, TI, SO, PY = re.split(dot_pattern, cr)
                else:
                    return None
                return CssciField(AU, TI, None, PY, None)

            # 期刊1
            elif dot_count == 5:
                _, AU, TI, SO, PY, VL = re.split(dot_pattern, cr)
                return CssciField(AU, TI, SO, PY, VL)
            # 期刊2
            elif dot_count == 4:
                _, AU, TI, SO, _ = re.split(dot_pattern, cr)
                return CssciField(AU, TI, SO, None, None)

            # 专著
            elif dot_count == 3:
                _, AU, TI, SO = re.split(dot_pattern, cr)
                return CssciField(AU, TI, SO, None, None)

            # 其他
            elif dot_count == 2:
                _, AU, TI = re.split(dot_pattern, cr)
                return CssciField(AU, TI, None, None, None)

            elif dot_count == 1:
                _, TI = re.split(dot_pattern, cr)
                return CssciField(None, TI, None, None, None)
            else:
                return None
        else:
            return None

    @staticmethod
    def _parse_scopus_cr(cr: str) -> Optional[ScopusField]:
        if cr.count(', ') < 3:
            return None

        # 年份
        PY_match = re.search(r' \((\d{4})\)$', cr)
        if PY_match:
            PY = PY_match[1]
            cr = cr.rsplit(', ', 1)[0]
        else:
            PY = None

        # 页码
        if re.search(r', [Pp]{2}', cr):
            if PP_match := re.search(r', [Pp]{2}[\.,]? ([\w\-\–\.]+)', cr):
                PP = PP_match[1].strip('., ')
                try:
                    BP, EP = re.split(r'[-–]', PP, 1)
                except:
                    BP, EP = None, None
            else:
                BP, EP = None, None
            cr = re.sub(r', [Pp]{2}.*', '', cr)

        elif PP_match := re.search(r',? (\d+[–-]\d+)$', cr):
            PP = PP_match[1]
            BP, EP = re.split(r'[-–]', PP)
            cr = re.sub(r',? \d+[–-]\d+$', '', cr)
        
        else:
            BP, EP = None, None

        # 卷期
        if ', xxxx' in cr:
            VL, IS = None, None
            cr = cr.replace(', xxxx', '')

        elif re.search(r', [Vv]ol\. ', cr):
            VL_match = re.search(r', [Vv]ols?\. ([^,]+)(?=,|$)', cr)
            if VL_match:
                VL = VL_match[1]
                IS_match = re.search(r', [Nn]o\. ([\w\-–]+)(?=,|$)', cr)
                if IS_match:
                    IS = IS_match[1]
                else:
                    IS = None
            else:
                VL, IS = None, None
            cr = re.sub(r', [Vv]ol.*', '', cr)

        elif VL_IS_match := re.search(r', ([\d\.\s,\-–]+)[\w\.]*$', cr):
            VL_IS = VL_IS_match[1]
            try:
                VL, IS = VL_IS.split(', ', 1)
            except:
                VL, IS = VL_IS, None
            cr = re.sub(r', [\d,\- ]+[A-Z]?', '', cr)
        
        else:
            VL, IS = None, None

        # 作者
        full_name_pattern = r'^[A-Z][a-zA-Z\'-]* [A-Z][a-zA-Z\'-]*(?:,|\.|-|\s)+[A-Z-]*,?\s'
        if 'Et al.' in cr:
            First_AU = cr.split(', ')[0]
            cr = re.sub(r'^.*Et al\., ', '', cr)

        elif '., ' in cr:
            AU = cr.rsplit('., ', 1)[0]
            if ',' in AU:
                First_AU = AU.split(', ')[0]
            else:
                First_AU = AU + '.'
            cr = cr.replace(f'{AU}., ', '')

        elif re.search(full_name_pattern, cr):
            First_AU = cr.split(', ')[0]
            while re.search(full_name_pattern, cr):
                cr = re.sub(full_name_pattern, '', cr, 1)

        elif re.search('^[A-Z][a-zA-Z-]+, ', cr):
            First_AU = cr.split(', ',1)[0]
            cr = cr.replace(f'{First_AU}, ', '')

        else:
            First_AU = None

        # 标题和来源
        comma_count = cr.count(', ')
        if comma_count == 0:
            TI, SO = cr, None
        elif comma_count == 1:
            TI, SO = cr.split(', ')
        else:
            # 中文文献引用规范
            chinese_jounal_ref_pattern = r'\s?\[[A-Z]\](?:, |$)'
            if re.search(chinese_jounal_ref_pattern,cr):
                TI, SO = re.split(chinese_jounal_ref_pattern,cr,1)
            
            # 会议文献
            elif re.search(r'[Cc]onference|Conf\.|[Pp]roceeding|Proc\.|[Cc]ommittee|[Ss]ymposium|[Cc]onvention|[Cc]ongress', cr):
                TI, SO = cr.split(', ', 1)

            # 匹配来源
            elif SO_match := re.search(r'[\w\)”], ([A-Z\d][\w \.\-&:]+)$',cr):
                SO = SO_match[1]
                TI = cr.replace(f', {SO}', '')
            
            # 匹配标题
            elif TI_match:= re.search(r'^(([^\.\s]+ ){3,}[^\.\sA-Z]+), [A-Z]',cr):
                TI = TI_match[1]
                SO = cr.replace(f'{TI}, ', '')

            # 首字母大写，其他小写
            elif re.search(r'^[A-Z][^A-Z]+$',cr):
                TI, SO = cr, None
            
            else:
                return None
        return ScopusField(First_AU,TI,SO,VL,IS,BP,EP,PY)

    def parse_cr_cell(self) -> Optional[dict[str, list[Any]]]:
        if self.cr_count == 0:
            return None
        
        parsed_cr_list : list[Union[WosField, CssciField, ScopusField, None]]
        if self.source_type == "wos":
            parsed_cr_list = [self._parse_wos_cr(i) for i in self.cr_list]
            keys = ['First_AU', 'PY', 'J9', 'VL', 'BP', 'DI']
        elif self.source_type == "cssci":
            parsed_cr_list = [self._parse_cssci_cr(i) for i in self.cr_list]
            keys = ['First_AU', 'TI', 'SO', 'PY', 'VL']
        elif self.source_type == "scopus":
            parsed_cr_list = [self._parse_scopus_cr(i) for i in self.cr_list]
            keys = ['First_AU', 'TI', 'SO', 'VL', 'BP', 'EP', 'PY']
        else:
            raise ValueError('Invalid source type')

        result:dict[str, list[Any]]  = {key: [] for key in keys}
        for parsed_cr in parsed_cr_list:
            if parsed_cr:
                for key in keys:
                    result[key].append(getattr(parsed_cr, key))
        result['doc_index'] = self.doc_index
        return result