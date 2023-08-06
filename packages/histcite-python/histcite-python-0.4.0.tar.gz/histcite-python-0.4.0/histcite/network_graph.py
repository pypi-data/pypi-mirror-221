from typing import Literal
import pandas as pd

class GraphViz:
    def __init__(self, docs_df: pd.DataFrame, source_type: str):
        self.docs_df = docs_df
        self.source_type = source_type
        self.empty_year_index = docs_df[docs_df['PY'].isna()].index

    def __obtain_groups(self):
        """obtain groups of docs by year"""
        year_series = self.docs_df.loc[self.node_list, 'PY']
        groups = year_series.groupby(year_series)
        year_list = [i[0] for i in groups]
        grouped_doc_index = [i[1].index.tolist() for i in groups]
        self.year_list = year_list
        for idx, year in enumerate(year_list):
            grouped_doc_index[idx].insert(0, year)
        self.grouped_doc_index = grouped_doc_index

    def __generate_edge(self, doc_index: int, 
                        doc_relation: str, 
                        relation_type: Literal['reference', 'citation']) -> set[tuple[int, int]]:
        related_doc_list = [int(i) for i in doc_relation.split(';') if int(i) not in self.empty_year_index]
        if relation_type == 'reference':
            return {(doc_index, ref) for ref in related_doc_list}
        else:
            return {(citation, doc_index) for citation in related_doc_list}

    def __generate_edge_list(self):
        min_df = self.docs_df.loc[self.doc_indices, ['reference', 'citation']]
        edge_set: set[tuple[int, int]] = set()
        for idx in self.doc_indices:
            doc_reference = min_df.loc[idx, 'reference']
            doc_citation = min_df.loc[idx, 'citation']
            if pd.notna(doc_citation) and isinstance(doc_citation, str):
                cell_edge_set = self.__generate_edge(idx, doc_citation, 'citation')
                if cell_edge_set:
                    edge_set.update(cell_edge_set)
            if pd.notna(doc_reference) and isinstance(doc_reference, str):
                cell_edge_set  = self.__generate_edge(idx, doc_reference, 'reference')
                if cell_edge_set:
                    edge_set.update(cell_edge_set)

        # 过滤索引列表之外的文献
        if not self.allow_external_node:
            edge_set = {(edge[0], edge[1]) for edge in edge_set if edge[0] in self.doc_indices and edge[1] in self.doc_indices}

        # 根据边生成节点
        source_node = set([i for i, _ in edge_set])
        target_node = set([j for _, j in edge_set])
        node_list = sorted(source_node | target_node)
        self.node_list: list[int] = node_list

        edge_list: dict[int, list[int]] = {i: [] for i in sorted(source_node)}
        for edge in edge_set:
            edge_list[edge[0]].append(edge[1])
        return edge_list

    def generate_dot_file(self, doc_indices:pd.Index, allow_external_node=False):
        """
        doc_indices: 文献索引列表\n
        allow_external_node: 是否允许出现doc_indices之外的节点，默认False
        """
        self.doc_indices = [i for i in doc_indices if i not in self.empty_year_index]
        self.allow_external_node = allow_external_node

        raw_edge_list = self.__generate_edge_list()
        self.__obtain_groups()

        dot_edge_list = [f'\t{source} -> '+'{ '+' '.join([str(i) for i in raw_edge_list[source]])+' };\n' for source in raw_edge_list]
        dot_groups = [f'\t{{rank=same; {" ".join([str(i) for i in group_index])}}};\n' for group_index in self.grouped_doc_index]

        reverse_year_list = self.year_list[::-1]
        year_edge_list = [(year, reverse_year_list[idx+1]) for idx,
                          year in enumerate(reverse_year_list) if idx < len(reverse_year_list)-1]
        dot_year_node_list = [f'\t{year} [ shape="plaintext" ];\n' for year in self.year_list]
        dot_year_edge_list = [f'\t{edge[0]} -> {edge[1]} [ style = invis ];\n' for edge in year_edge_list]
        dot_text = 'digraph metadata{\n\trankdir = BT;\n'

        for dot_group in dot_groups:
            dot_text += dot_group

        for dot_year_node in dot_year_node_list:
            dot_text += dot_year_node

        for dot_year_edge in dot_year_edge_list:
            dot_text += dot_year_edge

        for dot_edge in dot_edge_list:
            dot_text += dot_edge
        dot_text += '}'
        return dot_text

    def generate_graph_node_file(self) -> pd.DataFrame:
        # source_type会对节点信息产生影响
        if self.source_type == 'wos':
            use_cols = ['doc_index', 'AU', 'TI', 'PY', 'SO', 'LCS', 'TC']
        elif self.source_type == 'cssci':
            use_cols = ['doc_index', 'AU', 'TI', 'PY', 'SO', 'LCS']
        elif self.source_type == 'scopus':
            use_cols = ['doc_index', 'AU', 'TI', 'PY', 'SO', 'LCS', 'TC']
        else:
            raise ValueError('invalid source type')
        graph_node_df = self.docs_df.loc[self.node_list, use_cols]
        if 'TC' in graph_node_df.columns:
            graph_node_df.rename(columns={'TC': 'GCS'}, inplace=True)
        return graph_node_df

    def _export_graph_node_file(self, file_path: str):
        self.generate_graph_node_file().to_excel(file_path, index=False)