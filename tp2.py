#TRABAJO PRACTICO N2
'''
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

#9- Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nom_alumno = str(input("Ingresar nombre: "))
sexo = input("Ingresar sexo (F/M): ").upper()

letra_alumno = nom_alumno[0].title()
letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
num_letra = letras.index(letra_alumno)

if sexo == "F" and num_letra < 12 or sexo == "M" and num_letra > 13:
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")

#10- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar

edad_cliente = int(input("Ingresar edad: "))
if edad_cliente < 0:
    print("Edad ingresada no valida")
elif edad_cliente < 4:
    print("La entrada es gratuita.")
elif edad_cliente < 18:
    print("Valor entrada: $500")
else: 
    print("Valor entrada: $1000")


#11- Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija

si_no = str(input("Desea una pizza vegetariana? ")).lower()

vegetariana = ["Pimiento", "Tofu"]
no_vegetariana = ["Peperoni", "Jamon", "Salmon"]

if si_no == "si":
    print("Ingredientes disponibles: ", vegetariana)
    ingrediente = int(input("Ingresar el ingrediente deseado (1 o 2): "))
    print(f"La pizza elegida es vegetariana y contiene: Queso, Tomate y {vegetariana[ingrediente -1]}")

elif si_no == "no":
    print("Ingredientes disponibles: ", no_vegetariana)
    ingrediente = int(input("Ingresar el ingrediente deseado (1, 2 o 3): "))
    print(f"La pizza elegida no es vegetariana y contiene: Queso, Tomate y {no_vegetariana[ingrediente -1]}")


#12- Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.
anios = str(input("Ingresar el año actual y otro aleatorio separados por un espacio: "))
anio_actual = int(anios[0 : anios.find(" ")])
anio_selec = int(anios[anios.find(" ")+1 : len(anios)])

if anio_actual > anio_selec: 
    distancia = anio_actual - anio_selec
    print(f"Han pasado {distancia} dede el {anio_selec}")
elif anio_actual < anio_selec:
    distancia = anio_selec - anio_actual
    print(f"Faltan {distancia} años para el {anio_selec}")


#13-Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.

numeros_ingresados = str(input("Ingreasar dos numeros separados por un guion (-): "))
numero1= int(numeros_ingresados[0 : numeros_ingresados.find("-")])
numero2= int(numeros_ingresados[numeros_ingresados.find("-")+1: len(numeros_ingresados)])

if numero1 <= 0 or numero2 <= 0: 
    print("No se puede realizar con 0 o numeros negativos")
elif numero1 > numero2:
    if (numero1 % numero2) == 0 :
        print(f"El numero {numero1} es multiplo del numero {numero2}")
    else:
        print(f"El numero {numero1} no es multiplo del numero {numero2}")
elif numero2 > numero1:
    if (numero2 % numero1) == 0: 
        print(f"El numero {numero2} es multiplo del numero {numero1}")
    else:
        print(f"El numero {numero2} no es multiplo del numero {numero1}")
elif numero1 == numero2: 
    print("Los numeros ingresados son los mismos")

'''
#14- Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.

print("Ecuacion: (a x + b = 0)")
a=int("Ingresa el valor de a: ")
b=int("Ingresa el valor de b: ")

if a == 0:
    if b == 0:
        print("La ecuacion tiene infinitas soluciones (todos los numeros son solucion.)")
    else:
        print("La ecuacion no tiene solucion.")
else: 
    x = -b / a
    print(f"La solucion de la ecuacion {a}x +{b} = 0 es x = {x}.")

#15- Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo

t_o_r = str(input("Que area quiere calcular? t = triangulo c = circulo: ")).lower()

import math
pi = math.pi

if t_o_r =="t": 
    base_t = float(input("Ingresar base del triangulo (en centimetros): "))
    altura_t = float(input("Ingresar altura del triangulo (en centimetros): "))
    area = (base_t * altura_t)
    print(f"El area del triangulo es de {area}cm²")
elif t_o_r =="c":
    radio_c = int(input("Ingresar el radio del circulo (en centimetros): "))
    area = pi(radio_c ** 2)
    print(f"El area del circulo es de {area}cm²")
else: 
    print("VALOR INGRESADO NO VALIDO")