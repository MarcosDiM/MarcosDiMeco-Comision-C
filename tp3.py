'''
# 1- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Ingrese una palabra: ")

for i in range(10):
    print(palabra)

# 2- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Ingrese su edad: "))

for i in range(edad): 
    print(i + 1)


# 3- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Ingrese un numero entero positivo: "))

for i in range(numero +1):
    if i % 2 != 0:
        if i == numero:
            print(i)
            continue
        print(i,end=",")



# 4- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num_cuenta_regresiva = int(input("Ingresar un numero: "))
num_print = num_cuenta_regresiva
for i in range(num_cuenta_regresiva):
    if num_print == 1:
        print( num_print)
        continue 
    print(num_print, end=",")
    num_print -= 1



#5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

inversion = int(input("Ingrese el monto a invertir: "))
interes = int(input("Ingresar el porcentaje de interes anual: "))
cantidad_anios = int(input("Cuantos años durara la inversion: "))

for i in range(cantidad_anios):
    inversion += (inversion / 100) * interes
    print(f"El año {i+1} la inversion sera de {inversion}")



#6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo con de altura el número introducido.

str_triangulo = str(input("Ingrese la altura de un  triangulo: "))
int_triangulo = int(str_triangulo)
altura_triangulo = str_triangulo

for i in range(int_triangulo):
    print (altura_triangulo)
    altura_triangulo += str_triangulo


#7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.}

for i in range(10):
    print(f"TABLA DEL {i+1}")
    for y in range(10):
        resultado = (i+1) * (y+1)
        print(f"{i+1} * {y+1} = {resultado} ")
'''

#8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
altura = int(input("Ingrese la altura del triangulo: "))
num_base= 1
for i in range(altura): 
    num_vuelta = num_base
    print("")
    for j in range(i+1):
        
        print(num_vuelta, end=" ")
        num_vuelta += 2