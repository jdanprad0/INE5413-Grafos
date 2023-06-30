from grafo.Grafo import Grafo
from grafo.Vertice import Vertice

class ComponentesFortementeConexas:
    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
        self.componentes = []
        self.index = 0
        self.pilha = []

        for v in self.grafo.vertices.values():
            v.index = None
            v.lowlink = None

    def execute(self) -> None:
        self.processarAlgoritmo()
        self.imprimir()

    def processarAlgoritmo(self) -> None:
        for vertice in self.grafo.vertices.values():
            if vertice.index is None:
                self.buscaProfunda(vertice)

    def buscaProfunda(self, vertice: Vertice) -> None:
        vertice.index = self.index
        vertice.lowlink = self.index
        self.index += 1
        self.pilha.append(vertice)

        for vizinho in vertice.vizinhos_saintes:
            if vizinho.index is None:
                self.buscaProfunda(vizinho)
                vertice.lowlink = min(vertice.lowlink, vizinho.lowlink)
            elif vizinho in self.pilha:
                vertice.lowlink = min(vertice.lowlink, vizinho.index)

        if vertice.lowlink == vertice.index:
            componente = []
            while True:
                v = self.pilha.pop()
                componente.append(v.indice)
                if v == vertice:
                    break
            self.componentes.append(componente)

    def imprimir(self) -> None:
        print()
        for componente in self.componentes:
            print("{", ", ".join(map(str, componente)), "}")