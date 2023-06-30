from typing import List


class Vertice:
    def __init__(self, indice: int, rotulo: str) -> None:
        self.indice = indice
        self.rotulo = rotulo
        self.grau: int = 0
        self.vizinhos_saintes: List[Vertice] = []
        self.vizinhos_entrantes: List[Vertice] = []
