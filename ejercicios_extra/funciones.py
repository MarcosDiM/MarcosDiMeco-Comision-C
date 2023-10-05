#FUNCIONES

def most(a,b):
    if a>b:
        return a
    else:
        return b

def least(a,b):
    if a<b:
        return a
    else:
        return b


def hanged(word):

    #Defino las variables, word para la palabra a adivinar, lives para las limitar los errores de letra, y la lista para la palabra que esta adivinando
    word = word.upper()
    lives = 6
    long_word = len(word)
    list_word = []
    
    #Relleno la lista con espacios vacios del largo de la palabra a adivinar
    for i in range(long_word):
        list_word.append("_")

    #Inicio el ciclo para comenzar a jugar
    while True:
        
        #Creo una variable para convertir la lista a palabra y luego compararla con la palabra a adivinar
        word_guess = "".join(list_word)
        
        #Defino el final del ciclo en caso que haya ganado o perdido
        if word_guess == word:
            return print(f"Has ganado, la palabra era: {word}")
            break
        elif lives == 0:
            return print("Has perdido todas las vidas.")
            break
        
        #Imprimo la cantidad de vidas restantes y la lista con las letras que ha adivinado
        print(f"Usted tiene {lives} vidas")
        print(list_word)

        #Pido ingresar una letra 
        letter = str(input("Ingrese una letra: ")).upper()

        #Corrijo en caso que ingrese mas de una letra
        if len(letter) > 1:
            print("ERROR, Debe ingresar una sola letra")
            continue
        
        #Proceso la letra ingresada
        if letter in word: #En caso que la letra ingresada este en la palabra lo avisa y la pone en la lista en la posicion de que debe ir 
            print(f"La palabra contiene la letra {letter}")
            for y in range(long_word):
                if word[y] == letter:
                    list_word[y] = letter
            continue
        else: #En caso que la letra no este en la palabra resta una vida y vuelve a comenzar el ciclo
            print(f"La palabra no contiene la letra {letter}")
            lives -= 1
            continue
    

