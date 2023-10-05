import tp5funciones

'''
#Ejercicio 1 - Verificar DNI

#Pido al usuario ingresar su DNI, cito la funcion que lo verifica y en caso que este bien imprime DNI, sino imprime "El DNI NO ES VALIDO"
dni = input("Ingrese su DNI: ")

if tp5funciones.verify_dni(dni) == True:
    print("DNI: ", dni)
else:
    print("DNI INGRESADO NO VALIDO")

#Ejercicio 2 - Ultima palabra del string

#El usuario debe ingresar una frase y luego cito la funcion que retorna la ultima palabra.
phrase = str(input("Ingrese una frase: "))
tp5funciones.last_word(phrase)

#Ejercicio 3 - Identificador de cada socio

#Ingresa en un ciclo el cual pide ingresar nombre apellido y dni y lo guarda en una lista
while True :
    print("Para salir ingrese un espacio vacio.")
    print("Ingrese nombre y dni de socio \n Debe ingresa su nombre y solo un apellido seguido de su dni y separado por espacios \n Para salir ingrese un espacio vacio")
    user = str(input("Ingrese usuario: "))
    list_user = []
    list_user = user.split()

    #Define la salida del programa si se ingresa un espacio vacio
    if len(list_user) == 0:
        print("El programa ha finalizado")
        break
    #En caso de que ingrese mas o menos elementos de los requeridos resulta error y vuelve a comenzar el ciclo
    elif len(list_user) > 4 or len(list_user) < 3:
        print("ERROR Formato de usuario no valido")
        continue

    #Ingresa la lista en una funcion la cual la define nombre apellido y dni en variables distintas
    name_user, lastname_user, dni_user = tp5funciones.define_name(list_user)

    #Verifica el dni, si no es valido vuelve a comenzar el ciclo
    if tp5funciones.verify_dni(dni_user) == False :
        print("DNI INGRESADO NO VALIDO, VUELVA A INGRESAR EL USUARIO")
        continue
    
    #Define el username o ID del usuario mediante una funcion y termina el ciclo
    username = tp5funciones.create_username(name_user, lastname_user, dni_user)
    break
print(f"Su ID de usuario es: {username}")
'''

#Ejercicio 7 - Numero mayor y menor ingresados

numbers_entered = []

while True:
    entered_num = int(input("Ingresar numero, para finalizar ingrese 0: "))
    if entered_num == 0:
        break
    else:
        numbers_entered.append(entered_num)
        continue

results= tp5funciones.number_mayor_minor(numbers_entered) 
number_major = results[0]
number_minor = results[1]

print(f"El mayor numero ingresado es {number_major} y el menor es {number_minor}")


#Ejercicio 12 - Diccionario de una frase ingresada

while True:
    phrase_entered = str(int("Ingrese una frase y sus palabras seran agregadas al diccionario"))
    if phrase_entered == "":
        break
    
