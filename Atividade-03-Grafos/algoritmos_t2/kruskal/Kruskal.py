from grafo.Grafo import Grafo

class Kruskal:
    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
        self.parente = [i for i in range(self.grafo.qtdVertices() + 1)]
        self.rank = [0 for _ in range(self.grafo.qtdVertices() + 1)]
        self.arvoreMinima = []

    def execute(self) -> None:
        self.processarAlgoritmo()
        self.imprimir()

    def processarAlgoritmo(self) -> None:
        edges = list(self.grafo.arcos.values())
        edges.sort(key=lambda arco: arco.peso)
        
        for edge in edges:
            root1 = self.find(edge.vertice1.indice)
            root2 = self.find(edge.vertice2.indice)
            
            if root1 != root2:
                self.arvoreMinima.append(edge)
                self.union(root1, root2)

    def imprimir(self) -> None:
        total_weight = sum(edge.peso for edge in self.arvoreMinima)
        print(total_weight)

        edges_str = ', '.join(
            f"{edge.vertice1.indice}-{edge.vertice2.indice}" for edge in self.arvoreMinima
        )
        print(edges_str)

    def find(self, node: int) -> int:
        if self.parente[node] == node:
            return node
        else:
            root = self.find(self.parente[node])
            self.parente[node] = root
            return root

    def union(self, node1: int, node2: int) -> None:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if self.rank[root1] > self.rank[root2]:
            self.parente[root2] = root1
        else:
            self.parente[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1
