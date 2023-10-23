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
    