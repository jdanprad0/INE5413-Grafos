from itertools import combinations
from grafo.Vertice import Vertice
from grafo.Grafo import Grafo
from typing import Dict, List, Tuple
from math import inf

class Coloracao:
    def __init__(self, grafo: Grafo) -> None:
        self.grafo = grafo
       
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
                valores_comb = [conjunto[chave] for chave in comb]  # Lista dos valores correspondentes às chaves
                conjunto_potencia.append(valores_comb)
        
        #print(conjunto_potencia)
        iterador = iter(conjunto_potencia)
        next(iterador) 
        
        posicao = 1

        for subconjunto_potencia in iterador:
            arestas = []
            for i, vertice_u in enumerate(subconjunto_potencia):
                for j, vertice_v in enumerate(subconjunto_potencia[i:]):
                    if ((vertice_v not in vertice_u.vizinhos_saintes) and (vertice_v not in vertice_u.vizinhos_entrantes)):
                        print(vertice_u.rotulo, vertice_v.rotulo)
                        if (vertice_v == vertice_u):
                            aresta = [vertice_v.rotulo]
                        else:
                            aresta = [vertice_u.rotulo, vertice_v.rotulo]
                        arestas.append(aresta)
            print(arestas)
            print("*******************************************************************")

            self.cim(subconjunto_potencia, aresta)   
            
           

            # cim_grafo_linha = self.cim(subconjunto_potencia, aresta)
               
            # for i in cim_grafo_linha:
            #      resultado_subtracao = {chave: valor for chave, valor in subconjunto_potencia.items() if chave not in i}
            #      i = conjunto_potencia.index(resultado_subtracao)

            #      if ((vetor_x[i] + 1) < vetor_x[s]):
            #          vetor_x[s] = vetor_x[i] + 1

        
    
    def cim(self, vertices: List[Vertice], arestas: List[Tuple[Vertice, Vertice]]) -> None:
        print("oiiiiiiiiiiiiiiiiiiiiiiiiii")
        tamanho = 2 ** len(vertices)
        r = []
        conjunto_potencia = []

        for i in arestas:
            for tamanho in range(len(i) + 1):
                for comb in combinations(i.keys(), tamanho):
                    valores_comb = [i[chave] for chave in comb]  # Lista dos valores correspondentes às chaves
                    conjunto_potencia.append(valores_comb)
            for subconjunto in conjunto_potencia:
                if subconjunto in r:
                    r.remove(subconjunto)
            r.append(i)


        print(r)



    def imprimir(self) -> None:
        print("")
    


