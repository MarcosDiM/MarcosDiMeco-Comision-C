def complete_matrix_adn(matrix_dna):
    rows = 0
    
    print("Ingresar 6 lineas de 6 elementos de ADN (A/T/C/G)")
    #Incio un ciclo while para el ingreso de las lineas de adn
    while True:   
        try:
            dna = str(input(f"Ingresar linea {rows+1}: ")).upper()
        except ValueError:
            print("Valor ingresado no valido")
            continue

        # Condicion para verificar que la linea ingresada sea de 6 digitos
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
            print(matrix_dna)
        # En caso que se completen las 6 filas el ciclo termina con la matriz completa, de lo contrario continua volviendo a comenzar el ciclo
        if rows == 6:
            break
    return matrix_dna

def is_mutant(dna):
    for i in range(6):
        print("\n")
        for j in range(6):
            print(dna[i][j],end="")
    counter_dna = 0
    positions = []
    for i in range(6):
        for j in range(6):
            if (j + 3 < 7) and dna[i][j] == dna[i][j+1]:
                if dna[i][j] == dna[i][j+2] and dna[i][j] == dna[i][j+3] and dna[i][j] == dna[i][j+4]:
                    counter_dna += 1
            if (i + 3 < 7) and dna[i][j] == dna[i+1][j]: 
                if dna[i][j] == dna[i+2][j] and dna[i][j] == dna[i+3][j] and dna[i][j] == dna[i+4][j]:
                    counter_dna += 1
            if (i + 3 < 7) and (j + 3 < 7) and dna[i][j] == dna[i+1][j+1]:
                if dna[i][j] == dna[i+2][j+2] and dna[i][j] == dna[i+3][j+3] and dna[i][j] == dna[i+4][j+4]:
                    counter_dna += 1

    print("Contador: ", counter_dna)
    if counter_dna > 1:
        return True
    else:
        return False