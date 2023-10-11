#Funcion ejercicio 1

def verify_dni(dni):
    if len(str(dni)) == 7 or len(str(dni)) ==8:
        return True
    else:
        return False

#Funciones ejercicio 2

def return_adress(clients):
    adresses = []
    for client in clients:
        adresses.append(client[3])
    adresses = list(set(adresses))
    for adress in adresses:
        print(adress)


#Funciones ejercicio 3

import datetime
def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def get_membership_number(members):
    while True:
        try:
            membership_number = int(input("Ingrese el número de socio: "))
            if any(member["member"] == membership_number for member in members):
                print("¡Error! El número de socio ya está en uso. Intente con otro número.")
            else:
                return membership_number
        except ValueError:
            print("¡Error! Por favor, ingrese un número válido.")

def get_date():
    while True:
        new_date = input("Ingrese la fecha de ingreso (dd/mm/yyyy): ")
        if validate_date(new_date):
            return new_date
        else:
            print("¡Error! Por favor, ingrese una fecha válida en formato dd/mm/yyyy.")
