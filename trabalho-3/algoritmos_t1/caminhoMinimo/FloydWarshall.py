from grafo.Grafo import Grafo
from grafo.Vertice import Vertice
from math import inf


class FloydWarshall:
    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
        self.matriz_distancia = [
            [[inf] * self.grafo.qtdVertices() for _ in range(self.grafo.qtdVertices())]
        ]

    def execute(self) -> None:
        self.processarAlgoritmo()
        self.imprimir()

    def processarAlgoritmo(self) -> None:
        quantidade_vertices = self.grafo.qtdVertices()

        for u in range(quantidade_vertices):
            for v in range(quantidade_vertices):
                if u == v:
                    self.matriz_distancia[0][u][v] = 0
                elif self.grafo.haArco(u + 1, v + 1):
                    self.matriz_distancia[0][u][v] = self.grafo.peso(u + 1, v + 1)

        for k in range(1, quantidade_vertices + 1):
            self.matriz_distancia.append(self.matriz_distancia[k - 1].copy())
            for u in range(quantidade_vertices):
                for v in range(quantidade_vertices):
                    if (
                        self.matriz_distancia[k - 1][u][k - 1]
                        + self.matriz_distancia[k - 1][k - 1][v]
                        < self.matriz_distancia[k - 1][u][v]
                    ):
                        self.matriz_distancia[k][u][v] = (
                            self.matriz_distancia[k - 1][u][k - 1]
                            + self.matriz_distancia[k - 1][k - 1][v]
                        )

    def imprimir(self):
        quantidade_vertices = self.grafo.qtdVertices()

        for k in range(1, quantidade_vertices + 1):
            distancias = []
            for u in range(quantidade_vertices):
                distancias.append(self.matriz_distancia[k][k - 1][u])
            print(f"\n{k}", end=": ")
            distancias_formatadas = [f"{distancia:.2f}" for distancia in distancias]
            print(",".join(distancias_formatadas), end="")
        print("\n")
