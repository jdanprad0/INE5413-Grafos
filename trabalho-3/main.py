import sys
import os

# adiciona o caminho da pasta "grafo", "algoritmos" e suas subpastas ao sys.path
modules_paths = [
    os.path.abspath(os.path.join("algoritmos_t1/caminhoMinimo")),
    os.path.abspath(os.path.join("algoritmos_t1/busca")),
    os.path.abspath(os.path.join("algoritmos_t1/ciclo")),
    os.path.abspath(os.path.join("algoritmos_t2/componentesFortementeConexas")),
    os.path.abspath(os.path.join("algoritmos_t2/kruskal")),
    os.path.abspath(os.path.join("algoritmos_t2/ordenacaoTopologica")),
    os.path.abspath(os.path.join("algoritmos_t3/coloracao")),
    os.path.abspath(os.path.join("grafo")),
]
sys.path.extend(modules_paths)

from algoritmos_t1.caminhoMinimo.FloydWarshall import FloydWarshall
from algoritmos_t1.ciclo.CicloEuleriano import CicloEuleriano
from algoritmos_t1.caminhoMinimo.Dijkistra import Dijkstra
from algoritmos_t1.busca.BuscaLargura import BuscaLargura
from algoritmos_t2.kruskal.Kruskal import Kruskal
from algoritmos_t2.ordenacaoTopologica.OrdenacaoTopologica import OrdenacaoTopologica
from algoritmos_t2.componentesFortementeConexas.ComponentesFortementeConexas import ComponentesFortementeConexas
from algoritmos_t3.coloracao.Coloracao import Coloracao
from algoritmos_t3.edmondsKarp.EdmondsKarp import EdmondsKarp
from algoritmos_t3.hopcroftKarp.HopcroftKarp import HopcroftKarp
from grafo.Grafo import Grafo
from random import randint


pasta_testes = "testes/"

# obtem todos os arquivos na pasta testes
arquivos_testes = os.listdir(pasta_testes)

# cria um menu com os nomes dos arquivos
menu_arquivos = "\n".join(
    [f"{i+1}. {arquivo}" for i, arquivo in enumerate(arquivos_testes)]
)
menu_arquivos = f"0. Sair\n{menu_arquivos}"

# cria um submenu com as opcoes de algoritmos
menu_algoritmos = """
Selecione o algoritmo desejado:
0. Sair
1. Busca em Largura
2. Ciclo Euleriano
3. Dijkstra
4. Floyd-Warshall
5. Componentes Fortemente Conexas
6. Ordenação Topológica
7. Kruskal
8. Edmonds-Karp
9. Hopcroft-Karp
10. Coloração de Vértices
11. Voltar para o menu anterior
"""

while True:
    # imprime o menu de arquivos e pede a escolha do usuario
    print(f"Arquivos disponíveis:\n{menu_arquivos}")
    escolha_arquivo = input(
        "Escolha um arquivo para ler (digite o número correspondente ou 0 para sair): "
    )

    # trata a escolha do usuario para o menu de arquivos
    try:
        escolha_arquivo = int(escolha_arquivo)
        if escolha_arquivo == 0:
            print("Saindo...")
            break
        elif escolha_arquivo < 0 or escolha_arquivo > len(arquivos_testes):
            raise ValueError
        else:
            nome_arquivo = pasta_testes + arquivos_testes[escolha_arquivo - 1]
            grafo = Grafo()
            grafo.ler(nome_arquivo)
            print(f"Lendo arquivo {nome_arquivo}...")

            while True:
                # imprime o submenu de algoritmos e pede a escolha do usuario
                print(menu_algoritmos)
                escolha_algoritmo = input(
                    "Escolha um algoritmo (digite o número correspondente): "
                )

                vertice_origem = (
                    None  # substitua None aqui para o indice do vertice que deseja
                )

                # trata a escolha do usuario para o submenu de algoritmos
                try:
                    escolha_algoritmo = int(escolha_algoritmo)

                    if escolha_algoritmo == 0:
                        print("Saindo...")
                        sys.exit()

                    elif escolha_algoritmo == 1:
                        print("\nBusca em Largura selecionada.\n")

                        if not vertice_origem:
                            vertice_escolhido = randint(1, grafo.qtdVertices())
                        else:
                            vertice_escolhido = vertice_origem
                        print(
                            f"Vértice de origem escolhido: {vertice_escolhido} - {grafo.vertices[vertice_escolhido].rotulo}"
                        )

                        BuscaLargura(grafo, vertice_escolhido).execute()

                    elif escolha_algoritmo == 2:
                        print("\nCiclo Euleriano selecionado.\n")
                        CicloEuleriano(grafo).execute()

                    elif escolha_algoritmo == 3:
                        print("\nDijkstra selecionado.\n")

                        if not vertice_origem:
                            vertice_escolhido = randint(1, grafo.qtdVertices())
                            vertice_escolhido = grafo.vertices[vertice_escolhido]
                        else:
                            vertice_escolhido = grafo.vertices[vertice_origem]
                        print(
                            f"Vértice de origem escolhido: {vertice_escolhido.indice} - {vertice_escolhido.rotulo}"
                        )

                        Dijkstra(grafo, vertice_escolhido).execute()

                    elif escolha_algoritmo == 4:
                        print("\nFloyd-Warshall selecionado.\n")
                        FloydWarshall(grafo).execute()
                    
                    elif escolha_algoritmo == 5:
                        print("\nComponentes Fortemente Conexas selecionado.\n")
                        ComponentesFortementeConexas(grafo).execute()

                    elif escolha_algoritmo == 6:
                        print("\nOrdenação Topológica selecionado.\n")
                        OrdenacaoTopologica(grafo).execute()

                    elif escolha_algoritmo == 7:
                        print("\nKruskal selecionado.\n")
                        Kruskal(grafo).execute()

                    elif escolha_algoritmo == 8:
                        print("\nEdmonds-Karp selecionado.\n")
                        EdmondsKarp(grafo).execute()

                    elif escolha_algoritmo == 9:
                        print("\nHopcroft-Karp selecionado.\n")
                        HopcroftKarp(grafo).execute()

                    elif escolha_algoritmo == 10:
                        print("\nColoração de Vértices selecionado.\n")
                        Coloracao(grafo).execute()


                    elif escolha_algoritmo == 8:
                        print("Voltando para o menu de arquivos...\n")
                        break

                    else:
                        raise ValueError

                except ValueError:
                    print("Opção inválida. Tente novamente.")

    except ValueError:
        print("Opção inválida. Tente novamente.\n")
