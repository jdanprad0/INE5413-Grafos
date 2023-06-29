from itertools import combinations
from grafo.Grafo import Grafo
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

        for tamanho in range(len(conjunto) + 1):
            for comb in combinations(conjunto.keys(), tamanho):
                subconjunto = {k: conjunto[k].rotulo for k in comb}
                conjunto_potencia.append(subconjunto)
        
        
        iterador = iter(conjunto_potencia)
        next(iterador)  # Pular o primeiro elemento
        lista3 = list()
        dicionario1 = {2: "B", 3: "C", 4: "D"}
        dicionario2 = {3: "C"}
        lista3.append(dicionario1)
        lista3.append({2: "B", 3: "C", 4: "D"})
        lista3.append({2: "B", 3: "C"})
        lista3.append({2: "B", 4: "D"})
        print(lista3)
        resultado_subtracao = {chave: valor for chave, valor in dicionario1.items() if chave not in dicionario2}
        print(lista3.index(resultado_subtracao))
        print(resultado_subtracao)

      

        posicao = 1

        for subconjunto in iterador:
            s = posicao
            grafo_linha = 2

            for i in cim(grafo_linha):
                resultado_subtracao = {chave: valor for chave, valor in subconjunto.items() if chave not in i}
                i = lista_conjunto_potencia.index(resultado_subtracao)

                if ((vetor_x[i] + 1) < vetor_x[s]):
                    vetor_x[s] = vetor_x[i] + 1

        
    
    def cim(self) -> None:
        id = 0

    def imprimir(self) -> None:
        print("")
    


