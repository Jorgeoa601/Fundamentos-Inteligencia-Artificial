import heapq
import math

# 0 = libre, 1 = obstaculo
mapa = [
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
]


inicio = (0, 3)     
objetivo = (10, 4)  

# ---------------------- Heuristicas
def euclidiana(a, b):
    (x1, y1), (x2, y2) = a, b
    return math.hypot(x2 - x1, y2 - y1)

def manhattan(a, b):
    (x1, y1), (x2, y2) = a, b
    return abs(x2 - x1) + abs(y2 - y1)

# --- A* en matriz ---
def astar(mapa, inicio, objetivo, heuristica):
    filas, cols = len(mapa), len(mapa[0])
    openpq = []
    heapq.heappush(openpq, (heuristica(inicio, objetivo), 0, inicio))
    parent = {inicio: None}
    best_g = {inicio: 0}
    expandidos = set()
    orden = []

    # Movimientos: arriba, abajo, izquierda, derecha
    movimientos = [(-1,0), (1,0), (0,-1), (0,1)]

    while openpq:
        f, g, actual = heapq.heappop(openpq)
        if actual in expandidos:
            continue
        expandidos.add(actual)
        orden.append(actual)

        if actual == objetivo:
            # Reconstruir camino
            camino = []
            cur = actual
            while cur is not None:
                camino.append(cur)
                cur = parent[cur]
            return list(reversed(camino)), g, orden

        for dx, dy in movimientos:
            nx, ny = actual[0] + dx, actual[1] + dy
            vecino = (nx, ny)
            if 0 <= nx < cols and 0 <= ny < filas and mapa[ny][nx] == 0:
                ng = g + 1
                if ng < best_g.get(vecino, float("inf")):
                    best_g[vecino] = ng
                    parent[vecino] = actual
                    nf = ng + heuristica(vecino, objetivo)
                    heapq.heappush(openpq, (nf, ng, vecino))

    return None, None, orden  # No hay solución

# ------------- Print con ambos resultados ------------------
if __name__ == "__main__":
    print("--- A* con heurística Euclidiana ---")
    camino_e, costo_e, orden_e = astar(mapa, inicio, objetivo, euclidiana)
    print("Camino encontrado:", camino_e)
    print("Costo total:", costo_e)
    print("Nodos expandidos:", len(orden_e))

    print("\n--- A* con heurística Manhattan ---")
    camino_m, costo_m, orden_m = astar(mapa, inicio, objetivo, manhattan)
    print("Camino encontrado:", camino_m)
    print("Costo total:", costo_m)
    print("Nodos expandidos:", len(orden_m))