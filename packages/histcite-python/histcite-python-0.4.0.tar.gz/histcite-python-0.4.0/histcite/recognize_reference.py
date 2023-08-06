from typing import Any
import pandas as pd


class RecognizeCommonReference:
    def __init__(self, docs_df: pd.DataFrame, 
                 reference_df: pd.DataFrame, 
                 compare_cols: list[str]):
        self.docs_df = docs_df
        self.reference_df = reference_df
        self.compare_cols = compare_cols

    def filter_df(self, row_index: int) -> tuple[pd.DataFrame, pd.DataFrame]:
        row_year = self.docs_df.loc[row_index, 'PY']
        child_reference_df = self.reference_df[self.reference_df['doc_index'] == row_index].dropna(subset=self.compare_cols)
        child_docs_df = self.docs_df[(self.docs_df['PY'] <= row_year) 
                                     & (self.docs_df['doc_index'] != row_index)].dropna(subset=self.compare_cols)
        return child_docs_df, child_reference_df

    def recognize_ref(self, child_docs_df: pd.DataFrame, 
                      child_reference_df: pd.DataFrame) -> tuple[list[Any], list[Any]]:
        cited_list: list[Any] = []
        local_ref_list:list[Any] = []
        shared_df = child_docs_df[['doc_index']+self.compare_cols].merge(child_reference_df[['ref_index']+self.compare_cols])
        if shared_df.shape[0] > 0:
            cited_list = sorted(set(shared_df['doc_index']))
            local_ref_list = sorted(set(shared_df['ref_index']))
        return cited_list, local_ref_list

class RecognizeReference():
    @staticmethod
    def recognize_wos_reference(docs_df: pd.DataFrame,
                                reference_df: pd.DataFrame,
                                row_index: int) -> list[int]:
        cited_list:list[int] = []
        child_reference_df = reference_df[reference_df['doc_index'] == row_index]

        # DOI exists
        child_reference_df_doi = child_reference_df[child_reference_df['DI'].notna()]['DI']
        child_docs_df_doi = docs_df[(docs_df['DI'].notna()) & (docs_df['doc_index'] != row_index)]['DI']
        cited_list.extend(child_docs_df_doi[child_docs_df_doi.isin(child_reference_df_doi)].index.tolist())
        reference_df.loc[child_reference_df_doi[child_reference_df_doi.isin(child_docs_df_doi)].index, 'local'] = 1

        # DOI not exists
        compare_cols = ['First_AU', 'PY', 'J9', 'BP']
        child_reference_df_left = child_reference_df[child_reference_df['DI'].isna()].dropna(subset=compare_cols)
        child_reference_py = child_reference_df_left['PY']
        child_reference_bp = child_reference_df_left['BP']
        recognize_instance = RecognizeCommonReference(docs_df, reference_df, compare_cols)
        child_docs_df_left = docs_df[(docs_df['PY'].isin(child_reference_py)) 
                                     & (docs_df['BP'].isin(child_reference_bp))
                                     & (docs_df['DI'].isna())
                                     & (docs_df['doc_index'] != row_index)].dropna(subset=compare_cols)
        result = recognize_instance.recognize_ref(child_docs_df_left, child_reference_df_left)
        cited_list.extend(result[0])
        reference_df.loc[result[1], 'local'] = 1
        return cited_list

    @staticmethod
    def recognize_cssci_reference(docs_df: pd.DataFrame,
                                  reference_df: pd.DataFrame,
                                  row_index: int) -> list[int]:
        compare_cols = ['First_AU', 'TI']
        recognize_instance = RecognizeCommonReference(docs_df, reference_df, compare_cols)
        child_docs_df, child_reference_df = recognize_instance.filter_df(row_index)
        cited_list, local_ref_list = recognize_instance.recognize_ref(child_docs_df, child_reference_df)
        reference_df.loc[local_ref_list, 'local'] = 1
        return cited_list

    @staticmethod
    def recognize_scopus_reference(docs_df: pd.DataFrame,
                                   reference_df: pd.DataFrame,
                                   row_index: int) -> list[int]:
        compare_cols = ['First_AU', 'TI']
        recognize_instance = RecognizeCommonReference(docs_df, reference_df, compare_cols)
        child_docs_df, child_reference_df = recognize_instance.filter_df(row_index)
        cited_list, local_ref_list = recognize_instance.recognize_ref(child_docs_df, child_reference_df)
        reference_df.loc[local_ref_list, 'local'] = 1
        return cited_list