#TP 5

#Funcion Ejercicio 1 - Verificar DNI

#Funcion la cual una vez ingresado el DNI si tiene 7 u 8 caracteres retorna TRUE, sino retorna FALSE
def verify_dni(number):
    if (len(number) == 7) or (len(number) == 8):
        return True
    else:
        return False

#Funcion Ejercicio 2 - Ultima palabra del string

#En la funcion ingresa la frase y con el comando .split() separo en partes todas las palabras y las guardo en la  lista trimen_phrase
def last_word(phrase):
    trimed_phrase = phrase.split()
    #Guardo la ultima palabra de la lista en la variable word y luego retorno la misma
    word = trimed_phrase[-1]
    return print("La ultima palabra de la frase es:", word)


#Funciones Ejercicio 3

#Funcion que ingresa un nombre completo y dni en una lista y lo divide a cada uno en una variable
def define_name(complete_name):
    if len(complete_name) == 4:
        name = complete_name[0].title()
        lastname = complete_name[2].title()
        dni = complete_name[3]
    elif len(complete_name) == 3:
        name = complete_name[0].title()
        lastname = complete_name[1].title()
        dni = complete_name[2]
    return name, lastname, dni

#Funcion que crea el ID del usuario ingresando nombre apellido y dni.
def create_username(name, lastname, dni):
    user_name = f"{name}{len(lastname)}{dni[0:3]}" 
    return user_name

#Ejercicio 4
def is_multiple(num1,num2):
    if num1%num2==0:
        return True
    else:
        return False

#Ejercicio 5
def media_calculator(maxi,mini):
    media=(maxi+mini)/2
    return media

#Ejercicio 6
def enter_space (phrase):
    new_phrase=""
    for letter in phrase:
        new_phrase+=letter + " "
    return new_phrase


#Funciones ejercicio 7

#Funcion que ingresa una lista de numeros y retorna el mayor y el menor
def number_mayor_minor(list_numbers):

    #Defino el numero mayor y menor como el de la posicion 0 de la lista
    num_minor= list_numbers[0]
    num_mayor=list_numbers[0]

    #Ingresa la lista a un ciclo para recorrer todos los numeros
    for i in range(len(list_numbers)):
        #Comenzando en base al primer numero de la lista define el mayor y menor de la lista 
        if list_numbers[i] > num_mayor:
            num_mayor = list_numbers[i]
        
        if list_numbers[i] < num_minor :
            num_minor = list_numbers[i]
    
    return num_mayor, num_minor


#Ejericico 8

import math
def area_per_calculator(radio):
    perimeter=radio*2
    area=math.pi*(radio)**2
    return(print(f"El perímetro de la circunferencia es de {perimeter}cm y el area es de {area}cm2"))


#Ejericicio 9

def login (username, password):
    
    if username=="usuario1" and password=="asdasd":
        return True
    else:
        return False


#Ejercicio 10

def aply_discount(prices):
    final_price=0
    shopping_cart=float(input("Ingrese el monto total de su carrito de compra: "))
    if shopping_cart<=0:
        print("¡ERROR! El valor ingresado no es válido")
        aply_discount(prices)
    else:    
        if shopping_cart>=2000 and shopping_cart<4000:
            discount=(shopping_cart*prices[2000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[2000]}%")

        elif shopping_cart>=4000 and shopping_cart<6000:
            discount=(shopping_cart*prices[4000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[4000]}%")

        elif shopping_cart>=6000:
            discount=(shopping_cart*prices[6000])/100
            final_price=shopping_cart-discount
            print(f"Por el monto de su carrito obtiene un descuento del {prices[6000]}%")

        else:
            final_price=shopping_cart
            print(f"Por el monto de su carrito no obtiene ningún descuento")

        return final_price



#Ejercicio 11

def aply_function(func, numbers):
    results=[]
    
    for num in numbers:
        results.append(func(num))
    
    return results
def multiply_by_two(num):
    
    return num*2


#Funciones ejercicio 12

#Funcion que ingresa una frase y transforma las palabras a un diccionario con el largo de la palabra
def phrase_to_dictionary(phrase):
    #Transforma la frase en una lista de las palabras
    list_phrase = []
    list_phrase = phrase.split()
    dictionary = {}
    #Agrega al diccionario cada palabra con su largo y luego retorna el diccionario
    for word in list_phrase:
        dictionary[word] = len(word)

    return dictionary


#Funciones ejercicio 13

import math

def calculate_module(vector):
    x, y, z = vector
    module = math.sqrt(x**2 + y**2 + z**2)
    return module


#Funciones ejercicio 14

def is_prime(num):
    counter=0
    for i in range(1,num+1):
        if num%i==0:
            counter+=1
    
    if counter==2:
        return True
    else:
        return False


#Funciones ejercicio 15

def list_filler(nums):
    num=1
    while num!=0:
        num=int(input("Ingrese un número, para dejar de ingresar números ingrese 0(cero): "))
        if num!=0:
            nums.append(num)
    return nums

def factorial_calculator(num):
    if num==0:
        return 1
    else:
        return num*factorial_calculator(num-1)


#Funciones ejercicio 16

def frequency(num, digit):
    num_str=str(num)
    digit_str=str(digit)
    counter=0

    for i in num_str:
        if i==digit_str:
            counter+=1
    return counter


#Funciones ejercicio 17

def sum_of_digit(num):
        digits_sum=0
        num_str=str(num)
        for i in num_str:
            digits_sum+=int(i)
        return digits_sum

