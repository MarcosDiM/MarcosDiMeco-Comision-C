"""
#Ejercicio 1
import random

def paths(options, counter=0):
    rat_path=random.choice(options)

    if rat_path==1:
        print("La rata vuelve a la jaula")
        return paths(options, counter+3)
    elif rat_path==2:
        print("La rata vuelve a la jaula")
        return paths(options, counter+5)
    else:
        print("¡La rata logró salir de la jaula!")
        return counter+7

options=[1,2,3]
total_time=paths(options)
print(f"La rata se demoró {total_time} minutos en salir de la jaula")
"""

#Ejercicio 2

#Escribe una función recursiva llamada f(n) que tome un número entero n como entrada y devuelva una cadena que representa el número n con los dígitos en orden inverso

def f(n):
    s=str(n)
    if len(s)<=1:
        return s
    return s[-1]+f(int(s[:-1]))