from funcion import *
def main():
    menu = Menu()
    while True:
        menu.mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        menu.seleccionar_opcion(opcion)
        if opcion == 5:
            break

if __name__ == "__main__":
    main()