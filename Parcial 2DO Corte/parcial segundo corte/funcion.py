class Menu:
    def __init__(self):
        #declaramos  las opciones principales
        self.opciones = {
            1: "Persona",
            2: "Universidad",
            3: "Notas",
            4: "Cedulas",
            5: "Salir"
        }

    def mostrar_menu(self):
        #muestra el menu y obtiene el key y value de las opciones del menu principal y las muestra
        print("\nMENU PRINCIPAL")
        for opcion, descripcion in self.opciones.items():
            print(f"{opcion}. {descripcion}")

    def seleccionar_opcion(self, opcion):
        #verifica la selecion de el menu principal
        if opcion == 1:
            sub_menu = SubMenu("Persona")
            sub_menu.mostrar_menu()
            sub_menu.seleccionar_opcion()
        elif opcion == 2:
            sub_menu = SubMenu("Universidad")
            sub_menu.mostrar_menu()
            sub_menu.seleccionar_opcion()
        elif opcion == 3:
            sub_menu = SubMenu("Nota")
            sub_menu.mostrar_menu()
            sub_menu.seleccionar_opcion()
        elif opcion == 4:
            sub_menu = SubMenu("Cedula")
            sub_menu.mostrar_menu()
            sub_menu.seleccionar_opcion()
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


class SubMenu:
    def __init__(self, nombre):
        #edeclara las lista y las opciones del sub menu
        self.nombre = nombre
        self.opciones = {
            1: "Agregar elemento",
            2: "Eliminar elemento",
            3: "Actualizar elemento",
            4: "Mostrar lista",
            5: "Atrás"
        }
        self.lista = []
        self.lista2 = []
        self.lista3 = []
        self.lista4 = []
        self.lista5 = []

    def mostrar_menu(self):
        #Muestra el sub menu y obtiene el key y valiue de las opciones del menu ya las muestra
        print(f"\nSUBMENU - {self.nombre}")
        for opcion, descripcion in self.opciones.items():
            print(f"{opcion}. {descripcion}")

    def seleccionar_opcion(self):
        # el conficional para ingresar opciones del submenu
        while True:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1:
                self.agregar_elemento()
                self.mostrar_menu()
            elif opcion == 2:
                self.eliminar_elemento()
                self.mostrar_menu()
            elif opcion == 3:
                self.actualizar_elemento()
                self.mostrar_menu()
            elif opcion == 4:
                self.mostrar_lista()
                self.mostrar_menu()
            elif opcion == 5:
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def agregar_elemento(self):
        #Se piden los datos a inresar en la lista
        elemento = input("Ingrese el Primer elemento: ")
        elemento2 = input("Ingrese el Segundo elemento: ")
        elemento3 = input("Ingrese el Tercer elemento: ")
        elemento4 = input("Ingrese el Cuarto elemento: ")
        elemento5 = input("Ingrese el Quinto elemento: ")
 
        #Se Registra en lista
        self.lista.append(elemento)
        self.lista2.append(elemento2)
        self.lista3.append(elemento3)
        self.lista4.append(elemento4)
        self.lista5.append(elemento5)

        #Se muestra los elementos añadidos a la lista
        print(f"Elemento '{elemento}' agregado con éxito.")
        print(f"Elemento '{elemento2}' agregado con éxito.")
        print(f"Elemento '{elemento3}' agregado con éxito.")
        print(f"Elemento '{elemento4}' agregado con éxito.")
        print(f"Elemento '{elemento5}' agregado con éxito.")

    def eliminar_elemento(self):
        #elimina datos de las listas
        if self.lista:
            print("Lista actual:")
            self.mostrar_lista()

            indice = int(input("Ingrese el índice del elemento a eliminar: "))
            #elimina datos de la lista 1
            if 0 <= indice < len(self.lista):
                elemento_eliminado = self.lista.pop(indice)
                print(f"Elemento '{elemento_eliminado}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")
            #elimina datos de la lista 2
            if 0 <= indice < len(self.lista2):
                elemento_eliminado2 = self.lista2.pop(indice)
                print(f"Elemento '{elemento_eliminado2}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")
            
            #elimina datos de la lista 3
            if 0 <= indice < len(self.lista3):
                elemento_eliminado3 = self.lista3.pop(indice)
                print(f"Elemento '{elemento_eliminado3}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")
            
            #elimina datos de la lista 4
            
            if 0 <= indice < len(self.lista4):
                elemento_eliminado4 = self.lista4.pop(indice)
                print(f"Elemento '{elemento_eliminado4}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")
            #elimina datos de la lista 5
            #iF validan que el dato este dentro del rango de la lista
            if 0 <= indice < len(self.lista5):
                elemento_eliminado5 = self.lista5.pop(indice)
                print(f"Elemento '{elemento_eliminado5}' eliminado con éxito.")

            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

        #si no hay datos en la lista  manda el mensaje para decir que la lista esta vacia
        else:
            print("La lista está vacía. No hay elementos para eliminar.")

    def actualizar_elemento(self):
        # se actualiza los datos se pone dentro de cada for el dato para ver hasta que dato quiere actualizar
        if self.lista:
            print("Lista actual:")
            self.mostrar_lista()
            indice = int(input("Ingrese el índice del elemento a actualizar: "))
            if 0 <= indice < len(self.lista):
                nuevo_elemento = input("Ingrese el nuevo valor para el elemento: ")
                self.lista[indice] = nuevo_elemento
                print("Elemento actualizado con éxito.")
            else:       
                print("Índice fuera de rango. No se actualizó ningún elemento.")
            

            print("SI quiere dejar de actualizar ingrese -1, tiene que ingresar el -1 por cada dato que ya no quiera actualizar")
            indice2 = int(input("Ingrese el índice del elemento a actualizar: "))
            if 0 <= indice2 < len(self.lista2):
                nuevo_elemento2 = input("Ingrese el nuevo valor para el elemento: ")
                self.lista2[indice2] = nuevo_elemento2
                print("Elemento actualizado con éxito.")
                print("SI quiere dejar de actualizar ingrese -1")
                indice3 = int(input("Ingrese el índice del elemento a actualizar: "))
                if 0 <= indice3 < len(self.lista3):
                    nuevo_elemento3 = input("Ingrese el nuevo valor para el elemento: ")
                    self.lista3[indice3] = nuevo_elemento3
                    print("Elemento actualizado con éxito.")
                    print("SI quiere dejar de actualizar ingrese -1")
                    indice4 = int(input("Ingrese el índice del elemento a actualizar: "))
                    if 0 <= indice4 < len(self.lista4):
                        nuevo_elemento4 = input("Ingrese el nuevo valor para el elemento: ")
                        self.lista4[indice4] = nuevo_elemento4
                        print("Elemento actualizado con éxito.")
                        print("SI quiere dejar de actualizar ingrese -1")
                        indice5 = int(input("Ingrese el índice del elemento a actualizar: "))
                        if 0 <= indice5 < len(self.lista5):
                            nuevo_elemento5 = input("Ingrese el nuevo valor para el elemento: ")
                            self.lista5[indice5] = nuevo_elemento5
                            print("Elemento actualizado con éxito.")
                        else:       
                            print("El indice esta fuera de rango o ha decidino no actualizar")
                    else:       
                        print("El indice esta fuera de rango o ha decidino no actualizar")
                else:       
                    print("El indice esta fuera de rango o ha decidino no actualizar")
            else:       
                print("El indice esta fuera de rango o ha decidino no actualizar")
            
        else:
            print("La lista está vacía. No hay elementos para actualizar.")

    def mostrar_lista(self):
        # usados el condicional de la lista  si existe hara lo que indica,obtenemos el indice y el elemento de la lista como key y value 
        #usamos un enumerate para imprimir la lista con un contador asi se imprimira la lista con el indice correspondiente a su posicion 
        if self.lista:
            for indice, elemento in enumerate(self.lista):
                print(f"{indice}. {elemento}")
        if self.lista2:
            for indice2, elemento2 in enumerate(self.lista2):
                print(f"{indice2}. {elemento2}")

        if self.lista3:
            for indice3, elemento3 in enumerate(self.lista3):
                print(f"{indice3}. {elemento3}")
        if self.lista4:
            for indice4, elemento4 in enumerate(self.lista4):
                print(f"{indice4}. {elemento4}")
        if self.lista5:
            for indice5, elemento5 in enumerate(self.lista5):
                print(f"{indice5}. {elemento5}")
        else:
            print("La lista está vacía.")