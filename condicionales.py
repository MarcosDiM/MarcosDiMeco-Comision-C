ingreso = str(input("Ingresar fecha como dia de la semana, dia/mes: "))


dia= ingreso[0 : ingreso.find(",")]
num_dia= int(ingreso[ingreso.find(" ")+1 : ingreso.find("/")])
mes= int(ingreso[ingreso.find("/")+1 : len(ingreso)])

dia = dia.upper()

if num_dia > 31 or num_dia < 1:
    print("Dia ingresado no valido")
    quit()
elif mes < 1 or mes > 12:
    print("Mes ingresado no valido")
    quit()

if (dia != "LUNES" and dia != "MARTES" and dia !="MIERCOLES" and dia !="JUEVES" and dia !="VIERNES"):
    print("Dia de la semana no valido")
    quit()

if dia == "LUNES" or dia == "MARTES" or dia == "MIERCOLES":
    print(f"El dia {dia}, {num_dia}/{mes} se tomaron examenes?")
    examen = int(input("Si = 1 / No = 2 : "))
    if examen == 1: 
        aprobados= int(input("Cantidad de alumnos aprobados: "))
        desaprobados= int(input("Cantidad de alumnos desaprobados: "))
        total_alumnos = aprobados + desaprobados
        porcentaje = (aprobados * 100) / total_alumnos
        print(f"El porcentaje de alumnos aprobados es de %{porcentaje}")
    elif examen == 2:
        print("No se tomaron examenes")

if dia == "JUEVES":
    porcentaje = int(input("Ingresar el porcentaje de alumnos que asistio: %"))
    if porcentaje > 50:
        print("Asistio la mayoria")
    else:
        print("No asistio la mayoria")

if dia == "VIERNES": 
    if num_dia == 1 and mes==1 or mes==7:
        print("Comienza nuevo ciclo")
        alumnos_viajeros = int(input("Ingresar cantidad de alumnos ingresantes: "))
        arancel = int(input("Ingresar valor del arancel: "))
        ingreso_total = alumnos_viajeros * arancel
        print(f"El ingreso total por aranceles debe ser de ${ingreso_total}")
    else:
        print("No es fecha de comienzo de nuevo ciclo.")