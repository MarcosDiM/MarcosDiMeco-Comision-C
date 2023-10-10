import test_tp5funciones

#Ejercicio 1 - Verificar DNI

#Pido al usuario ingresar su DNI, cito la funcion que lo verifica y en caso que este bien imprime DNI, sino imprime "El DNI NO ES VALIDO"
dni = input("Ingrese su DNI: ")

if test_tp5funciones.verify_dni(dni) == True:
    print("DNI: ", dni)
else:
    print("DNI INGRESADO NO VALIDO")


#Ejercicio 2 - Ultima palabra del string

#El usuario debe ingresar una frase y luego cito la funcion que retorna la ultima palabra.
phrase = str(input("Ingrese una frase: "))
test_tp5funciones.last_word(phrase)


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
    name_user, lastname_user, dni_user = test_tp5funciones.define_name(list_user)

    #Verifica el dni, si no es valido vuelve a comenzar el ciclo
    if test_tp5funciones.verify_dni(dni_user) == False :
        print("DNI INGRESADO NO VALIDO, VUELVA A INGRESAR EL USUARIO")
        continue
    
    #Define el username o ID del usuario mediante una funcion y termina el ciclo
    username = test_tp5funciones.create_username(name_user, lastname_user, dni_user)
    break
print(f"Su ID de usuario es: {username}")


#Ejercicio 4
num1=int(input("Ingrese un número entero: "))
num2=int(input("Ingrese otro número entero: "))

if test_tp5funciones.is_multiple(num1,num2):
    print(f"{num1} es multiplo de {num2}")
else:
    print(f"{num1} no es multiplo de {num2}")


#Ejercicio 5
days=int(input("Ingrese la cantidad de días que quiere calcular: "))

for i in range(days):
    maxi_tem=float(input("Ingrese la temperatura máxima(en °C sin el símbolo\"°\"): "))
    mini_tem=float(input("Ingrese la temperatura minima(en °C sin el símbolo\"°\"): "))
    media=test_tp5funciones.media_calculator(maxi_tem,mini_tem)
    print(f"La temperatura media del día {i+1} fue de {media}°")


#Ejercicio 6
phrase=input("Ingrese una frase: ")

print(test_tp5funciones.enter_space(phrase))


#Ejercicio 7 - Numero mayor y menor ingresados
numbers_entered = []

while True:
    entered_num = int(input("Ingresar numero, para finalizar ingrese 0: "))
    if entered_num == 0:
        break
    else:
        numbers_entered.append(entered_num)
        continue

results= test_tp5funciones.number_mayor_minor(numbers_entered) 
number_major = results[0]
number_minor = results[1]

print(f"El mayor numero ingresado es {number_major} y el menor es {number_minor}")


#Ejericicio 8
radio=float(input("Ingrese el valor del radio de una circunferencia (en centimetros): "))
test_tp5funciones.area_per_calculator(radio)


#Ejericicio 9
attempt=3

while attempt>0:
    username=input("Ingrese su usuario: ")
    password=input("Ingrese la clave: ")

    if test_tp5funciones.login(username,password):
        print("¡BIENVENIDO!")
        break
    else:
        attempt-=1
        print(f"Inicio de sesión fallido. Intentos restantes: {attempt}")

if attempt==0:
    print("Has agotado tus intentos")


#Ejercicio 10
prices={2000:10, 4000:20, 6000:30}

print(f"El precio final de su carrito es de {test_tp5funciones.aply_discount(prices)}")


#Ejercicio 11
numbers=[2,6,10,43,84]

results=test_tp5funciones.aply_function(test_tp5funciones.multiply_by_two, numbers)

for i in range(len(numbers)):
    print(f"{numbers[i]} multiplicado por 2 es igual a {results[i]}")



#Ejercicio 12 - Diccionario de una frase ingresada

phrase_entered = str(input("Ingrese una frase y sus palabras seran agregadas al diccionario: "))

dictionary_phrase = test_tp5funciones.phrase_to_dictionary(phrase_entered)

print(dictionary_phrase)


#Ejercicio 13

vector = (3, 4, 5)

module = test_tp5funciones.calculate_module(vector)

print("El módulo del vector es:", module)


#Ejercicio 14
num=int(input("Ingrese un número: "))

if test_tp5funciones.is_prime(num)==True:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")

#Ejercicio 15
nums=[]
test_tp5funciones.list_filler(nums)

print("Factoriales de los números ingresados: ")
for num in nums:
    factorial=test_tp5funciones.factorial_calculator(num)
    print(f"El factorial de {num} es {factorial}")

print(f"Se leyeron {len(nums)} números en total")

#Ejercicio 16
num=int(input("Ingrese un número: "))
digit=int(input("Ingrese un digito: "))

print(f"El número {digit} se repite {test_tp5funciones.frequency(num, digit)} veces en {num}")

#Ejercicio 17
max_num=0

while True:
    num=int(input("Ingrese un número primo: "))
    if test_tp5funciones.is_prime(num):
        if num>max_num:
            max_num=num
        
        print(f"La suma de los dígitos de {num} es {test_tp5funciones.sum_of_digit(num)}")
        digit=int(input("Ingrese un dígito: "))
        print(f"El número {digit} se repite {test_tp5funciones.frequency(num, digit)} veces en {num}")
    else:
        break

factorial=test_tp5funciones.factorial_calculator(max_num)
print(f"El mayor número ingresado fue {max_num}")
print(f"El factorial de {max_num} es {factorial}")
