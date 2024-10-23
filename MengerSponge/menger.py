from vpython import box, vector, color
import numpy as np

def create_menger_sponge(level):
    """
    Crea una esponja de Menger de un nivel dado.
    Args:
    level (int): El nivel de recursividad para la esponja de Menger.
    Returns:
    np.ndarray: Una matriz tridimensional que representa la esponja de Menger.
    """
    size = 3 ** level  # Tamaño del cubo en este nivel
    sponge = np.ones((size, size, size), dtype=int)  # Inicializar la esponja con 1s (cubo sólido)

    def divide(x, y, z, size, level):
        """
        Función recursiva que subdivide el cubo y elimina los subcubos centrales utilizando coordenadas (-1, 0, 1).
        Args:
        x, y, z (int): Las coordenadas actuales.
        size (int): El tamaño actual del cubo a subdividir.
        level (int): El nivel de profundidad actual en la recursión.
        """
        if level == 0:
            return  # Caso base: no hacemos nada más si llegamos al nivel 0

        # Tamaño de los subcubos más pequeños
        new_size = size // 3

        # Iterar sobre los 27 subcubos posibles en una cuadrícula 3x3x3
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    # Eliminar el subcubo central en el medio y los subcubos centrales de cada cara y borde
                    if (i == 1 and j == 1) or (i == 1 and k == 1) or (j == 1 and k == 1):
                        sponge[x + i * new_size:x + (i + 1) * new_size, 
                               y + j * new_size:y + (j + 1) * new_size, 
                               z + k * new_size:z + (k + 1) * new_size] = 0
                    else:
                        # Llamada recursiva para subdividir los otros subcubos
                        divide(x + i * new_size, y + j * new_size, z + k * new_size, new_size, level - 1)

    # Llamar a la función de división recursiva
    divide(0, 0, 0, size, level)

    return sponge

def draw_menger_sponge_vpython(level):
    """
    Dibuja la esponja de Menger en 3D utilizando Vpython.
    Args:
    level (int): Nivel de la esponja de Menger.
    """
    # Crear la esponja de Menger como matriz 3D
    sponge = create_menger_sponge(level)
    size = sponge.shape[0]
    cube_size = 1  # Tamaño de cada cubo individual

    # Iterar sobre los valores de la esponja y dibujar solo donde el valor sea 1
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if sponge[x, y, z] == 1:
                    # Crear un cubo en las coordenadas correspondientes
                    box(pos=vector(x * cube_size, y * cube_size, z * cube_size),
                        size=vector(cube_size, cube_size, cube_size),
                        color=color.cyan)

# Ejemplo de uso
level = 3  # Cambia el nivel para aumentar o disminuir la complejidad
draw_menger_sponge_vpython(level)

# Mantener la ventana abierta
while True:
    pass  # Esto evita que la ventana se cierre automáticamente
