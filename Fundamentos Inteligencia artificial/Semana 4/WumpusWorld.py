# --- Mundo del Wumpus simplificado: modelamiento base ---
from collections import deque
import heapq

# Grilla 4x4 de ejemplo (el docente puede cambiarla en clase)
grid = [
    [".",".",".","P"],
    [".","G","P","."],
    [".",".",".","."],
    ["A",".","P","."]
]

ROWS, COLS = len(grid), len(grid[0])

# Estado inicial (A) y objetivo (G)

def find(symbol):
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == symbol:
                return (r, c)
    return None

INI = find("A")
GOAL = find("G")

# Movimientos vlidos: 4 direcciones (N,S,E,O)
DIRS4 = [(1,0),(-1,0),(0,1),(0,-1)]

def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def passable(r, c):
    # No se puede pasar por pozos
    return grid[r][c] != "P"

def neighbors(r, c):
    """Acciones aplicables: movimiento a celdas adyacentes libres."""
    for dr, dc in DIRS4:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc) and passable(nr, nc):
            yield (nr, nc)

def manhattan(a, b):
    """Heurstica para A*: distancia Manhattan (admisible en 4-dir, costo=1)."""
    (r1, c1), (r2, c2) = a, b
    return abs(r1 - r2) + abs(c1 - c2)

def reconstruct(parent, goal):
    """Reconstruye la ruta desde el inicio hasta ’goal’ usando el diccionario ’parent’."""
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    return path[::-1]

# --- Puntos de integracin (implementar en otro archivo o debajo):
# def bfs(start=INI, goal=GOAL): ...
# def dfs(start=INI, goal=GOAL): ...
# def astar(start=INI, goal=GOAL): ...