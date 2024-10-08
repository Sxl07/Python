import random
import time
import matplotlib.pyplot as plt

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]
    
    L[n1] = float('inf')
    R[n2] = float('inf')
    
    i = 0
    j = 0
    
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1 
    return A

def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        A = mergeSort(A, p, q)
        A = mergeSort(A, q + 1, r)
        A = merge(A, p, q, r)
    return A


sizes = [100, 500, 1000,2500, 5000,7500, 10000,12500,15000,17500, 20000]
times = []

for size in sizes:
    arr = [random.randint(0, 100) for _ in range(size)]
    start_time = time.time()
    mergeSort(arr, 0, len(arr) - 1)
    end_time = time.time()
    times.append((end_time - start_time)*1000)

plt.plot(sizes, times, marker='o')
plt.title('Tiempo de ejecución de mergeSort')
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo (milisegundos)')
plt.grid(True)
plt.show()
