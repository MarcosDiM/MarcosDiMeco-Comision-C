import funciones_tp6
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
