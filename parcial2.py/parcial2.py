#PARCIAL 2
import funciones_parcial2

#Defino la matriz en tamaño 6*6 llena de ceros 
matrix_dna = [[0 for _ in range(6)] for _ in range(6)]
rows = 0

#Llamo la funcion para rellenar la matriz de adn
matrix_dna = funciones_parcial2.complete_matrix_adn(matrix_dna)

# Imprision de la matriz de ADN
for i in range(rows):
    print(matrix_dna[i],"\n")
