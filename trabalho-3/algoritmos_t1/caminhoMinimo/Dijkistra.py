from grafo.Vertice import Vertice
from grafo.Grafo import Grafo
from typing import List, Tuple
from math import inf
import heapq


class Dijkstra:
    def __init__(self, grafo: Grafo, origem: Vertice) -> None:
        self.grafo = grafo
        self.origem = origem
        self.distancia: List[float] = [inf] * self.grafo.qtdVertices()
        self.antecessor: List[int] = [None] * self.grafo.qtdVertices()
        self.heap: List[Tuple[float, int]] = [
            (inf, i) for i in range(1, self.grafo.qtdVertices() + 1)
        ]

    def execute(self) -> None:
        self.processarAlgoritmo()
        self.imprimir()

    def processarAlgoritmo(self) -> Tuple[List, List]:
        self.distancia[self.origem.indice - 1] = 0
        self.heap[self.origem.indice - 1] = (0, self.origem.indice)

        heapq.heapify(self.heap)

        while self.heap:
            (dist_atual, atual) = heapq.heappop(self.heap)

            for vizinho in self.grafo.vertices[atual].vizinhos_saintes:
                self.distancia_vizinho = dist_atual + self.grafo.peso(
                    atual, vizinho.indice
                )

                if self.distancia_vizinho < self.distancia[vizinho.indice - 1]:
                    indice = self.heap.index(
                        (self.distancia[vizinho.indice - 1], vizinho.indice)
                    )
                    self.heap[indice] = (self.distancia_vizinho, vizinho.indice)
                    self.distancia[vizinho.indice - 1] = self.distancia_vizinho
                    heapq.heapify(self.heap)
                    self.antecessor[vizinho.indice - 1] = atual

        return (self.distancia, self.antecessor)

    def imprimirCaminho(self, num_vertice: int) -> str:
        if self.antecessor[num_vertice - 1] is None:
            return str(num_vertice)
        else:
            caminho = self.imprimirCaminho(self.antecessor[num_vertice - 1])
            return f"{caminho},{num_vertice}"

    def imprimirResultado(self, num_vertice: int, caminho: str) -> None:
        print(
            "{}: {}; d={:.2f}".format(
                num_vertice, caminho, self.distancia[num_vertice - 1]
            )
        )

    def imprimir(self) -> None:
        for vertice in range(1, self.grafo.qtdVertices() + 1):
            self.imprimirResultado(vertice, self.imprimirCaminho(vertice))
