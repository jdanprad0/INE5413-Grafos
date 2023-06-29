from grafo.Grafo import Grafo
from typing import List
from math import inf


class BuscaLargura:
    def __init__(self, grafo: Grafo, origem: int) -> None:
        self.grafo = grafo
        self.origem = origem
        self.visitado: List[bool] = [False] * self.grafo.qtdVertices()
        self.distancia: List[float] = [inf] * self.grafo.qtdVertices()
        self.antecessor: List[int] = [None] * self.grafo.qtdVertices()

    def execute(self) -> None:
        self.processarAlgoritmo()
        self.imprimir()

    def processarAlgoritmo(self) -> None:
        self.visitado[self.origem - 1] = True
        self.distancia[self.origem - 1] = 0

        fila = [self.origem]

        while fila:
            atual = fila.pop(0)

            for vizinho in self.grafo.vertices[atual].vizinhos_saintes:
                if not self.visitado[vizinho.indice - 1]:
                    self.visitado[vizinho.indice - 1] = True
                    self.distancia[vizinho.indice - 1] = self.distancia[atual - 1] + 1
                    self.antecessor[vizinho.indice - 1] = atual
                    fila.append(vizinho.indice)

    def imprimir(self) -> None:
        nivel_vertices = {}

        for vertice, nivel in enumerate(self.distancia):
            if nivel in nivel_vertices:
                nivel_vertices[nivel].append(vertice + 1)
            else:
                nivel_vertices[nivel] = [vertice + 1]

        for nivel in sorted(nivel_vertices.keys()):
            vertices = nivel_vertices[nivel]
            print(f"{nivel}: {','.join(str(vertice) for vertice in vertices)}")
