#Funciones BINGO 

def complete_table_bingo(bingo_table):
    print("Ingresar 25 numeros entre 1 y 75 para completar el carton de bingo:")
    counter = 0
    numbers_bingo = []
    
    

    while counter < 26:
        number= int(input("N: "))
        if number < 1 or number > 75:
            print("Numero ingresado fuera de rango, ingrese otro")
            continue
        elif number in numbers_bingo:
            print("Este numero ya fue ingresado, ingrese otro.")
            continue
        else:
            numbers_bingo.append(number)
            counter += 1
    
    for i in range(5):
        for j in range(5):
            bingo_table[i][j] = numbers_bingo.pop()
    
    return bingo_table
    