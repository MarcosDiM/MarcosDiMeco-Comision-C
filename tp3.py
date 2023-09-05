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

'''

#5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
