class Personas:
    def __init__(self) :
        global nombre,apellido,cedula,edad,sexo
        nombre=[]
        apellido=[]
        cedula=[]
        edad=[]
        sexo=[]
    
    def menu(self):
        while True:
            print("MENU PERSONAS")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print(Personas.agregar())
            elif opcion == "2":
                print(Personas.listar())
            elif opcion == "3":
                 print(Personas.eliminar())
            elif opcion =="4":
                print(Personas.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
            
    
    def agregar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        per=input("ingrese su nombre ")
        cedu=input("ingrese su cedula ")
        ed=input("ingrese su edad ")
        apell=input("ingrese su apellido ")
        gen=input("ingrese su genero ")

        apellido.append(apell)
        nombre.append(per)
        cedula.append(cedu)
        edad.append(ed)
        sexo.append(gen)

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        for i in range(len(nombre)):
            print(i,nombre[i])
            print(i,apellido[i])
            print(i,cedula[i])
            print(i,edad[i])
            print(i,sexo[i])
        return f"Lista De Datos Ingresados:",nombre,apellido,cedula,edad,sexo
            
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        if nombre:
            indice = int(input("Ingrese el índice del elemento a eliminar: "))
            #elimina datos de la lista 1
            if 0 <= indice < len(nombre):
                elemento_eliminado = nombre.pop(indice)
                print(f"Elemento '{elemento_eliminado}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(apellido):
                elemento_eliminado2 = apellido.pop(indice)
                print(f"Elemento '{elemento_eliminado2}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(edad):
                elemento_eliminado3 = edad.pop(indice)
                print(f"Elemento '{elemento_eliminado3}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(cedula):
                elemento_eliminado4 = cedula.pop(indice)
                print(f"Elemento '{elemento_eliminado4}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(sexo):
                elemento_eliminado5 = sexo.pop(indice)
                print(f"Elemento '{elemento_eliminado5}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")
            return f"La lista actual es",nombre,apellido,cedula,edad,sexo
            
    def  actualizar():
        if nombre:
            indice = int(input("Ingrese el índice del elemento a actualizar: "))
            if 0 <= indice < len(nombre):
                nuevo_elemento = input("Ingrese el nombre que actualizara")
                nombre[indice] = nuevo_elemento
                print("Elemento actualizado con éxito.")


                print("actualizar apellido")
                if 0 <= indice < len(apellido):
                    nuevo_elemento2 = input("Ingrese el Apelldio nuevo: ")
                    apellido[indice] = nuevo_elemento2
                    print("Elemento actualizado con éxito.")

                    print("actualizar  Edad")
                    if 0 <= indice < len(edad):
                        nuevo_elemento3 = input("Ingrese La edad nueva: ")
                        edad[indice] = nuevo_elemento3
                        print("Elemento actualizado con éxito.")

                        print("actualizar  Cedula")
                        if 0 <= indice < len(cedula):
                            nuevo_elemento4 = input("Ingrese La cedula nueva: ")
                            cedula[indice] = nuevo_elemento4
                            print("Elemento actualizado con éxito.")
                            if 0 <= indice < len(sexo):
                                nuevo_elemento5 = input("Ingrese El sexo nuevo:")
                                sexo[indice] = nuevo_elemento5
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

        
#CLASE UNIVERSIDADES    
class universidades:
    def __init__(self) :
        global universidad,telefono,calidad,ubicacion,dueño
        universidad=[]
        telefono=[]
        calidad=[]
        ubicacion=[]
        dueño=[]
    
    def menu(self):
        while True:
            print("MENU UNIVERSIDADES")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(universidades.agregar())
            elif opcion == "2":
                print(universidades.listar())
            elif opcion == "3":
                print(universidades.eliminar())
            elif opcion =="4":
                print(universidades.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        uni=input("ingrese universidad ")
        tel=input("ingrese telefono de la universidad ")
        cal=input("Ingrese Calidad ")
        ubi=input("ingrese ubicacion ")
        du=input("ingrese dueño")

        universidad.append(uni)
        telefono.append(tel)
        calidad.append(cal)
        ubicacion.append(ubi)
        dueño.append(du)

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        for i in range(len(universidad)):
            print(i,universidad[i])
            print(i,telefono[i])
            print(i,calidad[i])
            print(i,ubicacion[i])
            print(i,dueño[i])
        return f"Lista De Datos Ingresados:",universidad,telefono,calidad,ubicacion,dueño
            
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        if universidad:
            indice = int(input("Ingrese el índice del elemento a eliminar: "))
            #elimina datos de la lista 1
            if 0 <= indice < len(universidad):
                elemento_eliminado = universidad.pop(indice)
                print(f"Elemento '{elemento_eliminado}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(telefono):
                elemento_eliminado2 = telefono.pop(indice)
                print(f"Elemento '{elemento_eliminado2}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(calidad):
                elemento_eliminado3 = calidad.pop(indice)
                print(f"Elemento '{elemento_eliminado3}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(ubicacion):
                elemento_eliminado4 = ubicacion.pop(indice)
                print(f"Elemento '{elemento_eliminado4}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(dueño):
                elemento_eliminado5 = dueño.pop(indice)
                print(f"Elemento '{elemento_eliminado5}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")
            return f"La lista actual es",universidad,telefono,calidad,ubicacion,dueño
    
    def  actualizar():
        if universidad:
            indice = int(input("Ingrese el índice del elemento a actualizar: "))
            if 0 <= indice < len(universidad):
                nuevo_elemento = input("Ingrese la universidad que actualizara")
                universidad[indice] = nuevo_elemento
                print("Elemento actualizado con éxito.")


                print("actualizar telefono")
                if 0 <= indice < len(telefono):
                    nuevo_elemento2 = input("Ingrese telefono nuevo: ")
                    telefono[indice] = nuevo_elemento2
                    print("Elemento actualizado con éxito.")

                    print("actualizar  calidad")
                    if 0 <= indice < len(calidad):
                        nuevo_elemento3 = input("Ingrese La calidad nueva: ")
                        calidad[indice] = nuevo_elemento3
                        print("Elemento actualizado con éxito.")

                        print("actualizar  ubicacion")
                        if 0 <= indice < len(ubicacion):
                            nuevo_elemento4 = input("Ingrese La ubicacion nueva: ")
                            ubicacion[indice] = nuevo_elemento4
                            print("Elemento actualizado con éxito.")
                            if 0 <= indice < len(dueño):
                                nuevo_elemento5 = input("Ingrese El dueño nuevo:")
                                dueño[indice] = nuevo_elemento5
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


#MENU RESTAURANTES
class restaurantes:
    def __init__(self) :
        global restaurante,number,direccion,numero_estrellas,empleado_año
        restaurante=[]
        number=[]
        direccion=[]
        numero_estrellas=[]
        empleado_año=[]
    
    def menu(self):
        while True:
            print("MENU RESTAURANTES")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(restaurantes.agregar())
            elif opcion == "2":
                print(restaurantes.listar())
            elif opcion == "3":
                print(restaurantes.eliminar())
            elif opcion =="4":
                print(restaurantes.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        re=input("ingrese restaurante ")
        nu=input("ingrese telefono ")
        di=input("Ingrese direccion ")
        ne=input("ingrese numero estrellas ")
        ea=input("ingrese empleado del año ")

        restaurante.append(re)
        number.append(nu)
        direccion.append(di)
        numero_estrellas.append(ne)
        empleado_año.append(ea)


        
    def listar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')  
        for i in range(len(restaurante)):
            print(i,restaurante[i])
            print(i,number[i])
            print(i,direccion[i])
            print(i,numero_estrellas[i])
            print(i,empleado_año[i])
        return f"Lista De Datos Ingresados:",restaurante,number,direccion,numero_estrellas,empleado_año
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        if restaurante:
            indice = int(input("Ingrese el índice del elemento a eliminar: "))
            #elimina datos de la lista 1
            if 0 <= indice < len(restaurante):
                elemento_eliminado = restaurante.pop(indice)
                print(f"Elemento '{elemento_eliminado}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(number):
                elemento_eliminado2 = number.pop(indice)
                print(f"Elemento '{elemento_eliminado2}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(direccion):
                elemento_eliminado3 = direccion.pop(indice)
                print(f"Elemento '{elemento_eliminado3}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(numero_estrellas):
                elemento_eliminado4 = numero_estrellas.pop(indice)
                print(f"Elemento '{elemento_eliminado4}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(empleado_año):
                elemento_eliminado5 = empleado_año.pop(indice)
                print(f"Elemento '{elemento_eliminado5}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")
            return f"La lista actual es",restaurante,number,direccion,numero_estrellas,empleado_año
    
    def  actualizar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        if restaurante:
            indice = int(input("Ingrese el índice del elemento a actualizar: "))
            if 0 <= indice < len(restaurante):
                nuevo_elemento = input("Ingrese la restaurante nuevo")
                restaurante[indice] = nuevo_elemento
                print("Elemento actualizado con éxito.")


                print("actualizar numero telefonico")
                if 0 <= indice < len(number):
                    nuevo_elemento2 = input("Ingrese numero nuevo: ")
                    number[indice] = nuevo_elemento2
                    print("Elemento actualizado con éxito.")

                    print("actualizar  direccion")
                    if 0 <= indice < len(direccion):
                        nuevo_elemento3 = input("Ingrese La direccion nueva: ")
                        direccion[indice] = nuevo_elemento3
                        print("Elemento actualizado con éxito.")

                        print("actualizar  numero de estrellas")
                        if 0 <= indice < len(numero_estrellas):
                            nuevo_elemento4 = input("Ingrese numero de estrellas nuevo: ")
                            numero_estrellas[indice] = nuevo_elemento4
                            print("Elemento actualizado con éxito.")
                            if 0 <= indice < len(empleado_año):
                                nuevo_elemento5 = input("Ingrese empleado del año nuevo:")
                                empleado_año[indice] = nuevo_elemento5
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


#MENU ANIMALES
class Animales:
    def __init__(self) :
        global animal,numero_patas,fecha_vacunacion,tutor,color
        animal=[]
        numero_patas=[]
        fecha_vacunacion=[]
        tutor=[]
        color=[]
    
    def menu(self):
        while True:
            print("MENU ANIMALES")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Actualizar")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Animales.agregar())
            elif opcion == "2":
                print(Animales.listar())
            elif opcion == "3":
                print(Animales.eliminar())
            elif opcion =="4":
                print(Animales.actualizar())
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR')
        an=input("Ingrese animal ")
        np=input("Ingrese numero patas ")
        fe=input("ingrese fecha vacunacion")
        tu=input("Ingrese tutor")
        co=input("ingrese color")

        animal.append(an)
        numero_patas.append(np)
        fecha_vacunacion.append(fe)
        tutor.append(tu)
        color.append(co)

        
    def listar():   
        print('HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR')
        for i in range(len(animal)):
            print(i,animal[i])
            print(i,numero_patas[i])
            print(i,fecha_vacunacion[i])
            print(i,tutor[i])
            print(i,color[i])
        return f"Lista De Datos Ingresados:",animal,numero_patas,fecha_vacunacion,tutor,color
    
    def eliminar(): 
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR')
        if animal:
            indice = int(input("Ingrese el índice del elemento a eliminar: "))
            #elimina datos de la lista 1
            if 0 <= indice < len(animal):
                elemento_eliminado = animal.pop(indice)
                print(f"Elemento '{elemento_eliminado}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(numero_patas):
                elemento_eliminado2 = numero_patas.pop(indice)
                print(f"Elemento '{elemento_eliminado2}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(fecha_vacunacion):
                elemento_eliminado3 = fecha_vacunacion.pop(indice)
                print(f"Elemento '{elemento_eliminado3}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(tutor):
                elemento_eliminado4 = tutor.pop(indice)
                print(f"Elemento '{elemento_eliminado4}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")

            if 0 <= indice < len(color):
                elemento_eliminado5 = color.pop(indice)
                print(f"Elemento '{elemento_eliminado5}' eliminado con éxito.")
            else:
                print("Índice fuera de rango. No se eliminó ningún elemento.")
            return f"La lista actual es",animal,numero_patas,fecha_vacunacion,tutor,color
    
    def  actualizar():
        print('HAZ SELECCIONADO LA FUNCIONALIDAD ACTUALIZAR')
        if animal:
            indice = int(input("Ingrese el índice del elemento a actualizar: "))
            if 0 <= indice < len(animal):
                nuevo_elemento = input("Ingrese la animal nuevo")
                animal[indice] = nuevo_elemento
                print("Elemento actualizado con éxito.")


                print("actualizar numero de patas ")
                if 0 <= indice < len(numero_patas):
                    nuevo_elemento2 = input("Ingrese numero de patas nuevo: ")
                    numero_patas[indice] = nuevo_elemento2
                    print("Elemento actualizado con éxito.")

                    print("actualizar  fecha de vacunacion")
                    if 0 <= indice < len(fecha_vacunacion):
                        nuevo_elemento3 = input("Ingrese fecha de vacunacion nueva: ")
                        fecha_vacunacion[indice] = nuevo_elemento3
                        print("Elemento actualizado con éxito.")

                        print("actualizar tutor")
                        if 0 <= indice < len(tutor):
                            nuevo_elemento4 = input("Ingrese tutor nuevo: ")
                            color[indice] = nuevo_elemento4
                            print("Elemento actualizado con éxito.")
                            if 0 <= indice < len(color):
                                nuevo_elemento5 = input("Ingrese color nuevo:")
                                color[indice] = nuevo_elemento5
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