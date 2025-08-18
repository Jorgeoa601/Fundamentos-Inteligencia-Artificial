from collections import deque

laberinto = [
    ["S", 0, "X", 0, 0, 0, "X", 0, 0, 0],
    [0, "X", 0, "X", "X", 0, "X", 0, "X", 0],
    [0, "X", 0, 0, 0, 0, 0, 0, "X", 0],
    [0, "X", "X", "X", 0, "X", "X", 0, "X", 0],
    [0, 0, 0, "X", 0, "X", 0, 0, 0, 0],
    ["X", "X", 0, "X", 0, "X", 0, "X", "X", 0],
    [0, 0, 0, 0, 0, 0, 0, "X", 0, 0],
    [0, "X", "X", "X", "X", "X", 0, "X", 0, "X"],
    [0, 0, 0, 0, 0, "X", 0, 0, 0, 0],
    ["X", "X", "X", "X", 0, "X", "X", "X", "X", "G"]
]

ROWS, COLS = len(laberinto), len(laberinto[0])
INI, OBJ = (0, 0), (9, 9)

DIRS = {
    "N": (-1, 0),
    "S": ( 1, 0),
    "E": ( 0, 1),
    "O": ( 0,-1),
}

def vecinos(r, c):
    for a, (dr, dc) in DIRS.items():
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and laberinto[nr][nc] != "X":
            yield (nr, nc), a

def reconstruir_camino(padre, meta):
    camino = []
    cur = meta
    while cur is not None:
        camino.append(cur)
        cur = padre.get(cur)
    camino.reverse()
    return camino

def bfs(inicio=INI, objetivo=OBJ):
    q = deque([inicio])
    padre = {inicio: None}
    visit = {inicio}
    orden = []

    while q:
        r, c = q.popleft()
        orden.append((r, c))
        if (r, c) == objetivo:
            return reconstruir_camino(padre, objetivo), orden
        for (nr, nc), _ in vecinos(r, c):
            if (nr, nc) not in visit:
                visit.add((nr, nc))
                padre[(nr, nc)] = (r, c)
                q.append((nr, nc))
    return None, orden

def dfs(inicio=INI, objetivo=OBJ, orden_acciones=("N","S","E","O")):
    stack = [inicio]
    padre = {inicio: None}
    visit = set()
    orden = []

    # Para que salga primero la acción 'N', empujamos en orden inverso
    preferencia = {a:i for i,a in enumerate(orden_acciones)}

    while stack:
        r, c = stack.pop()
        if (r, c) in visit:
            continue
        visit.add((r, c))
        orden.append((r, c))
        if (r, c) == objetivo:
            return reconstruir_camino(padre, objetivo), orden

        # recolecta vecinos y ordénalos según preferencia
        nbrs = []
        for (nr, nc), a in vecinos(r, c):
            if (nr, nc) not in visit:
                nbrs.append(((nr, nc), a))
        nbrs.sort(key=lambda x: preferencia[x[1]], reverse=True)  # push en reverso

        for (nr, nc), _ in nbrs:
            if (nr, nc) not in padre:
                padre[(nr, nc)] = (r, c)
            stack.append((nr, nc))
    return None, orden

camino_bfs, orden_bfs = bfs()
camino_dfs, orden_dfs = dfs()

print("BFS camino:", camino_bfs, "costo:", len(camino_bfs)-1)
print("DFS camino:", camino_dfs, "costo:", len(camino_dfs)-1)
print("BFS orden de expansión:", orden_bfs)
print("DFS orden de expansión:", orden_dfs)
