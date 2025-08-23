import math
import heapq

coords = {
    "A": (0,0),
    "B": (2,1),
    "C": (5,2),
    "D": (6,5),
    "G": (8,3)
}

edges = {
    "A": {"B": 2},
    "B": {"A": 2, "C": 3},
    "C": {"B": 3, "D": 3, "G": 4},
    "D": {"C": 3, "G": 2},
    "G": {}
}

def euclidean(a, b="G"):
    (x1, y1), (x2, y2) = coords[a], coords[b]
    return math.hypot(x2 - x1, y2 - y1)

def manhattan(a, b="G"):
    (x1, y1), (x2, y2) = coords[a], coords[b]
    return abs(x2 - x1) + abs(y2 - y1)

def reconstruct(parent, goal):
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    return list(reversed(path))

def astar(start="A", goal="G", h=euclidean):
    # open set con prioridad por f = g + h
    openpq = []
    heapq.heappush(openpq, (h(start, goal), 0, start))  # (f, g, nodo)

    parent = {start: None}
    best_g = {start: 0}
    order = []  # para registrar el orden de expansión

    while openpq:
        f, g, u = heapq.heappop(openpq)

        # Salto de seguridad si hay una entrada obsoleta en la cola
        if g > best_g.get(u, float("inf")):
            continue

        order.append((u, g, h(u, goal), f))

        if u == goal:
            path = reconstruct(parent, goal)
            return path, g, order  # camino, costo óptimo, orden de expansión

        # Expandir vecinos
        for v, cost in edges[u].items():
            ng = g + cost
            if ng < best_g.get(v, float("inf")):
                best_g[v] = ng
                parent[v] = u
                nf = ng + h(v, goal)
                heapq.heappush(openpq, (nf, ng, v))

    return None, None, order  # sin solución

# --- Demo: correr con Euclidiana y con Manhattan ---
if __name__ == "__main__":
    path_e, cost_e, order_e = astar(h=euclidean)
    print("A* (Euclidiana)")
    print("  Camino:", path_e)
    print("  Costo :", cost_e)
    print("  Orden de expansión:", [n for (n, _, __, ___) in order_e])

    path_m, cost_m, order_m = astar(h=manhattan)
    print("\nA* (Manhattan)")
    print("  Camino:", path_m)
    print("  Costo :", cost_m)
    print("  Orden de expansión:", [n for (n, _, __, ___) in order_m])
