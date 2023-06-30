from grafo.Grafo import *
from collections import deque

class EdmondsKarp:
    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
        self.fluxo = {arco: 0 for arco in self.grafo.arcos.values()}

        self.fluxo = {}
        for arco in self.grafo.arcos.values():
            self.fluxo[(arco.vertice1.indice, arco.vertice2.indice)] = 0
            self.fluxo[(arco.vertice2.indice, arco.vertice1.indice)] = 0

        for arco in list(self.grafo.arcos.values()):
            if (arco.vertice2.indice, arco.vertice1.indice) not in self.grafo.arcos:
                self.grafo.arcos[(arco.vertice2.indice, arco.vertice1.indice)] = Arco(arco.vertice2, arco.vertice1, 0)
                arco.vertice2.vizinhos_saintes.append(arco.vertice1)


    def buscaLargura(self, s: int, t: int) -> dict:
        parent = {s: None}
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for v in self.grafo.vizinhos_saintes(u):
                if v.indice not in parent and self.grafo.arcos[(u, v.indice)].peso - self.fluxo[(u, v.indice)] > 0:
                    parent[v.indice] = u
                    if v.indice == t:
                        return parent
                    queue.append(v.indice)
        return None

    def execute(self) -> None:
        self.processarAlgoritmo()
        self.imprimir()

    def processarAlgoritmo(self) -> None:
        s = 1  
        t = len(self.grafo.vertices)

        max_flow = 0

        while True:
            parent = self.buscaLargura(s, t)
            if parent is None:
                break

            path_flow = float("Inf")
            v = t
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.grafo.arcos[(u, v)].peso - self.fluxo[(u, v)])
                v = u

            max_flow += path_flow

            v = t
            while v != s:
                u = parent[v]
                self.fluxo[(u, v)] += path_flow
                self.fluxo[(v, u)] -= path_flow
                v = u

        self.max_flow = max_flow

    def imprimir(self) -> None:
        print("O fluxo máximo possível é %d" % self.max_flow)
