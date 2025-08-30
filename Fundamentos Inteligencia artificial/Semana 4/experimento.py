# experimento.py
# Script para probar y comparar BFS, DFS y A*

from busquedas import bfs, dfs, astar
from WumpusWorld import INI, GOAL

def imprimir_resultados(nombre, camino, orden_expansion):
    print(f"\nAlgoritmo: {nombre}")
    if camino:
        print(f"Camino encontrado: {camino}")
        print(f"Costo del camino: {len(camino)-1}")
    else:
        print("No se encontró camino.")
    print(f"Nodos expandidos: {len(orden_expansion)}")
    print(f"Orden de expansión: {orden_expansion}")

if __name__ == "__main__":
    camino_bfs, orden_bfs = bfs()
    imprimir_resultados("BFS", camino_bfs, orden_bfs)

    camino_dfs, orden_dfs = dfs()
    imprimir_resultados("DFS", camino_dfs, orden_dfs)

    camino_astar, orden_astar = astar()
    imprimir_resultados("A*", camino_astar, orden_astar)
