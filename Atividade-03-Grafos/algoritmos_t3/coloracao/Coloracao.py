from itertools import combinations
from grafo.Vertice import Vertice
from grafo.Grafo import Grafo
from typing import List, Tuple
from math import inf

class Coloracao:
    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
        self.numero_cromatico: List[int] = []
        self.coloracao_minima: int = inf

    def execute(self) -> None:
        self.processarAlgoritmo()
        self.imprimir()

    def processarAlgoritmo(self) -> None:
        tamanho = 2 ** self.grafo.qtdVertices()
        vetor_x = [inf] * tamanho
        vetor_x[0] = 0
        conjunto = self.grafo.vertices
        conjunto_potencia = []
        arestas = []

        for tamanho in range(len(conjunto) + 1):
            for comb in combinations(conjunto.keys(), tamanho):
                valores_comb = [conjunto[chave] for chave in comb]
                conjunto_potencia.append(valores_comb)
        
        copia_conjunto_potencia = conjunto_potencia[:]
        
        iterador = iter(conjunto_potencia)
        next(iterador)
        
        s = 1

        for subconjunto_potencia in iterador:
            arestas = []
            for i, vertice_u in enumerate(subconjunto_potencia):
                for j, vertice_v in enumerate(subconjunto_potencia[i:]):
                    if ((vertice_v not in vertice_u.vizinhos_saintes) and (vertice_v not in vertice_u.vizinhos_entrantes)):
                        if (vertice_v == vertice_u):
                            aresta = [vertice_v]
                        else:
                            aresta = [vertice_u, vertice_v]
                        if aresta not in arestas:
                            arestas.append(aresta)
                
            resultado = self.cim(len(subconjunto_potencia), arestas) 

            for i in resultado:
                copia_subconjunto_potencia = subconjunto_potencia.copy()

                for elemento in i:
                    if elemento in subconjunto_potencia: 
                        copia_subconjunto_potencia.remove(elemento)

                indice = copia_conjunto_potencia.index(copia_subconjunto_potencia)

                if ((vetor_x[indice] + 1) < vetor_x[s]):
                    vetor_x[s] = vetor_x[indice] + 1
            s = s + 1

        self.numero_cromatico = vetor_x
        self.coloracao_minima = max(vetor_x)
   
    
    def cim(self, tam: int, arestas: List[Tuple[Vertice, Vertice]]) -> None:
        tamanho = 2 ** tam
        r = []

        arestas = sorted(arestas, key=len)

        for i in arestas:
            novo_conjunto = []
            for tamanho in range(len(i) + 1):
                for comb in combinations(i, tamanho):
                    novo_conjunto.append(list(comb))
            for subconjunto in novo_conjunto:
                if subconjunto in r:
                    r.remove(subconjunto)
            r.append(i)

        return r


    def imprimir(self) -> None:
        print("ALGORITMO DE LAWLER\n")
        print("VETOR X: ", self.numero_cromatico)
        print("\nCOLORACAO MINIMA: ", self.coloracao_minima)