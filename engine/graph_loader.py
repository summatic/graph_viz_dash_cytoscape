import networkx as nx
import numpy as np
import os
import pandas as pd


class GraphLoader:
    def __init__(self, dataset="github"):
        self.dataset = dataset

    @staticmethod
    def _read_pandas(data_path):
        tab = pd.read_csv(
            data_path, encoding="utf8", sep=",", dtype={"switch": np.int32}
        )
        return tab

    def _load_dataset(self, end):
        file_path = os.path.dirname(__file__)
        package_path = os.path.dirname(file_path)
        data_path = os.path.join(package_path, "data", self.dataset, end)
        data = self._read_pandas(data_path)
        return data

    def get_graph(self):
        nodes_df = self._load_dataset("target.csv")
        nodes_df = nodes_df.set_index("id")

        graph = nx.Graph()
        idx2name = []
        for idx, row in nodes_df.iterrows():
            graph.add_node(row["name"], name=row["name"], target=row["ml_target"])
            idx2name.append(row["name"])

        edges_df = self._load_dataset("edges.csv")
        for idx, row in edges_df.iterrows():
            source = idx2name[row["id_1"]]
            target = idx2name[row["id_2"]]

            graph.add_edge(source, target)

        return graph


loader = GraphLoader()
graph = loader.get_graph()
