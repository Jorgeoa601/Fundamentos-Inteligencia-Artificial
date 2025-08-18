from collections import deque

# Definimos los nombres para mayor claridad
G, L, O, C = 0, 1, 2, 3

def es_valido(estado):
    # No puede quedar la oveja sola con el lobo sin el granjero
    for b in [0, 1]:
        if estado[L] == b and estado[O] == b and estado[G] != b:
            return False
        if estado[O] == b and estado[C] == b and estado[G] != b:
            return False
    return True

def posibles_movimientos(estado):
    movimientos = []
    lado = estado[G]
    # El granjero puede cruzar solo
    nuevo = list(estado)
    nuevo[G] = 1 - lado
    movimientos.append(tuple(nuevo))
    # El granjero puede cruzar con L, O o C si están en la misma orilla
    for x in [L, O, C]:
        if estado[x] == lado:
            nuevo = list(estado)
            nuevo[G] = 1 - lado
            nuevo[x] = 1 - lado
            movimientos.append(tuple(nuevo))
    return movimientos

def bfs():
    inicial = (0, 0, 0, 0)
    objetivo = (1, 1, 1, 1)
    visitados = set([inicial])  # Marcar inicial como visitado
    padre = {inicial: None}
    q = deque([inicial])
    while q:
        actual = q.popleft()
        if actual == objetivo:
            # Reconstruir el camino
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padre[actual]
            camino.reverse()
            return camino
        for sig in posibles_movimientos(actual):
            if sig not in visitados and es_valido(sig):
                visitados.add(sig)
                padre[sig] = actual
                q.append(sig)
    return None

def dfs():
    inicial = (0, 0, 0, 0)
    objetivo = (1, 1, 1, 1)
    visitados = set([inicial])  # Marcar inicial como visitado
    padre = {inicial: None}
    stack = [inicial]
    while stack:
        actual = stack.pop()
        if actual == objetivo:
            # Reconstruir el camino
            camino = []
            while actual is not None:
                camino.append(actual)
                actual = padre[actual]
            camino.reverse()
            return camino
        for sig in posibles_movimientos(actual):
            if sig not in visitados and es_valido(sig):
                visitados.add(sig)
                padre[sig] = actual
                stack.append(sig)
    return None

# Ejecutar y mostrar la solución BFS
try:
    print("\n--- Solución usando BFS ---")
    camino = bfs()
    nombres = ['Granjero', 'Lobo', 'Oveja', 'Col']
    if camino is None:
        print("No se encontró solución al problema.")
    else:
        for paso, estado in enumerate(camino):
            orilla_izq = [nombres[i] for i in range(4) if estado[i] == 0]
            orilla_der = [nombres[i] for i in range(4) if estado[i] == 1]
            print(f"Paso {paso}: Izquierda: {orilla_izq} | Derecha: {orilla_der}")
        print(f"\n¡Solución encontrada en {len(camino)-1} cruces!")
except Exception as e:
    print(f"Error durante la ejecución BFS: {e}")

# Ejecutar y mostrar la solución DFS
try:
    print("\n--- Solución usando DFS ---")
    camino = dfs()
    nombres = ['Granjero', 'Lobo', 'Oveja', 'Col']
    if camino is None:
        print("No se encontró solución al problema.")
    else:
        for paso, estado in enumerate(camino):
            orilla_izq = [nombres[i] for i in range(4) if estado[i] == 0]
            orilla_der = [nombres[i] for i in range(4) if estado[i] == 1]
            print(f"Paso {paso}: Izquierda: {orilla_izq} | Derecha: {orilla_der}")
        print(f"\n¡Solución encontrada en {len(camino)-1} cruces!")
except Exception as e:
    print(f"Error durante la ejecución DFS: {e}")