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

#Funciones ejercicio 7

def number_mayor_minor(list_numbers):
    num_minor= list_numbers[0]
    num_mayor=list_numbers[0]
    for i in range(len(list_numbers)):
        if list_numbers[i] > num_mayor:
            num_mayor = list_numbers[i]
        
        if list_numbers[i] < num_minor :
            num_minor = list_numbers[i]
    
    return num_mayor, num_minor

#Funciones ejercicio 12

def phrase_to_dictionary(phrase):
    list_phrase = []
    list_phrase = phrase.split()
    dictionary = {}

#for i in range(len(list_phrase)):






