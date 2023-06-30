from grafo.Grafo import Grafo
from grafo.Vertice import Vertice

class OrdenacaoTopologica:
    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
        self.visitado = [False] * (self.grafo.qtdVertices() + 1)
        self.pilha = []

    def execute(self) -> None:
        self.processarAlgoritmo()
        self.imprimir()

    def processarAlgoritmo(self) -> None:
        for vertice in self.grafo.vertices.values():
            if not self.visitado[vertice.indice]:
                self.buscaProfunda(vertice)

    def buscaProfunda(self, vertice: Vertice):
        self.visitado[vertice.indice] = True
        for vizinho in vertice.vizinhos_saintes:
            if not self.visitado[vizinho.indice]:
                self.buscaProfunda(vizinho)
        self.pilha.append(vertice)

    def imprimir(self) -> None:
        while self.pilha:
            vertice = self.pilha.pop()
            if self.pilha:
                print(f'{vertice.rotulo} → ', end='')
            else:
                print(vertice.rotulo)
