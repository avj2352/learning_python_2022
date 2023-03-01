'''
Graph datastructure
'''
from typing import Union, List

AlphaNumeric = Union[int, str, float]

class GraphNode:
    def __init__(self, key: AlphaNumeric):
        self.key = key
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

class Graph:
    def __init__(self, directed: bool = False):
        self.nodes = []
        self.edges = []
        self.directed = directed

    def add_node(self, key: AlphaNumeric):
        node = GraphNode(key)
        self.nodes.append(node)

    def get_node(self, key: AlphaNumeric):
        node = list(filter(lambda item: item.key == key, self.nodes))
        if len(node) > 0:
            return node[0]
        else:
            return None

    def add_edge(self, k1: AlphaNumeric, k2: AlphaNumeric):
        n1 = self.get_node(k1)
        n2 = self.get_node(k2)
        if n1 and n2:
            n1.add_neighbor(n2)
            self.edges.append(f'{k1}-{k2}')
            if not self.directed:
                n2.add_neighbor(n1)


    def print(self):
        def serialize(item):
            key, neighbors = item.key, item.neighbors
            result = key
            if len(neighbors):
                keys = map(lambda n: n.key, neighbors)
                result += f"=>{','.join(keys)}"
                return result
        result_list: List = map(serialize, self.nodes) if self.nodes else []
        return '\n'.join(result_list)    

    def print_primitive(self):
        result = {}
        for item in self.nodes:
            result[item.key] = map(lambda n: n.key, item.neighbors)
        return result

    def parse_primitive(self, graph_obj):
        for key in graph_obj.keys():
            self.add_node(key)
            for item in graph_obj[key]:
                self.add_edge(key, item)


def build_graph(list: List) -> dict:
    graph = {}
    for item in list:
        [a,b] = item
        if a not in graph.keys(): graph[a] = []
        if b not in graph.keys(): graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

# TESTING

def test_graph():
  graph = Graph(True)

  # add nodes
  graph.add_node('Kyle')
  graph.add_node('Anna')
  graph.add_node('Krios')
  graph.add_node('Tali')

  # add relationships
  graph.add_edge('Kyle', 'Anna')
  graph.add_edge('Anna', 'Kyle')
  graph.add_edge('Kyle', 'Krios')
  graph.add_edge('Kyle', 'Tali')
  graph.add_edge('Anna', 'Krios')
  graph.add_edge('Anna', 'Tali')
  graph.add_edge('Krios', 'Anna')
  graph.add_edge('Tali', 'Kyle')

  # printing
  print(graph.print())
  
  # print primitive format
  # print(f'Graph primitive format: {graph.printPrimitive()}')

test_graph()
'''
 prints the following relationship
 Kyle => Anna Krios Tali
 Anna => Kyle Krios Tali
 Krios => Anna
 Tali => Kyle
 Graph primitive format: {"Kyle":["Anna","Krios","Tali"],"Anna":["Kyle","Krios","Tali"],"Krios":["Anna"],"Tali":["Kyle"]}
'''
