#Le pido al usuario que ingrese su nombre
name = str(input("Ingrese su nombre: ")).title()

#Pido que ingrese una opcion para ingresar a cada juego
options = int(input(f"Hola {name}, ingrese una opcion: \n 1 - Juego de numeros \n 2 - Juego de palabra: "))

#En caso de elegir la opcion 1 ingresa al juego de numeros
if options == 1: 

    print(f"{name}, has elegido el Juego de números.")

    #Igualo variables de contador a 0
    numbers_odd = 0
    major_number = 0
    counter = 0

    #Inicio el ciclo while para pedir numeros y hasta que ingrese 0
    while True:
        number = str(input("Ingrese un numero, para salir ingrese 0: "))
        
        if number == "":
            print("No se ha ingresado ningun numero.")
            continue
        
        number = float(number)
        if number == 0:
            break
        #En caso de ingresar un numero impar se suma a la variable de contador de impares y otro contador para la cantidad de impares
        if number % 2 != 0:
            numbers_odd += number
            counter += 1
        #Si el numero ingresado es par y mayor que el ultimo par ingresado se almacena en la variable
        elif number % 2 == 0 and number > major_number:
            major_number = number

#Imprime el resultado y en caso de ingresar impares calcula el promedio
    if numbers_odd == 0 and major_number == 0: 
        print("No se ha ingresado numeros pares ni impares")
    elif numbers_odd == 0 :
        print("No se han ingresado numeros impares")
        print(f"El mayor numero par ingresado es :{major_number}")
    elif major_number == 0: 
        average = float(numbers_odd / counter)
        print("No se ingresaron numeros pares")
        print(f"El promedio de numeros impares es: {average}")
    else: 
        average = float(numbers_odd / counter)
        print(f"El mayor numero par ingresado es :{major_number}")
        print(f"El promedio de numeros impares es: {average}")


#En caso de seleccionar la opcion 2 ingresa al juego de palabras
elif options == 2:
    #Defino el ingreso de la frase
    print(f"{name}, has elegido el Juego de palabras.")
    phrase = str(input("Ingrese una frase: ")).lower()

    #Ingreso variables de contadores para cada vocal
    vowel_a = phrase.count("a")
    vowel_e = phrase.count("e")
    vowel_i = phrase.count("i")
    vowel_o = phrase.count("o")
    vowel_u = phrase.count("u")

    #Muestro resultado de cantidad de vocales
    print(f"{name}, La cantidad de vocales a = {vowel_a} \n La cantidad de vocales e = {vowel_e} \n La cantidad de vocales i = {vowel_i} \n La cantidad de vocales o = {vowel_o} \n La cantidad de vocales u = {vowel_u}")

else:
    print("La opcion ingresada no es correcta")
