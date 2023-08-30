# FOR

letras = letra = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

lugares = int(input("Ingresa cauntos lugares se correran las letras: "))
for i in range(5):
    frase = input(f"Ingrese el mensaje {i+1}: ").lower() 
    mensaje_encriptado=""
    for letra in frase:
        posicion = letras.index(letra)
        nueva_letra = (lugares + posicion)%27
        mensaje_encriptado = mensaje_encriptado + letras[nueva_letra]
    print(mensaje_encriptado)

#WHILE

numero = input("Ingresar un numero ")
numero_string = str(numero)
numero = int(numero_string)

total_pares = 0
total_impares = 0


while numero != 0 : 
    pares = 0
    impares = 0
    if numero < 0 :
        print("Numero no valido")
    elif len (numero_string) > 1:
        for i in numero_string:
            if int(i) % 2 == 0:
                pares += 1
                total_pares += 1
            else:
                impares += 1
                total_impares += 1
    else:
        if numero % 2 == 0:
            pares += 1 
            total_pares += 1
        else:
            impares = impares +1
            total_impares =+ 1
    print(f"La cantidad de numeros pares del numero {numero} es de {pares} y de impares es de {impares}")
    numero = input("Ingresar un numero ")
    numero_string = str(numero)
    numero = int(numero_string)
print(f"El numero total de digitos pares es de {total_pares} y de impares es de {total_impares}")





