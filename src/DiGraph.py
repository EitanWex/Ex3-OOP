from hashlib import new

from src.GraphInterface import GraphInterface

from GRF_Node import GRF_Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.Vertices = {}           #קודקודי הגרף
        self.num_of_ver = 0
        self.num_of_edges = 0
        self.mc_count= 0        #the count for number of operations performed



    def v_size(self) -> int:
       return self.num_of_ver

    def e_size(self) -> int:
        return self.num_of_edges

    def get_mc(self) -> int:
        return self.mc_count

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.Vertices.get(id1) is None or self.Vertices.get(id2) is None or weight <= 0 or id1 == id2:
            return False

        self.Vertices.get(id1).edge_O[id2] = weight
        self.Vertices.get(id2).edge_IN[id1] = weight
        self.num_of_edges += 1
        self.mc_count += 1
        return True


    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.Vertices.get(node_id) is None:
            return False
        self.Vertices[node_id] = GRF_Node(node_id, pos)
        self.num_of_ver += 1
        self.mc_count += 1       #number of operations performed on the graph
        return True

    def remove_node(self, node_id: int) -> bool:
      if self.Vertices.get(node_id) is not None:
          for k in self.Vertices.get(node_id).edge_O.keys():
              self.Vertices.get(node_id).edge_O.pop(node_id)
              self.num_of_edges -= 1
              self.num_of_ver -= 1
          for m in self.Vertices.get(node_id).edge_IN.pop(node_id):
              self.Vertices.get(node_id).edge_IN.pop(node_id)
              self.num_of_edges -= 1
              self.num_of_ver -= 1
          self.mc_count += 1
          self.Vertices.pop(node_id)
          return True
      return False








    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.vertices.get(node_id1) is not None and self.Vertices.get(node_id2) is not None:
            if self.Vertices.get(node_id1).edge_O is not None:
                self.Vertices.get(node_id1).edge_O.pop(node_id1)
                self.Vertices.get(node_id2).edge_IN.pop(node_id2)
                self.num_of_edges -= 1
                self.mc_count += 1
                return True

        return False

