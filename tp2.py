#TRABAJO PRACTICO N2

#1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.

anios_computadora = int(input("Ingresar cuantos años tine esta computadora: "))
if anios_computadora > 0 and anios_computadora <= 2 :
    print("El computador nuevo")
elif anios_computadora > 2:
    print("El computador es viejo")
else:
    print("Error: Numero ingresado no valido")

#2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.

#3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.

nombre1 = str(input("Ingresar un nombre: "))
nombre2 = str(input("Ingresar otro nombre: "))

nombre1 = nombre1.title()
nombre2 = nombre2.title()

if nombre1[0] == nombre2[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")

#4- Crear un programa que permita al usuario elegir un candidato por el cual votar
print("Para votar ingrese: A - Partido Rojo ; B - Partido Verde ; C - Partido Azul")
votacion = str(input("Ingresar votacion: "))
votacion = votacion.upper()

if votacion == "A":
    print("Usted ha votado por el color: Rojo")
elif votacion == "B":
    print("Usted ha votado por el color: Verde")
elif votacion == "C":
    print("Usted ha votado por el color: Azul")
else: 
    print("Opcion errónea")

# 5- Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.

letra = str(input("Ingresar una letra: "))

letra = letra.upper()
if len(letra) > 1: 
    print("No se puede procesar el dato.")
elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U": 
    print("Es vocal")
else: 
    print("No es vocal")

# 6- Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
a_bisiesto = int(input("Ingresar un año para saber si es bisiesto: "))

if a_bisiesto % 4 == 0 and a_bisiesto % 100 != 0 or a_bisiesto % 400 == 0 :
    print("Es año bisiesto")
else:
    print("El año no es bisiesto")

#7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.

n1 = int(input("Ingresar numero 1: "))
n2 = int(input("Ingresar numero 2: "))
n3 = int(input("Ingresar numero 3: "))
num_menor = n1

if num_menor > n2:
    num_menor = n2
elif num_menor > n3: 
    num_menor = n3

print("El numero menor ingresado es el numero: ", num_menor)

#8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.

usuario = str(input("Usuario: "))
contrasenia = str(input("Contraseña: "))

if usuario == "Gwenevere" and contrasenia == "excalibur": 
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else: 
    print("Acceso denegado")