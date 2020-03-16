from itertools import product
from graphviz import Digraph

class DynamicalSystem():
    def __init__(self, definition):
        domain = set(definition.keys())
        codomain = set(definition.values())
        if not codomain <= domain :
            raise ValueError('Codomain is not a subset of Domain')
        self.graph = definition
        self.system_set = domain

    def __mul__(self, other):
        product_graph = {}
        for pair in product(iter(self.system_set), iter(other.system_set)):
            product_graph[pair] = (self.image(pair[0]), other.image(pair[1]))
        return DynamicalSystem(product_graph)

    def image(self, element):
        if element not in self.system_set:
            raise ValueError('element is not part of the set')
        return self.graph[element]

    def to_dot(self):
        dot = Digraph()
        for element in iter(self.system_set):
            dot.node(str(element), shape='point')
        for element in iter(self.system_set):
            dot.edge(str(element), str(self.image(element)), arrowsize='0.5', arrowhead='ovee')
        return dot
