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

#16-	Haz una calculadora básica pida al usuario dos valores, a y b. Según la opción que desean, realizar la operación

num1 = int(input("Ingresar un numero: "))
num2 = int(input("Ingresar otro numero: "))
operacion = int(input("Ingresar que operacion desea realizar (1/2/3/4): "))

if operacion == 1: 
    res_operacion = num1 + num2
    print("El resultado de la operacion es:", res_operacion)
elif operacion == 2: 
    res_operacion = num1 - num2
    print("El resultado de la operacion es:", res_operacion)
elif operacion == 3:
    res_operacion = num1 * num2
    print("El resultado de la operacion es:", res_operacion)
elif operacion == 4: 
    res_operacion = num1 / num2
    print("El resultado de la operacion es:", res_operacion)
else: 
    print("Operacion ingresada no valida")

#17- Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
dia_semana = str(input("Ingresar un dia de la semana: ")).lower()

if dia_semana == "lunes":
    print("Esta comenzando la semana")
elif dia_semana == "viernes":
    print("Hoy empieza el fin de semana")
elif dia_semana == "sabado" or dia_semana == "domingo":
    print("Es fin de semana")
else:
    print("Es mitad de semana")

#18- Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.

horas_trabajadas = int(input("Ingresar el horas trabajadas: "))
salario = int(input("Ingresar salario por hora: "))
salario_extra = (horas_trabajadas % 48)*salario*0.1


if horas_trabajadas <= 48: 
    salario_total = salario * horas_trabajadas
elif horas_trabajadas > 48:
    salario_total = (salario * horas_trabajadas) + salario_extra

print("El salario total es de: ", salario_total)

#19- Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.

cant_lapices = int(input("Ingresar cuantos lapices quiere comprar: "))

precio_lapiz = 60

if cant_lapices >= 1000 : 
    precio_total = (precio_lapiz * cant_lapices) * 0.93
else: 
    precio_total = precio_lapiz * cant_lapices

print(f"El precio por {cant_lapices} es de: {precio_total}")

#20- Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.

nota1 = int(input("Ingresar nota 1: "))
nota2 = int(input("Ingresar nota 2: "))
nota3 = int(input("Ingresar nota 3: "))
nota4 = int(input("Ingresar nota 4: "))

prom = (nota1 + nota2 + nota3 + nota4) /4

if prom >= 6 :
    print("Aprobado: ",prom)
else:
    print("Desaprobado: ",prom)