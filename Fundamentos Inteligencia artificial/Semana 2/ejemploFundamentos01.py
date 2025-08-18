# Representación del laberinto
laberinto = [
    ["S", 0, "X", 0, 0],
    [0, "X", 0, "X", 0],
    [0, 0, 0, "X", 0],
    ["X", "X", 0, 0, 0],
    [0, 0, 0, "X", "G"]
]

def acciones_posibles(f, c):
    movimientos = []
    direcciones = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "O": (0, -1)
    }
    for a, (df, dc) in direcciones.items():
        nf, nc = f + df, c + dc
        if 0 <= nf < len(laberinto) and 0 <= nc < len(laberinto[0]):
            if laberinto[nf][nc] != "X":
                movimientos.append(a)
    return movimientos

print("Desde (0,0) puedo ir a:", acciones_posibles(2,2))
