import funciones_var_dimensionadas

#Ejercicio 1

passengers = [("Pablo", "12345678", "Mendoza"), ("Pepe", "1234567", "Mendoza"), ("Martin", "12345676", "San Juan"), ("Joaquin", "12345432", "Montevideo"), ("Marcos", "12312312", "Lima")]
citys_and_countries = [("Mendoza", "Argentina"), ("San Juan", "Argentina"), ("Montevideo", "Uruguay"), ("Lima", "Perú")]
city = ''
country = ''
name = ''
dni = 0
count = 0
while True:
    print(f"Seleccione una opcion:\n1.Agregar pasajeros a la lista de viajeros\n2.Agregar ciudades a la lista de ciudades\n3.Buscar a que ciudad viaja por DNI\n4.Mostrar cantidad de pasajeros que viajan a una ciudad\n5.Buscar pais al que viaja por DNI\n6.Mostrar cuantos pasajeros viajan a un pais\n0. Salir")
    option = int(input())
    if option == 1:
        while True:
            print(f"Ingrese los siguientes datos:\n")
            name = input("Nombre:")
            dni = int(input("DNI:"))
            city = input("Ciudad:")
            if funciones_var_dimensionadas.verify_dni(dni) == True:
                passengers.append((name, dni, city))
                break
            else: 
                print("Ingrese un dni valido por favor")
    elif option == 2:
        city = input("Ingrese el nombre de la ciudad: ")
        country = input("Ingrese en pais al que pertenece la ciudad: ")
        citys_and_countries.append((city, country))
    elif option == 3:
        print(f"Ingrese el DNI del pasajero:")
        dni = int(input("DNI:"))
        for person in passengers:
            if person[1] == dni:
                print(f"La ciudad a la que viaja el pasajero con el dni {dni} es {person[2]}")

    elif option == 4:
        city = input("Ingrese una ciudad: ")
        for person in passengers:
            if person[2] == city:
                count += 1
        print(f"La cantidad de pasajeros que viajan a {city} es de {count}")
    elif option == 5:
        dni = int(input("Ingrese DNI:"))
        for person in passengers:
            for location in citys_and_countries:
                if person[1] == dni:
                    if person[2] == location[0] :
                        print(f"El pais al que pertenece es {location[1]}")
                    else:
                        print(f"No se ha podido encontrar el pais al cual pertenece {person[2]}")
    elif option == 6:
        country = input("Ingrese un pais:")
        for person in passengers:
            for location in citys_and_countries:
                if person[2] == location[0] and location[1] == country:
                    count += 1
        print(f"La cantidad de personas que viajan a {country} es de {count}")
    elif option == 7:
        print("Adios :)")
        break

#Ejercicio 2

my_clients = [("cliente1", "5", "1234.5", "calle1"),("cliente1", "6", "12.5", "calle1"), ("cliente2", "5", "134.5", "calle2"), ("cliente3", "6", "12300", "calle3") ]
funciones_var_dimensionadas.return_adress(my_clients)

#Ejercicio 3

members = [
    {"member": 1, "name": "Amanda Núñez", "start_date": "17/03/2009", "fee": True},
    {"member": 2, "name": "Bárbara Molina", "start_date": "17/03/2009", "fee": True},
    {"member": 3, "name": "Lautaro Campos", "start_date": "17/03/2009", "fee": True}
]

while True:
    print("1. Mostrar cantidad de socios")
    print("2. Registrar pago por número de socio")
    print("3. Modificar fecha de ingreso")
    print("4. Dar de baja por número de socio")
    print("5. Mostrar todos los socios")
    print("6. Registrar un nuevo socio")
    print("0. Salir")
    option = input("Ingrese una opción: ")

    if option == "1":
        print(f"Cantidad de socios: {len(members)}")
    elif option == "2":
        membership_number = int(input("Ingrese el número de socio para registrar el pago: "))
        for member in members:
            if member["member"] == membership_number:
                member["fee"] = True
                print("Pago registrado exitosamente.")
                break
        else:
            print("Socio no encontrado.")
    elif option == "3":
        print("Ingrese la fecha que desea reemplazar:")
        old_date = funciones_var_dimensionadas.get_date()
        print("Ingrese la nueva fecha:")
        new_date = funciones_var_dimensionadas.get_date()
        modification_count = 0
        for member in members:
            if member["start_date"] == old_date:
                member["start_date"] = new_date
                modification_count += 1
        print(f"Se modificaron las fechas de ingreso de {modification_count} socios.")
    elif option == "4":
        try:
            membership_number = int(input("Ingrese el número de socio a dar de baja: "))
            for member in members:
                if member["member"] == membership_number:
                    members.remove(member)
                    print(f"Socio {membership_number} dado de baja exitosamente.")
                    break
            else:
                print("Socio no encontrado.")
        except ValueError:
            print("¡Error! Por favor, ingrese un número válido para el socio.")
    elif option == "5":
        for member in members:
            print(f"Socio {member['member']}: {member['name']} - Fecha de ingreso: {member['start_date']} - Cuota al día: {member['fee']}")
    elif option == "6":
        new_membership_number = funciones_var_dimensionadas.get_membership_number()
        new_name = input("Ingrese el nombre y apellido del nuevo socio: ")
        new_start_date = funciones_var_dimensionadas.get_date()
        new_member = {
            "member": new_membership_number,
            "name": new_name,
            "start_date": new_start_date,
            "fee": True
        }
        members.append(new_member)
        print("Nuevo socio registrado exitosamente.")
    elif option == "0":
        print("Adiós :)")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
