from grafo.Grafo import Grafo
from grafo.Vertice import Vertice
from random import choice
from typing import List, Tuple, Union


class CicloEuleriano:
    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
        self.visitado = {(v, u): False for (v, u) in self.grafo.arcos}
        self.ciclo: List[int] = []
        self.num_subciclo = 0

    def execute(self) -> None:
        haCiclo, ciclo = self.processarAlgoritmo()
        self.ciclo = ciclo
        self.imprimir(haCiclo)

    def processarAlgoritmo(self) -> None:
        vertice = self.grafo.vertices[1]
        return self.buscarSubcicloEuleriano(vertice)

    def buscarSubcicloEuleriano(self, vertice: Vertice) -> bool:
        ciclo = [vertice]
        vertice = vertice.indice
        t = vertice

        while True:
            if not False in self.visitado.values():
                return False, None

            for indice, valor in self.visitado.items():
                if not valor and (indice[0] == vertice or indice[1] == vertice):
                    nao_visitado = indice
                    break

            if nao_visitado:
                vertice1, vertice2 = nao_visitado

                if not (vertice1, vertice2) in self.visitado:
                    vertice2, vertice1 = nao_visitado

                self.visitado[vertice1, vertice2] = True
                vertice_vizinho = vertice1 if vertice1 != vertice else vertice2
                ciclo.append(self.grafo.vertices[vertice_vizinho])
                vertice = vertice_vizinho

            if t == vertice:
                break

        if False in self.visitado.values():
            vizitar = []

            for vertice in ciclo:
                for vertice_vizinho in vertice.vizinhos_saintes:
                    if (vertice.indice, vertice_vizinho.indice) in self.visitado:
                        if not self.visitado[(vertice.indice, vertice_vizinho.indice)]:
                            vizitar.append(vertice)

                    elif (vertice_vizinho.indice, vertice.indice) in self.visitado:
                        if not self.visitado[(vertice_vizinho.indice, vertice.indice)]:
                            vizitar.append(vertice)

            if vizitar:
                for vertice in vizitar:
                    haSubciclo, subciclo = self.buscarSubcicloEuleriano(vertice)

                    if haSubciclo == False:
                        return False, None

                    for vertice in ciclo:
                        if vertice.indice == subciclo[0].indice:
                            ciclo[
                                ciclo.index(vertice) : ciclo.index(vertice) + 1
                            ] = subciclo
                            break
                    break

        return True, ciclo

    def imprimir(self, haCiclo: bool) -> None:
        if haCiclo:
            print("1")
            print(",".join(str(vertice.indice) for vertice in self.ciclo))
        else:
            print("0")
