#El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir
from funciones import most,least
#programa principal
x = int(input("Un numero:"))
y = int(input("Otro numero:"))

print(most(x-3, least(x+2, y-5)))

#No estabamos utilizando los parametros de las funciones (a y b). Estabamos utilizando las variables globales x e y.
