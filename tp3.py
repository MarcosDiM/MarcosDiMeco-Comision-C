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


#8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

altura = int(input("Ingrese la altura del triangulo: "))
num_base= 1
for i in range(altura): 
    num_vuelta = num_base
    print("")
    for j in range(i+1):
        
        print(num_vuelta, end=" ")
        num_vuelta += 2

#9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

nueva_contra = str(input("Crear una nueva contraseña: "))
confir_contra = str(input("Ingresar contraseña: "))

while confir_contra != nueva_contra: 
    print("Contraseña incorrecta")
    confir_contra = str(input("Ingresar contraseña: "))

print("Contraseña correcta!")

#10- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

num_primo = int(input("Ingrese un numero para saber si es primo: "))
contador  = 0
for i in range(2, num_primo):
    if num_primo % i == 0:
        contador += 1

if contador >= 1: 
    print("El numero ingresado no es primo")
else:
    print("El numero es primo")

#11- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

word=str(input("Ingrese una palabra: "))
long=len(word)

for i in range(long-1, -1, -1):
    letter=word[i]
    print(letter)

#12- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
phrase=str(input("Ingrese una frase: "))
letter=str(input("Ingrese una letra: "))
phrase=phrase.upper()
letter=letter.upper()

counter=0

for character in phrase:
    if character==letter:
        counter=counter+1
print(f"La letra \"{letter}\" se repite {counter} veces en la frase ingresada")

#13- Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

eco="eco"
while eco!="salir":
    eco=str(input("Escriba algo: "))
    print(eco)
    eco=eco.lower()

#14- Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

num1=int(input("Ingrese un número: "))    
num2=int(input("Ingrese otro número: "))

if num1<num2:
    for i in range(num1,num2+1):
        if i%2==0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")
else:
    for i in range(num2,num1+1):
        if i%2==0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")

#15- Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

num=int(input("Ingrese un número entero positivo: "))

for i in range(num):
    if num%(i+1)==0:
        print(f"{i+1} es divisor de {num}")

#16- Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

amount_num=int(input("¿Cuantos número va a ingresar?: "))

counter=0

if amount_num<0:
    print("¡ERROR! Ingrese una cantidad válida")
else:
    for i in range(amount_num):
        num=float(input("Ingrese un número: "))
        if num<0:
            counter=counter+1
print(f"Se ingresaron {counter} números negativos")

#17- Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

phrase=str(input("Escriba una frase: "))
phrase=phrase.upper()
vowels=[]

for letter in phrase:
    if letter in "AEIOU" and letter not in vowels:
        vowels.append(letter)

print(f"Las vocales en la frase son: {vowels}")

#18- Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci

fibo=[0,1]

for i in range(2,10):
    next_num=fibo[i-1]+fibo[i-2]
    fibo.append(next_num)

for num in fibo:
    print(num)

#19- Escriba un programa que simule una alcancía. 

amount=float(input("Ingrese la cantidad que desea ahorrar: $"))

if amount<0:
    print("¡ERROR! Ingrese una cantidad válida (positiva)")
else:
    saving=0

    while saving<amount:
        new_saving=float(input("Ingrese el monto que desea ingresar: $"))

        if new_saving<0:
            print("¡ERROR! Ingese una cantidad válida (positiva)")
        else:
            saving+=new_saving
            remaining=amount-saving
            print(f"Usted ha ahorrado ${saving}, le fantan {remaining} para alcanzar su objetivo de {amount}")
    
    if saving==amount:
        print(f"Usted ha alcanzado su objetivo de ahorrar ${amount}")
    else:
        additional=saving-amount
        print(f"Usted ha alcanzado su objetivo de ahorrar ${amount} y ha obtenido un adicional de {additional}")

#20- Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

num=1
addition=0
while num!=0:
    num=int(input("Ingrese un número entero positivo: "))
    if num<0:
        print("¡ERROR! Ingrese solo números enteros positivos")
    else:
        addition=addition+num
print(f"La suma de todos los números válidos ingresados es {addition}")

#21- Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

num=1
highest=0

while num!=0:
    num=int(input("Ingrese un número entero positivo: "))
    if num<0:
        print("¡ERROR! Ingrese solo números enteros positivos")
    else:
        if num>highest:
            highest=num
print(f"El mayor número ingresado fue {highest}")

#22- Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen

num=0
even_number=0

while num!=-1:
    num=int(input("Ingrese un número entero positivo (o -1 para salir): "))

    if num==-1:
        break
    elif num<0:
        print("¡ERROR! Ingrese un número válido (positivo)")
    else:
        num_str=str(num)
        addition=0

        for digit_str in num_str:
            digit=int(digit_str)
            addition+=digit
        
        print(f"La suma de los dígitos de {num} es {addition}")

        if num%2==0:
            even_number+=1

print(f"Total de números pares ingresados: {even_number}")

#Ejercicio 23 y 24

product=1
total=0

while product!=0:
    product=float(input("Ingrese el valor del productor: "))
    if product<0:
        print("¡ERROR! Ingrese solo montos válidos")
    else:
        total=total+product

if total>1000:
    discount=total*0.1
    final_price=total-discount
    print(f"El total de su compra es de ${total}")
    print(f"Se le aplicó un descuento del 10%, así que el precio final es de {final_price}")
else:
    print(f"El total de su compra es de ${total}")

#25- Dado un número entero positivo, mostrar su factorial. 

num=int(input("Ingrese un número entero positivo: "))

if num<0:
    print("¡ERROR! El número debe ser positivo")
elif num==0:
    print("El factorial de 0 es 1")
else:
    factorial=1

    for i in range(1, num+1):
        factorial*=i
    
    print(f"El factorial de {num} es {factorial}")