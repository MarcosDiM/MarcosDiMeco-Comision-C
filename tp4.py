#Trabajo practico N°4

#Exercise 

x = 0 #Definicion de variable

#Se ingresa el parametro al ciclo y se aumenta la variable en 1 cada vez que vuelva a empezar
while x < 30: 
    x += 1 
    #Siempre que el valor de x sea 4, 6 u 8 la impresion del ciclo se omite
    if x == 4 or x == 6 or x == 10: 
        print(f"When the value of x is {x} it is skip")
    #Cuando el valor de la variable x sea 15 el ciclo se rompe
    elif x == 15: 
        print(f"The execution of the loop was broken when x was {x}")
        break
    #En caso que no se cumplan las condiciones anteriores el ciclo continua normal imprimiendo su valor
    else: 
        print(f"The value of the loop is {x}")

#Ejercicio 1 

#Se define el ingreso de la oracion y el arreglo que almacenara las oraciones
sentence = str(input("Ingresar oraciones para convertir a mayusculas, para finalizar ingrese una linea en blanco: "))
sentences_saved = []

#Se inicia el ciclo para convertir las oraciones en mayusculas y almacenarlas hasta que se ingrese un espacio vacio
while len(sentence) != 0: 
    sentence = sentence.upper()
    sentences_saved.append(sentence)
    sentence = str(input("Ingresar oraciones para convertir a mayusculas, para finalizar ingrese una linea en blanco: "))

#Se imprimen las oraciones e indica en caso de no haer ingresado ninguna
if len(sentences_saved) == 0: 
    print("No se ingreso ninguna oración")
else:
    for i in sentences_saved:
        print(i)

#Ejercicio 2

#Explicacion de funcionamiento del cajero y los fondos son definidos en una variable igualada a 0
print("Para ingresar dinero, ingrese la letra D seguida del monto, y en caso de retirar, use la letra R. Para salir, simplemente presione Enter sin escribir nada.")
funds = 0

#Inicia el ciclo y pide que se ingrese la operacion como se lo indico anteriormente
while True:
    command_casher = input("Ingresar operación: ").upper()

    #Se configura la salida del ciclo al no ingresar ningun comando
    if len(command_casher) == 0:
        break

    #Se configura que al no ingresar un comando valido resulte error
    if command_casher[0] != "D" and command_casher[0] != "R":
        print("Comando ingresado incorrecto")
    else:
        #Se define el monto mediante la variable movement y dependiendo el comando ingresado se suma o se resta a la variable funds
        try:
            movement = int(command_casher[1:])
            if command_casher[0] == "D":
                funds += movement
            elif command_casher[0] == "R":
                #En caso que se pida retirar un monto mayor retorna que hay fondos insuficientes
                if funds < movement:
                    print("Fondos insuficientes")
                else:
                    funds -= movement
        #En caso que se ingrese un comando incorrecto retorne error
        except ValueError:
            print("Error: El monto debe ser un número")

#Se imprimer los fondos al salir del ciclo
print(f"Los fondos son de: ${funds}")

#Ejercicio 3

#Define las variables para contar la cantidad de numeros primos y un array para almacenarlos
prime_number_counter = 0
storage_prime_number = []

#Incia el ciclo para pedir numeros enteros mayores que 1
while True: 
    number = int(input("Ingresar numero mayor que 1, para finalizar ingrese 0: "))
    #Se define la salida del ciclo al ingresar 0
    if number == 0:
        break
    #Al ingresar el numero 1 o menor responde que el numero no es valido
    elif number <= 1:
        print("Numero ingresado no valido")
        continue
    #Si es el numero 3 al ser primo se almacena y suma + 1 al contador de numeros primos 
    else:
        if number <= 3:
            es_primo = True
            storage_prime_number.append(number)
            prime_number_counter += 1
        #Si el numero ingresado es divisible por 2 o 3 no es primo y vuelve a empezar el ciclo
        elif number % 2 == 0 or number % 3 == 0:
            continue
        #Se define si el numero es primo y si lo es se almacena y suma uno al contador de primos
        else:
            i = 5
            while i * i <= number:
                if number % i == 0 or number % (i + 2) == 0:
                    break
                i += 6
            else:
                storage_prime_number.append(number)
                prime_number_counter += 1

#Respuesta de cuantos numeros primos se ingresaron y cuales fueron
print(f"Se ingresaron {prime_number_counter} numeros primos los cuales son: {storage_prime_number}")

#Ejercicio 4

#Define los años mediante lo que se vaya a ingresar por consola
age1 = input('Ingrese un primer año: ')
age2 = input('Ingrese el siguiente año: ')

#En el ciclo se recorren todos los años entre los ingresados y se imprimen los que sean bisiestos o decadas
for i in range(age1,age2+1):
    if i%4==0 and i%10==0 and not i%100==0:
        print(i)
    elif i%400==0:
        print(i)
    else:
        continue

#Ejercicio 5

for i in range(1,21):
    if i%2==0:
        print(i)
    else:
        continue

#Ejercicio 6

list_numbers=[1,2,4,6,8,10]
search_number=int(input("Ingrese un número para saber si se encuentra en la lista: "))

for i in list_numbers:
    if search_number==i:
        print(f"El número {search_number} si se encuentra en la lista")
        break
    else:
        continue

#Ejercicio 7 

print(f"Carta cafeteria: \n1- COMBO 1 : Cafe + Medialuna o tortita + Jugo de naranja  = $1200 \n2- COMBO 2 : Licuado de fruta a eleccion + Tostado de Jamon y Queso = $1000\n3- COMBO 3 : Cafe XXL + Porcion de torta a eleccion (Sujeto a stock) + Jugo de Naranja = $ 3000 \n0- Salir")
option=1
account=0
count=[]
while option!=0:
    option=int(input("Ingrese una opción: "))
    if option==0:
        break
    elif option==1:
        print("COMBO 1 : Cafe + Medialuna o tortita + Jugo de naranja  = $1200")
        account+=1200
        count.append(1)
    elif option==2:
        print("COMBO 2 : Licuado de fruta a eleccion + Tostado de Jamon y Queso = $1000")
        account+=1000
        count.append(2)
    elif option==3:
        print("COMBO 3 : Cafe XXL + Porcion de torta a eleccion (Sujeto a stock) + Jugo de Naranja = $ 3000")
        account+=1000
        count.append(3)
    else:
        print("¡ERROR! Ingrese una opción válida")
print(f"Ha elegido el COMBO: {count}\nLa cuenta total es de ${account}")
