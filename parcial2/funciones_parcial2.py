#FUNCIONES PARCIAL 2

def complete_matrix_adn(matrix_dna):
    rows = 0
    print("Ingresar 6 lineas de 6 elementos de ADN (A/T/C/G)")
    #Incio un ciclo while para el ingreso de las lineas de adn
    while True:   
        #Pide ingreso de linea de adn de 6 caracteres
        dna = str(input(f"Ingresar linea {rows+1}: ")).upper()
        #Condicion para verificar que no se ingrese un espacio vacio
        if dna == "":
            print("Valor ingresado no valido")
            continue
        #Condicion para verificar que la linea ingresada sea de 6 digitos
        if len(dna) != 6:
            print("Linea de ADN no valido, vuelva a ingresar la linea.")
            continue
        else:
            # Ingresa a un ciclo para verificar que los elementos del string sean elementos de adn 
            valid_dna = True
            for i in range(6):
            
                if dna[i] not in "ATCG":
                #En caso que la letra no sea un elemento la variable retorna falsa y sale del ciclo
                    print("Valores de ADN ingresados no validos, vuelva a ingresar la linea.")
                    valid_dna = False
                    break
        #Mientras la variable sea verdadera continua con el ciclo y agrega la linea a la primer fila de la matriz
        if valid_dna == True:
            matrix_dna[rows] = dna
            rows += 1   
        # En caso que se completen las 6 filas el ciclo termina con la matriz completa, de lo contrario continua volviendo a comenzar el ciclo
        if rows == 6:
            break
    return matrix_dna

def is_mutant(dna):
    #Defino variable para contar la cantidad de veces que hay lineas de 4 elementos de adn iguales consecutivos
    counter_dna = 0
    #Defino arreglos para agregar los puntos de las lineas de adn consecutivas
    horizontal_position = []
    vertical_position = []
    diagonal_position = []
    diagonal_inv_position = []

    #Incio dos ciclos para recorrer la matriz de tamaño 6x6
    for i in range(6):
        for j in range(6):
            #Condicion que ingrese en caso que el elemento selecconado de la matriz tenga 3 elementos iguales consecutivos en forma HORIZONTAL y no este fuera de rango
            if (j + 3 < 6) and dna[i][j] == dna[i][j+1] == dna[i][j+2] == dna[i][j+3] and (i , j) not in horizontal_position:
                    #En caso que se cumpla la condicion suma 1 al contador de lineas de adn y guarda los puntos en el arreglo correspondiente 
                    counter_dna += 1
                    horizontal_position.append((i , j))
                    horizontal_position.append((i , j+1))
                    horizontal_position.append((i , j+2))
                    horizontal_position.append((i , j+3))
            #Condicion que ingrese en caso que el elemento selecconado de la matriz tenga 3 elementos iguales consecutivos en forma VERTICAL y no este fuera de rango
            if (i + 3 < 6) and dna[i][j] == dna[i+1][j] == dna[i+2][j] == dna[i+3][j] and (i , j) not in vertical_position:
                #En caso que se cumpla la condicion suma 1 al contador de lineas de adn y guarda los puntos en el arreglo correspondiente 
                counter_dna += 1
                vertical_position.append((i , j))
                vertical_position.append((i+1 , j))
                vertical_position.append((i+2 , j))
                vertical_position.append((i+3 , j))
            #Condicion que ingrese en caso que el elemento selecconado de la matriz tenga 3 elementos iguales consecutivos en forma DIAGONAL y no este fuera de rango
            if (i + 3 < 6) and (j + 3 < 6) and dna[i][j] == dna[i+1][j+1] and (i , j) not in diagonal_position:
                if dna[i][j] == dna[i+1][j+1] == dna[i+2][j+2] == dna[i+3][j+3]:
                    #En caso que se cumpla la condicion suma 1 al contador de lineas de adn y guarda los puntos en el arreglo correspondiente 
                    counter_dna += 1
                    diagonal_position.append((i , j))
                    diagonal_position.append((i+1 , j+1))
                    diagonal_position.append((i+2 , j+2))
                    diagonal_position.append((i+3 , j+3))
            #Condicion que ingrese en caso que el elemento selecconado de la matriz tenga 3 elementos iguales consecutivos en forma DIAGONAL INVERSA A LA ANTERIOR y no este fuera de rango
            if (i + 3 < 6) and (j - 3 > 0) and dna[i][j] == dna[i+1][j-1] and (i , j) not in diagonal_inv_position:
                if dna[i][j] == dna[i+1][j-1] == dna[i+2][j-2] == dna[i+3][j-3]:
                    #En caso que se cumpla la condicion suma 1 al contador de lineas de adn y guarda los puntos en el arreglo correspondiente 
                    counter_dna += 1
                    diagonal_inv_position.append(i , j)
                    diagonal_inv_position.append(i+1 , j-1)
                    diagonal_inv_position.append(i+2 , j-2)
                    diagonal_inv_position.append(i+3 , j-3)
    #Condicion que corrobora si hay mas de dos lineas de elementos consecutivos, y retorna valor Verdadero de la funcion
    if counter_dna > 1:
        return True
    #En caso que no haya mas de una linea que cumpla los requisitos la funcion retorna valor Falso
    else:
        return False

