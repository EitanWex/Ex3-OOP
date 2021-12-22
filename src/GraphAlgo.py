from src.GraphAlgoInterface import GraphAlgoInterface

from GRF_Node import GRF_Node

class GraphAlgo(GraphAlgoInterface):
    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass