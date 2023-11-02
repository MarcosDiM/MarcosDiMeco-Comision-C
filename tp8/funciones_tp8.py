
#Funcion ejercicio 1

def digits(num):
    #Convierte el número a una cadena para contar los dígitos
    str_num = str(num)
    #Verifica si el número es negativo y ajusta la longitud si es necesario
    if str_num[0] == "-":
        return len(str_num) - 1  #Resta 1 para excluir el signo negativo
    else:
        return len(str_num)  #Devuelve la longitud de la cadena (número de dígitos)
    

# Funcion ejercicio 2

def is_potency(n, b):
    #Caso base: si n es igual a b, es una potencia de b
    if n == b:
        return True
    #Caso base: si n es menor que b y no divisible por b, no es una potencia de b
    if n < b or n % b != 0:
        return False
    #Llamada recursiva dividiendo n por b
    return is_potency(n // b, b)

#Funcion ejercicio 3

def positions_of(a, b, index=0, positions=None):
    #Inicializa la lista de posiciones en la primera llamada a la función
    if positions is None:
        positions = []
    
    #Encuentra la próxima ocurrencia de b en a a partir del índice actual
    position = a.find(b, index)
    
    #Si se encontró una ocurrencia, agrega su posición a la lista y busca la siguiente
    if position != -1:
        positions.append(position)
        #Llama recursivamente a la función para encontrar más ocurrencias después de la posición actual
        positions_of(a, b, position + 1, positions)
    
    return positions

#Funciones ejercicio 4

#Definición de la función even que determina si un número es par
def even(n):
    #Caso base: si n es 1, retorna False (1 no es par)
    if n == 1:
        return False
    else:
        #Llama a la función odd con el argumento n-1 y devuelve su resultado
        return odd(n - 1)

#Definición de la función odd que determina si un número es impar
def odd(n):
    #Caso base: si n es 1, retorna True (1 es impar)
    if n == 1:
        return True
    else:
        #Llama a la función even con el argumento n-1 y devuelve su resultado
        return even(n - 1)


#Funcion ejercicio 5

#Función recursiva para encontrar el máximo en una lista
def find_max(numbers):
    #Caso base: si la lista tiene un solo elemento, ese es el máximo
    if len(numbers) == 1:
        return numbers[0]
    else:
        #Llama recursivamente a la función con la lista sin el primer elemento
        remaining = find_max(numbers[1:])
        #Compara el primer elemento con el máximo encontrado en la lista restante
        if numbers[0] > remaining:
            return numbers[0]  #Si el primer elemento es mayor, es el nuevo máximo
        else:
            return remaining  #Si el máximo de la lista restante es mayor, sigue siendo el máximo


#Funcion ejerciccio 6

#Definición de la función que repite los elementos de la lista
def repeat_element(my_list, repeater):
    #Caso base: si repeater es 1, devuelve la lista tal cual
    if repeater == 1:
        return my_list
    else:
        new_list = []  #Lista vacía para almacenar los elementos repetidos
        #Itera sobre los elementos de la lista original
        for item in my_list:
            #Extiende la nueva lista con el elemento repetido repeater veces
            new_list.extend([item] * repeater)
        #Llamada recursiva con la nueva lista y repeater decrementado en 1
        return repeat_element(new_list, repeater - 1)

#Funcion ejercicio 7

def k(n, p):
    #Caso base: si n es 1, retorna p como resultado
    if n == 1:
        return p
    else:
        #Llamada recursiva: multiplica n por p y agrega el resultado a la llamada recursiva con n - 1
        return n * p + k(n - 1, p)

#Funcionres ejercicio 8

#Definición de la función recursiva pascal que calcula el valor en la fila n y columna k del Triángulo de Pascal
def pascal(n, k):
    #Casos base: los valores en los bordes del Triángulo de Pascal son siempre 1
    if k == 0 or k == n:
        return 1
    else:
        #Llamadas recursivas para calcular el valor en la posición (n, k) sumando los valores de las posiciones (n-1, k-1) y (n-1, k)
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

#Funciones ejercicio 9

#Definición de la función recursiva que genera combinaciones de longitud k
def combinations(my_list, k, prefix=""):
    #Caso base: si la longitud requerida (k) es 0, imprimir la combinación actual
    if k == 0:
        print(prefix)
    else:
        #Para cada elemento en la lista, llamar recursivamente la función con k-1 y el elemento añadido al prefijo
        for i in my_list:
            combinations(my_list, k - 1, prefix + i)

#Funciones ejercicio 10

#Definición de la función sheet_size_A que calcula las dimensiones de una hoja A(N)
def sheet_size_A(n):
    #Caso base: hoja A0
    if n == 0:
        #Retorna las dimensiones de la hoja A0
        return (841, 1189)
    else:
        #Llamada recursiva para obtener las dimensiones de la hoja A(N-1)
        previous_width, previous_length = sheet_size_A(n - 1)
        #Calcula las dimensiones de la hoja A(N) doblando al medio la hoja A(N-1)
        actual_length = previous_width  #El largo de la hoja A(N) es igual al ancho de la hoja A(N-1)
        actual_width = previous_length / 2  # El ancho de la hoja A(N) se reduce a la mitad del largo de la hoja A(N-1)
        #Retorna las dimensiones de la hoja A(N) como una tupla de enteros
        return (int(actual_width), int(actual_length))
