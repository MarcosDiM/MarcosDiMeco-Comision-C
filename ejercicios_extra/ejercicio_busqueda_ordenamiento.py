# Bubble sort: Algoritmo de ordenamiento de burbuja
def bubble_sort(arr):
    n = len(arr)  # Obtiene la longitud de la lista
    for i in range(n):  # Itera sobre cada elemento de la lista
        for j in range(0, n-i-1):  # Itera sobre los elementos no ordenados , el bucle se detiene en el penultimo elemento
            # Compara elementos adyacentes y los intercambia si están en el orden incorrecto
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambia los elementos
    return arr  # Devuelve la lista ordenada

# Selection sort: Algoritmo de ordenamiento de selección
def selection_sort(arr):
    n = len(arr)  # Obtiene la longitud de la lista
    for i in range(n):  # Itera sobre cada elemento de la lista
        min_index = i  # Supone que el elemento actual es el mínimo
        # Encuentra el índice del mínimo elemento en el resto de la lista
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Intercambia el elemento mínimo encontrado con el primer elemento no ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr  # Devuelve la lista ordenada

# Insertion sort: Algoritmo de ordenamiento de inserción
def insertion_sort(arr):
    n = len(arr)  # Obtiene la longitud de la lista
    for i in range(1, n):  # Itera sobre cada elemento desde el segundo hasta el último
        key = arr[i]  # Almacena el elemento actual que se va a insertar en su lugar correcto
        j = i - 1  # Inicializa un índice para comparar con los elementos anteriores
        # Mueve los elementos mayores que key una posición adelante de su posición actual
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Inserta el elemento en su lugar correcto
    return arr  # Devuelve la lista ordenada

# Merge sort: Algoritmo de ordenamiento por fusión
def merge_sort(arr):
    if len(arr) <= 1:  # Caso base: si la lista tiene 0 o 1 elementos, está ordenada
        return arr

    mid = len(arr) // 2  # Encuentra el índice medio de la lista
    left = arr[:mid]  # Divide la lista en dos mitades
    right = arr[mid:]

    # Llamadas recursivas para ordenar y combinar las mitades
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)  # Combina las mitades ordenadas y devuelve la lista ordenada

def merge(left, right):
    result = []  # Lista para almacenar el resultado combinado
    i = j = 0  # Índices para recorrer las listas izquierda y derecha respectivamente

    # Combina las dos listas ordenadas en una sola lista ordenada
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # Compara los elementos de las listas izquierda y derecha
            result.append(left[i])  # Agrega el elemento de la lista izquierda al resultado
            i += 1  # Mueve el índice de la lista izquierda
        else:
            result.append(right[j])  # Agrega el elemento de la lista derecha al resultado
            j += 1  # Mueve el índice de la lista derecha

    # Añade los elementos restantes de las listas, si los hay
    result.extend(left[i:])
    result.extend(right[j:])
    return result  # Devuelve la lista combinada y ordenada

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]  
print("Bubble Sort:", bubble_sort(arr.copy()))
print("Selection Sort:", selection_sort(arr.copy()))
print("Insertion Sort:", insertion_sort(arr.copy()))
print("Merge Sort:", merge_sort(arr.copy()))
