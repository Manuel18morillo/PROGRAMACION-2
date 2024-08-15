from parcial import Personas
from parcial import universidades
from parcial import restaurantes
from parcial import Animales

def menu_principal():
    while True:
        print("MENU PRINCIPAL")
        print("1. Personas")
        print("2. universidades")
        print("3. restaurantes")
        print("4. Animales")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            p = Personas()
            print(p.menu())
        elif opcion =="2":
            u = universidades()
            print(u.menu())
        elif opcion == "3":
            res = restaurantes()
            print(res.menu())
        elif opcion == "4":
            An = Animales()
            print(An.menu())
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


# Ejecutar el menú principal
menu_principal()