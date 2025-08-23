import heapq  # módulo estándar de Python para trabajar con montículos (heaps)

# Creamos una lista vacía que será nuestro heap
heap = []

# Agregamos elementos usando heappush(heap, valor)
heapq.heappush(heap, 5)   # heap = [5]
heapq.heappush(heap, 3)   # heap = [3, 5]  (3 sube a la raíz porque es menor)
heapq.heappush(heap, 8)   # heap = [3, 5, 8]
heapq.heappush(heap, 1)   # heap = [1, 3, 8, 5]

print("Heap interno:", heap)  
# Internamente está organizado como árbol binario, 
# pero se almacena en una lista optimizada.

# Para extraer el menor elemento usamos heappop(heap)
min_value = heapq.heappop(heap)  
print("Mínimo extraído:", min_value)  # → 1
print("Heap después de pop:", heap)   # → [3, 5, 8]

# También podemos usar heappushpop(heap, valor)
# que inserta y extrae en una sola operación eficiente
heapq.heappushpop(heap, 2)  # inserta 2 y devuelve el menor
