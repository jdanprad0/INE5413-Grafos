from Vertice import Vertice


class Arco:
    def __init__(self, vertice1: Vertice, vertice2: Vertice, peso: float) -> None:
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.peso = peso
