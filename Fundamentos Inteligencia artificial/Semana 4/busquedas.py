# busquedas.py
# Implementación de BFS, DFS y A* para el Mundo del Wumpus
# Reutiliza el modelamiento de WumpusWorld.py

from WumpusWorld import neighbors, manhattan, INI, GOAL
from collections import deque
import heapq

def bfs(start=INI, goal=GOAL):
    """Búsqueda en anchura (Breadth-First Search)."""
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    orden_expansion = []
    
    while queue:
        current = queue.popleft()
        orden_expansion.append(current)
        
        if current == goal:
            # Reconstruir el camino usando el starter
            from WumpusWorld import reconstruct
            camino = reconstruct(parent, goal)
            return camino, orden_expansion
        for neighbor in neighbors(*current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    return None, orden_expansion  # No se encontró camino

def dfs(start=INI, goal=GOAL):
    """Búsqueda en profundidad (Depth-First Search)."""
    stack = [start]
    visited = set([start])
    parent = {start: None}
    orden_expansion = []
    while stack:
        current = stack.pop()
        orden_expansion.append(current)
        if current == goal:
            from WumpusWorld import reconstruct
            camino = reconstruct(parent, goal)
            return camino, orden_expansion
        for neighbor in neighbors(*current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
    return None, orden_expansion  # No se encontró camino

def astar(start=INI, goal=GOAL):
    """Búsqueda A* usando la heurística de Manhattan."""
    open_set = []
    heapq.heappush(open_set, (manhattan(start, goal), 0, start))  # (f, g, nodo)
    parent = {start: None}
    g_score = {start: 0}
    orden_expansion = []
    visited = set()
    while open_set:
        _, g, current = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        orden_expansion.append(current)
        if current == goal:
            from WumpusWorld import reconstruct
            camino = reconstruct(parent, goal)
            return camino, orden_expansion
        for neighbor in neighbors(*current):
            tentative_g = g + 1  # costo uniforme
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f = tentative_g + manhattan(neighbor, goal)
                parent[neighbor] = current
                heapq.heappush(open_set, (f, tentative_g, neighbor))
    return None, orden_expansion  # No se encontró camino
