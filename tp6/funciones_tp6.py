#Funcion ejercicio 2

def delete_number_list(list):
    delete_number = int(input("Ingrese un numero para borrar de la lista: "))

    if delete_number in list:
        for i in range(len(list)):
            if delete_number == list[i]:
                list.remove(list[i])
                break
    else:
        print("El numero ingresado no esta en la lista")

    return(list)

#Funcion ejercicio 3

def summation_list(list):
    summation = 0
    for i in range(len(list)):
        summation = summation + list[i]
    return summation

#Funcion ejercicio 5

def len_number_tuple(list):
    large_list = len(list)
    list_len_numbers = []
    for i in range(large_list):
        large_number = str(list[i])
        list_len_numbers.append((list[i], len(large_number)))
    return list_len_numbers

#Funciones ejercicio 6

def list_without_repeat(list):
    unique_list = []
    for student in list:
        if student not in unique_list:
            unique_list.append(student)
    return unique_list

def repeat_into_lists(list1, list2):
    repeat_list = []
    for item in list1:
        if item in list2:
            repeat_list.append(item)
    return repeat_list

def not_repeat_into_lists(list1, list2):
    for item in list1:
        if item in list2:
            list1.remove(item)
    return list1

#Funciones ejercicio 9

def complete_matrix(matrix):
    import random
    numbers_matrix = list(range(1,9))*2
    random.shuffle(numbers_matrix)
    for i in range(4):
        for j in range(4):
            matrix[i][j] = numbers_matrix.pop()
    return matrix