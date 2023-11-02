import funciones_tp8

#Ejercicio 1

while True:
    num = int(input("Ingrese un número: "))
    
    print(f"{num} tiene {funciones_tp8.digits(num)} dígitos")
    condition = str(input("Ingrese N para salir, para continuar cualquier tecla: ")).title()
    if condition == "N":
        break
    else:
        continue


#Ejercicio 2

#Corroborar que el número ingresado sea un entero
while True:
    #Entrada de datos desde el usuario
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))

    #Llamada a la función is_potency para verificar si num1 es potencia de num2
    potency = funciones_tp8.is_potency(num1, num2)
        
    #Verificación del resultado y muestra del mensaje correspondiente
    if potency == True:
        print(f"{num1} es potencia de {num2}")
        break
    else:
        print(f"{num1} no es potencia de {num2}")
        break


#Ejercicio 3

#Solicita al usuario dos cadenas de texto
string1 = input("Ingrese una cadena de texto: ")
string2 = input("Ingrese otra cadena: ")

#Llama a la función positions_of y almacena el resultado en la variable result
result = funciones_tp8.positions_of(string1, string2)

#Imprime las posiciones donde se encontró la segunda cadena en la primera cadena
print(result)


#Ejercicio 4

#Bucle para solicitar al usuario un número entero positivo
while True:
    try:
        #Solicita al usuario que ingrese un número y lo convierte a entero
        num = int(input("Ingrese un número entero: "))
        
        #Verifica si el número ingresado es positivo
        if num > 0:
            #Llama a la función even con el número ingresado y verifica si es True (par)
            if funciones_tp8.even(num) == True:
                print(f"{num} es par")
            else:
                print(f"{num} es impar")
            #Sale del bucle ya que se ingresó un número válido
            break
        else:
            #Si el número ingresado no es positivo, muestra un mensaje de error
            print("¡ERROR! Ingrese solo números enteros positivos")
            
    except ValueError:
        #Si se ingresa algo que no es un número entero, muestra un mensaje de error
        print("¡ERROR! Ingrese solo números enteros positivos")


#Ejercicio 5
#Lista de números
numbers = [1, 4, 6, 2, 3]

#Llama a la función find_max con la lista de números y almacena el resultado en la variable result
result = funciones_tp8.find_max(numbers)

#Imprime el máximo encontrado en la lista
print(result)

#Ejercicio 6

#Inicialización de la lista
my_list = []

#Bucle para ingresar elementos en la lista hasta que se ingrese 0
while True:
    element = input("Ingrese un elemento para la lista, para dejar de agregar ingrese 0: ")
    if element == "0":
        break
    else:
        my_list.append(element)

#Bucle para ingresar la cantidad de repeticiones y corroborar que se ingrese un valor correcto
while True:
    try:
        repeater = int(input("Ingrese la cantidad de veces que desea repetir cada elemento de la lista: "))
        break
    except ValueError:
        print("¡ERROR! Ingrese un número válido")

#Llamada a la función y muestra del resultado
print(funciones_tp8.repeat_element(my_list, repeater))

#Ejercicio 7

while True:
    try:
        #Solicita al usuario dos números enteros
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        
        #Inicia el cálculo recursivo llamando a la función k con los números ingresados y muestra el resultado
        print(f"El resultado es {funciones_tp8.k(num1, num2)}")
        break
    except ValueError:
        #Captura errores si el usuario no ingresa números enteros
        print("¡ERROR! Ingrese números válidos")

#Ejercicio 8

#Bucle principal para solicitar al usuario la fila y columna del Triángulo de Pascal
while True:
    try:
        #Solicita al usuario el número de fila y columna (números enteros)
        row = int(input("Ingrese el número de fila: "))
        column = int(input("Ingrese el número de columna: "))

        #Verifica que la columna sea menor o igual a la fila para calcular el valor correspondiente en el Triángulo de Pascal
        if column <= row:
            result = funciones_tp8.pascal(row, column)
            #Muestra el valor en la fila y columna especificadas del Triángulo de Pascal
            print(f"El valor en la fila {row} y columna {column} del Triángulo de Pascal es: {result}")
        else:
            #Muestra un mensaje de error si la columna es mayor que la fila
            print("La columna no puede ser mayor que la fila.")
        break  #Sale del bucle si la entrada es válida
    except ValueError:
        #Captura la excepción si el usuario ingresa algo que no es un número entero
        print("Por favor, ingrese números enteros válidos.")

#Ejercicio 9

#Lista para almacenar los caracteres ingresados por el usuario
my_list = []
#Variable de control para el bucle principal
validator = True

#Bucle para ingresar caracteres hasta que el usuario ingrese "0"
while True:
    my_string = input("Ingrese un caracter (sin repetir) u oprima 0(cero) para salir: ")
    if my_string == "0":
        validator = False
        break
    else:
        #Verificar si el caracter ya existe en la lista
        if my_string in my_list:
            print("¡ERROR! Ese caracter ya existe en la lista")
        else:
            #Agregar el caracter a la lista
            my_list.append(my_string)

#Bucle para ingresar la longitud de las combinaciones
while True:
    try:
        length = int(input("Ingrese la longitud de las combinaciones: "))
        #Llamar a la función con la lista y la longitud especificada
        funciones_tp8.combinations(my_list, length)
        break
    except ValueError:
        print("¡ERROR! Ingrese un número válido")


#Ejercicio 10

#Bucle principal para solicitar al usuario el tipo de hoja y mostrar sus dimensiones
while True:
    try:
        validator = True
        #Bucle interno para validar la entrada del usuario
        while validator:
            #Solicita al usuario el tipo de hoja deseada (número entero)
            sheet_type = int(input("Ingrese de qué tipo de hoja necesita saber el tamaño: Hoja A"))
            if sheet_type < 0:
                #Si el valor ingresado es negativo, muestra un mensaje de error
                print("¡ERROR! El valor debe ser mayor que 0 (cero)")
            else:
                #Si el valor ingresado es válido, calcula las dimensiones y muestra el resultado
                result = funciones_tp8.sheet_size_A(sheet_type)
                print(f"La hoja A{sheet_type} mide {result[0]} X {result[1]}mm")
                validator=False #Validator cambia su valor a False para salir del bucle interno
        break  #Sale del bucle principal si la entrada es válida
    except ValueError:
        #Captura la excepción si el usuario ingresa algo que no es un número entero
        print("¡ERROR! Ingrese un número válido")
