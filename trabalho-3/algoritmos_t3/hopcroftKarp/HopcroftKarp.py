from grafo.Grafo import Grafo
from collections import deque

class HopcroftKarp:
    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
        self.dist = [0] * (len(self.grafo.vertices) + 1)
        self.par = [0] * (len(self.grafo.vertices) + 1)
       
    def buscaLargura(self):
        queue = deque()
        for u in range(1, len(self.grafo.vertices) + 1):
            if self.par[u] == 0:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float("Inf")
        self.dist[0] = float("Inf")
        while queue:
            u = queue.popleft()
            if u != 0:
                for v in self.grafo.vizinhos_saintes(u):
                    if self.dist[self.par[v.indice]] == float("Inf"):
                        self.dist[self.par[v.indice]] = self.dist[u] + 1
                        queue.append(self.par[v.indice])
        return self.dist[0] != float("Inf")

    def buscaProfundidade(self, u):
        if u == 0:
            return True
        for v in self.grafo.vizinhos_saintes(u):
            if self.dist[self.par[v.indice]] == self.dist[u] + 1 and self.buscaProfundidade(self.par[v.indice]):
                self.par[v.indice] = u
                self.par[u] = v.indice
                return True
        self.dist[u] = float("Inf")
        return False

    def execute(self) -> None:
        self.processarAlgoritmo()
        self.imprimir()

    def processarAlgoritmo(self) -> None:
        self.par = [0] * (len(self.grafo.vertices) + 1)
        self.dist = [0] * (len(self.grafo.vertices) + 1)
        matching = 0
        while self.buscaLargura():
            for u in range(1, len(self.grafo.vertices) + 1):
                if self.par[u] == 0 and self.buscaProfundidade(u):
                    matching += 1
        self.matching = matching

    def imprimir(self) -> None:
        print("O número máximo de emparelhamentos é %d" % self.matching)
