import time
import matplotlib.pyplot as plt

# Función de backtracking para el problema de la mochila
def knapsack_backtracking(weights, values, capacity):
    n = len(weights)
    max_value = 0

    def backtrack(index, current_weight, current_value):
        nonlocal max_value
        if index == n:
            if current_weight <= capacity:
                max_value = max(max_value, current_value)
            return
        
        # Excluye el elemento actual
        backtrack(index + 1, current_weight, current_value)
        
        # Incluye el elemento actual si no excede la capacidad
        if current_weight + weights[index] <= capacity:
            backtrack(index + 1, current_weight + weights[index], current_value + values[index])
    
    backtrack(0, 0, 0)
    return max_value

# Función de ramificación y poda para el problema de la mochila
def knapsack_branch_and_bound(weights, values, capacity):
    n = len(weights)
    max_value = 0

    def branch_and_bound(index, current_weight, current_value, potential_value):
        nonlocal max_value
        if index == n:
            if current_weight <= capacity:
                max_value = max(max_value, current_value)
            return
        
        # Poda: si el valor potencial ya es menor que max_value, no continuar
        if potential_value <= max_value:
            return
        
        # Excluir el elemento actual
        branch_and_bound(index + 1, current_weight, current_value, potential_value - values[index])

        # Incluir el elemento actual si no excede la capacidad
        if current_weight + weights[index] <= capacity:
            branch_and_bound(index + 1, current_weight + weights[index], current_value + values[index], potential_value)
    
    branch_and_bound(0, 0, 0, sum(values))
    return max_value

# Función para medir el tiempo de ejecución de ambos algoritmos
def measure_execution_time(algorithm, weights, values, capacity, sizes):
    times = []
    for size in sizes:
        start = time.time()
        algorithm(weights[:size], values[:size], capacity)
        end = time.time()
        times.append((end - start) * 1000)  # Convertir el tiempo a milisegundos
    return times

# Datos de ejemplo más grandes y capacidad de la mochila
weights = [2, 3, 4, 5, 9, 7, 8, 5, 6, 4, 3, 10, 6, 8, 9, 3, 5, 4, 6, 8]
values = [3, 4, 8, 8, 10, 7, 6, 5, 6, 4, 3, 12, 5, 9, 10, 2, 4, 3, 7, 9]
capacity = 20
sizes = list(range(20, 1000, 20))  # Tamaños de problema en incrementos

# Medición de tiempo para ambos algoritmos
times_backtracking = measure_execution_time(knapsack_backtracking, weights, values, capacity, sizes)
times_branch_and_bound = measure_execution_time(knapsack_branch_and_bound, weights, values, capacity, sizes)

# Graficar los resultados
plt.plot(sizes, times_backtracking, label="Backtracking", marker='o')
plt.plot(sizes, times_branch_and_bound, label="Ramificación y Poda", marker='o')
plt.xlabel("Tamaño del problema")
plt.ylabel("Tiempo de ejecución (ms)")  # Mostrar tiempo en milisegundos
plt.legend()
plt.title("Backtracking vs Ramificación y Poda")
plt.grid(True)
plt.show()
