from typing import Dict, List, Tuple
from Vertice import Vertice
from Arco import Arco
from math import inf
import sys


class Grafo:
    def __init__(self) -> None:
        self.vertices: Dict[int, Vertice] = {}
        self.arcos: Dict[Tuple[int, int], Arco] = {}

    def qtdVertices(self) -> int:
        return len(self.vertices.keys())

    def qtdArcos(self) -> int:
        return len(self.arcos.keys())

    def grau(self, vertice: int) -> int:
        return self.vertices[vertice].grau

    def rotulo(self, vertice: int) -> str:
        return self.vertices[vertice].rotulo

    def vizinhos_saintes(self, vertice: int) -> List[Vertice]:
        return self.vertices[vertice].vizinhos_saintes

    def haArco(self, vertice1: int, vertice2: int) -> bool:
        return (vertice1, vertice2) in self.arcos or (
            vertice2,
            vertice1,
        ) in self.arcos

    def peso(self, vertice1: int, vertice2: int) -> float:
        ha_arco = self.haArco(vertice1, vertice2)

        if ha_arco:
            if (vertice1, vertice2) in self.arcos:
                return self.arcos[vertice1, vertice2].peso
            else:
                return self.arcos[vertice2, vertice1].peso
        return inf

    def ler(self, arquivo: str) -> None:
        try:
            with open(arquivo, "r") as arq:
                # ler numero de vertices
                num_vertices = int(arq.readline().strip().split()[1])

                # ler rotulos dos vertices
                for _ in range(num_vertices):
                    linha = arq.readline().strip()

                    conteudo = linha.split()

                    indice = int(conteudo[0])
                    rotulo = (" ".join(conteudo[1:])).strip()

                    self.vertices[indice] = Vertice(indice, rotulo)

                # pular linha que contem a string *edges ou *arcs
                arq.readline()

                # ler arcos e/ou arcos
                for linha in arq:
                    vertice1, vertice2, peso = linha.split()

                    vertice1 = self.vertices[int(vertice1)]
                    vertice2 = self.vertices[int(vertice2)]

                    # se for grafo nao dirigido considere como aresta
                    self.arcos[vertice1.indice, vertice2.indice] = Arco(
                        vertice1, vertice2, float(peso)
                    )

                    # para caro de grafo dirigido, em grafo nao dirigido considere apenas uma das listas
                    if vertice2 not in vertice1.vizinhos_saintes:
                        vertice1.vizinhos_saintes.append(vertice2)
                    if vertice1 not in vertice2.vizinhos_entrantes:
                        vertice2.vizinhos_entrantes.append(vertice1)

                    vertice1.grau += 1

        except FileNotFoundError:
            print("O arquivo não foi encontrado. Saindo...")
            sys.exit()

        except IOError:
            print("Erro ao abrir o arquivo. Saindo...")
            sys.exit()
