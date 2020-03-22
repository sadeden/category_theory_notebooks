from itertools import product
from graphviz import Digraph

class DynamicalSystem():
    def __init__(self, definition, engine='dot'):
        domain = set(definition.keys())
        codomain = set(definition.values())
        if not codomain <= domain :
            raise ValueError('Codomain is not a subset of Domain')
        self.map = definition
        self.set = domain
        self.engine = engine

    def __mul__(self, other):
        product_graph = {}
        for pair in product(iter(self.set), iter(other.set)):
            product_graph[pair] = (self.image(pair[0]), other.image(pair[1]))
        return DynamicalSystem(product_graph)

    def image(self, element):
        if element not in self.set:
            raise ValueError('element is not part of the set')
        return self.map[element]

    def to_dot(self):
        dot = Digraph(engine=self.engine)
        for element in iter(self.set):
            dot.node(str(element), shape='point')
        for element in iter(self.set):
            dot.edge(str(element), str(self.image(element)), arrowsize='0.5', arrowhead='ovee')
        return dot

    def _repr_svg_(self):
        return self.to_dot()._repr_svg_()
