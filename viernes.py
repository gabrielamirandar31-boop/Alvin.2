print("Bienvenido al sistema de control de colas")
cola = ["Ana", "Pedro", "Carlos"]
retirados = []

# mostrar cola
print(cola)
print("Elija una opcion(1-6):")
print("1. Agregar estudiante regular")
print("2. agregar estudiante prioritario")
print("3. Cancelar solicitud")
print("4. atender usuario")
print("5. Consultar cola")
print("6. Salir del sistema")

# pedir opcion
while True:
    print("Elija una opcion(1-6):")
    print("1. Agregar estudiante regular")
    print("2. agregar estudiante prioritario")
    print("3. Cancelar solicitud")
    print("4. atender usuario")
    print("5. Consultar cola")
    print("6. Salir del sistema")
    opcion = input("Ingrese su opcion: ")

    if opcion == "1":
        while True:
            nombre = input("Ingrese el nombre del estudiante: ")
            if nombre == "":
                print("No se puede agregar un estudiante sin nombre.")
            else:
                cola.append(nombre)
                print(f"{nombre} ha sido agregado a la cola.")
                print(cola)
                break

    elif opcion == "6":
        confirmacion = input("¿Está seguro que desea salir del sistema? (s/n): ").lower()
        if confirmacion == "s":
            print("Saliendo del sistema...")
            break
        
    
        