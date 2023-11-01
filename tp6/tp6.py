import funciones_tp6

'''
#Ejercicios 1

print("Ingresar numeros para agregar a la lista, para salir ingrese 0 ")
numbers_list= []

while True:
    number_entered= int(input("N : "))
    if number_entered == 0:
        break
    else:
        numbers_list.append(number_entered)


print(f"Los numeros ingresados fueron: {numbers_list}")

#Ejercicio 2

funciones_tp6.delete_number_list(numbers_list)
print(f"La lista es: {numbers_list}")

#Ejercicio 3

summation_of_list = funciones_tp6.summation_list(numbers_list)
print(f"La suma de los numeros de la lista es: {summation_of_list}")

#Ejercicio 4

limit_number = int(input("Ingresar un numero para sacar todos los numeros de la lista menores a el: "))
limit_list = []
for i in range(len(numbers_list)):
    if numbers_list[i] < limit_number:
        limit_list.append(numbers_list[i])

if len(limit_list) == 0: 
    print(f"En la lista no hay numeros menores a {limit_number}")
else:
    print(f"La lista de numeros menores a {limit_number} quedaria: {limit_list}")

#Ejercicio 5

print("Ingresar numeros para agregar a la lista, para salir ingrese 0 ")
list_numbers = []

while True:
    entered_number= int(input("N : "))
    if entered_number == 0:
        break
    else:
        list_numbers.append(entered_number)

list_len_numbers = funciones_tp6.len_number_tuple(list_numbers)

print(f"El resultado de la lista e: {list_len_numbers}")

#Ejercicio 6

primary_students = []
secundary_students = []

print("Ingrese los nombres de pila de los alumnos del nivel primario, para finalizar ingrese 'x': ")
while True: 
    student = str(input("A: ")).title()
    if student == "X":
        break
    else:
        primary_students.append(student)

print("Ingrese los nombres de pila de los alumnos del nivel secundario, para finalizar ingrese 'x': ")
while True: 
    student = str(input("A: ")).title()
    if student == "X":
        break
    else:
        secundary_students.append(student)

primary_students = funciones_tp6.list_without_repeat(primary_students)

secundary_students = funciones_tp6.list_without_repeat(secundary_students)

#print(f"Los nombres de los alumnos de nivel primario sin repetir son: \n {primary_students}")
#print(f"Los nombres de los alumnos de nivel secundario sin repetir son: \n {secundary_students}")

students_repeat = funciones_tp6.repeat_into_lists(primary_students, secundary_students)

print(f"Los nombres repetidos entre primaria y secundara son: \n {students_repeat}")

students_not_repeat_in_lists = funciones_tp6.not_repeat_into_lists(primary_students, secundary_students)

print(f"Los nombres de primaria que no estan repetidos en secundaria son: \n {students_not_repeat_in_lists}")

#Ejercicio 7

counter=0
string_list=[]
frequency={}

while counter<=5:
    string=input("Ingrese una letra, palabra o cadena de texto: ")
    string_list.append(string)
    counter+=1
    
for element in string_list:
    for i in element:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1

for i, frequency in frequency.items():
    print(f"\"{i}\":{frequency}")


#Ejercicio 8

fixture=[]

for _ in range(10):
    team=[]
    for _ in range(10):
        team.append(0)
    fixture.append(team)

for i in range(10):
    for j in range(10):
        while True:
            try:
                goals=int(input(f"Ingrese la cantidad de goles que metió el Equipo {i+1} al Equipo {j+1} :"))
                fixture[i][j]=goals
                break
            except ValueError:
                print("¡ERROR! Ingrese un número válido")

triumphs=[0]*10
ties=[0]*10
defeats=[0]*10
goals_scored=[0]*10
goals_received=[0]*10

for i in range(10):
    for j in range(10):
        if i!=j:
            if fixture[i][j]>fixture[j][i]:
                triumphs[i]+=1
            elif fixture[i][j]<fixture[j][i]:
                defeats[i]+=1
            else:
                ties[i]+=1
            goals_scored[i]+=fixture[i][j]
            goals_received[i]+=fixture[j][i]

for i in range(10):
    print(f"Equipo {i+1}: ")
    print(f"Triunfos: {triumphs[i]}, Empates: {ties[i]}, Derrotas{defeats[i]}")
    print(f"Diferencia de goles: {goals_scored[i]} - {goals_received[i]}")
    print("---------")

'''

#Ejercicio 9
import random
matrix_memorytest = [[0]*4 for _ in range(4)]

matrix_hidden = [["X"]*4 for _ in range(4)]

#matrix_memorytest = funciones_tp6.complete_matrix(matrix_memorytest)

numbers_matrix = list(range(1,9))*2
random.shuffle(numbers_matrix)
for i in range(4):
    for j in range(4):
        matrix_memorytest[i][j] = numbers_matrix.pop()

for i in range(4):
        print("")
        for j in range(4):
            print("[",matrix_memorytest[i][j],"]",end="")

print("\n")
print("MEMOTEST : Comienza el juego!")

while True:
    for i in range(4):
        print("")
        for j in range(4):
            print("[",matrix_hidden[i][j],"]",end="")
    

    print("\n")
    print("Ingrese los numeros que quieres descubrir (fila/columna):")
    position1 = str(input("Posicion 1 (fila/columna): "))
    
    row1= int(position1[0]) -1
    column1= int(position1[2]) -1

    position2 = str(input("Posicion 2 (fila/columna): "))
    row2= int(position2[0]) -1
    column2= int(position2[2])-1

    if (len(position1) > 3) or (len(position2) > 3):
        print("Valores ingresados no validos")
        continue
    elif (row1 > 4) or (row2 > 4) or (column1 > 4) or (column2 > 4):
        print("Valores ingresados no validos")
        continue
    
    print(f"Los valores ingresados son {matrix_memorytest[row1][column1]} y {matrix_memorytest[row2][column2]}")

    if (matrix_memorytest[row1][column1]) == (matrix_memorytest[row2][column2]):
        print("Bien! Los numeros son los mismos")
        matrix_hidden[row1][column1] = matrix_memorytest[row1][column1]
        matrix_hidden[row2][column2] = matrix_memorytest[row2][column2]
        continue
    elif (matrix_memorytest[row1][column1]) != (matrix_memorytest[row2][column2]):
        print("Los valores no son iguales, vuelve a intentar!")
        continue

    if matrix_memorytest == matrix_hidden:
        print("Felicitaciones! Completaste el memotest y has ganado.")
        break


#Ejercicio 10
my_matriz=[]

for _ in range(3):
    rows=[]
    for _ in range(3):
        rows.append(0)
    my_matriz.append(rows)

for i in range(3):
    for j in range(3):
        while True:
            try:
                nums=float(input(f"Ingrese un número: "))
                my_matriz[i][j]=nums
                break
            except ValueError:
                print("¡ERROR! Ingrese un número válido")

print(f"DIAGONAL PRINCIPAL\n{my_matriz[0][0]}\n   {my_matriz[1][1]}\n      {my_matriz[2][2]}")
print(f"DIAGONAL INVERSA\n      {my_matriz[2][2]}\n   {my_matriz[1][1]}\n{my_matriz[0][0]}")

#Ejercicio 11
foreign_exchange={"Euro":"€", "Dollar":"$", "Yen":"¥"}

user=input("¿El simbolo de que divisa desea conocer?: ").capitalize()
if user=="Dolar":
    user="Dollar"
    print("Quizas usted quizo escribir \"Dollar\"")

if user in foreign_exchange:
    print(f"El simbolo de {user} es {foreign_exchange[user]}")
else:
    print("La divisa que solicita no está en el diccionario")

#Ejercicio 12
name = input("Enter your name.\n-->  ")
while True:
    age = int(input("Enter your age.\n-->  "))
    if age < 0 or age>100:
        print("Error, the age is wrong,try again.")
    else:
        break
address = input("Enter your address.\n-->  ")
cell_phone = int(input("Enter your cell phone number.\n-->  "))

profile = {'name':name,'age':age,'address':address,'cell_phone':cell_phone }
print(f"{profile['name']} tiene {profile['age']} años, vive en {profile['address']} y su número de teléfono es {profile['cell_phone']}.")

#Ejercicio 13
fruits={}

while True:
    choice=input("Para agregar un valor oprima 1, para salir oprima cualquier tecla: ")
    
    if choice=="1":
        fruit=input("Agregue el nombre de una fruta: ").capitalize()
        while True:
            try:
                value=float(input("Ingrese el valor por kilogramo de esa fruta: $"))
                fruits[fruit]=value
                break

            except ValueError:
                print("¡ERROR! Ingrese un número válido")
    else:
        break

user=input("¿Que fruta quiere llevar?: ").capitalize()

while True:
    try:
        kg=float(input("¿Cuantos kilogramos desea llevar?. "))
        break
    except ValueError:
        print("¡ERROR! Ingrese un monto válido")

if user not in fruits:
    print("No disponemos de la fruta solicitada")

else:
    print(f"{kg}Kg de {user} sale ${fruits[user]*kg}")




