#PARTE 1.2 

#1.	Calcular el perímetro y área de un rectángulo dada su base y su altura.

base= int(input("Ingresar base de rectangulo: "))
altura= int(input("Ingresar la altura del rectangulo: "))
area = base * altura 
print("El area del rectangulo es de: ", area)

#2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto1 = int(input("Ingresar cateto 1: "))
cateto2 = int(input("Ingresar cateto 2: "))
hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
print("La longitud de la hipotenusa es de: ", hipotenusa)

#3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

num1 = int(input("Ingresar numero 1: "))
num2 = int(input("Ingresar numero 2: "))

suma = num1 + num2
print("SUMA:", suma)

resta = num1 - num2
print("\n RESTA:", resta)

multiplicacion = num1 * num2
print("\n MULTIPLICACION:", multiplicacion)

division = num1 / num2
print("\n DIVISION:", division)
print("\n")

#4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius

f = int(input("Ingresar grados Fahrenheit: "))
c = (f - 32)*(5/9)
print(f,"grados Fahrenheit son ", c, " grados celcius. \n")

#5. Solucionar las instrucciones

#a 
nombre = input("Cual es tu cancion favorita?")

#b 
precio = int(input("Precio: "))
total = 0
total = total + precio

#c
edad = int(input("Edad: "))
print("Tu edad es: ", edad)

#d
edad = int(input("Edad: "))
print("Veamos si tu edad es 18... edad: ", edad)

#6.	Calcular la media de tres números pedidos por teclado.
num1 = int(input("Ingresar numero 1 al azar:"))
num2 = int(input("Ingresar numero 2 al azar:"))
num3 = int(input("Ingresar numero 3 al azar:"))

media = (num1 + num2 + num3)/3
print("La media es igual a: ", media)

#7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
minutos =  int(input("Ingresar minutos: "))
horas = minutos / 60
print(minutos, "son igual a: ",horas," horas")

#8. Sueldo y comisiones
sueldo = int(input("Sueldo: "))
comision = sueldo/10
comisiones = int(input("Cantidad de ventas: "))
total_comision = comision * comisiones
sueldo_total = total_comision + sueldo
print("Total en comisiones: ", total_comision)
print("Sueldo total: ", sueldo_total)

#9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
total_compra= int(input("Ingresar total de la compra: "))
precio_final = total_compra * 0.85
print("El precio final es de: ", precio_final)

#10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos
parciales = float(input("Ingresar promedio de parciales: ")) * 0.55
examen_final = float(input("Ingresar calificacion examen final: ")) * 0.30
calif_trabajo_final = float(input("Ingresar calificacion trabajo final: ")) * 0.15
promedio_final = parciales + examen_final + calif_trabajo_final
print("El promedio final es: ", promedio_final)

#11. Pide al usuario dos números y muestra la “distancia” entre ellos.
numero1 = abs(input("Ingresar numero 1: "))
numero2 = abs(input("Ingresar numero 2: "))
distancia= numero1 - numero2
print("La distancia entre ellos es: ", distancia)

#12. Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
num = int(input("Ingresar numuero"))
raiz_cuadrada = num **(1/2)
raiz_cubica = num**(1/3)
print("Raiz cuadrada: ", raiz_cuadrada)
print("Raiz cubica: ", raiz_cubica)

#13. Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
numero = input("Ingresar un numero: ")
numero_reversa = numero[-1:-len(numero)-1:-1] 
print(numero_reversa)

#14. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
var1= int(input("Ingresar numero 1: "))
var2= int(input("Ingresar numero 2: "))
var_vacia= var1
var1 = var2 
var2 = var_vacia
print("Variable 1:", var1," variable2: ", var2)


#15. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
hora_salida = int(input("Ingresar la hora de salida: "))
min_salida = int(input("Ingresar los minutos de salida: "))
seg_salida = int(input("Ingresar los segundos de salida: "))
tiempo_viaje = int(input("Ingresar el tiempo del recorrido en segundos: "))

tiempo_total = hora_salida * 3600 + min_salida * 60 + seg_salida + tiempo_viaje

hora_llegada = int(tiempo_total / 3600)
min_llegada = int((tiempo_total % 3600)/ 60 )
seg_llegada = tiempo_total % 60

print(f"El horario de llegada es: {hora_llegada}:{min_llegada}:{seg_llegada}")

#16. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
nombre = str(input("Ingresar nombre: "))
primer_apellido = str(input("Ingresar primer apellido: "))
segundo_apellido = str(input("Ingresar segundo apellido: "))

i1= nombre[0]
i2= primer_apellido[0]
i3= segundo_apellido[0]
print("Sus iniciales son ", i1,i2,i3)

#17. Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.
usuario = str(input("Ingrese su nombre: "))
print("Ahora esta en la matrix, ", usuario)

#18. Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.
valor_cena = float(input("Ingresar costo de la cena: "))
valor_total  = valor_cena * (16.2 / 100)
print("El costo final de la cena es de: ", valor_total)

#19.Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.
dia_nacimiento = int(input("Ingresa el numero de dia de nacimiento: "))
mes_nacimiento = int(input("Ingresar numero de mes de nacimiento: "))
anio_nacimiento = int(input("Ingresa el año de nacimiento: "))
print(dia_nacimiento,"/",mes_nacimiento,"/",anio_nacimiento)

#20. Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.
fecha_nacimiento = str(int(input("Ingresar fecha de nacimiento en numeros y seguido: ")))
dia = fecha_nacimiento[0:2]
mes = fecha_nacimiento[2:4]
anio = fecha_nacimiento[4:8]
print(dia,"/",mes,"/",anio)

#21. Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.

km_por_litro = float(input("Ingresar cuantos km se pueden recorrer con un litro: "))
capacidad_tanque = float(input("Ingresar capacidad en litros del tanque: "))
km_recorrer = float(input("Ingresar los km que se recorreran: "))

km_por_tanque = km_por_litro * capacidad_tanque
tanques_totales = km_recorrer / km_por_tanque

print(f"Se necesitan {tanques_totales:.2f} para recorrer {km_recorrer}km")
