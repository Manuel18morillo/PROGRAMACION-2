import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
path = Image.open("Manuel.jpg")
#from tkinter import tk, StringVar, Label, Button
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)
ventana.title("My Creavity")

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Establecer el tamaño completo de la ventana
ventana.geometry(f"{900}x{900}")
# Definimos si la ventana puede ser modificada en su tamaño.
ventana.resizable(True, True) 
# Podemos añadir configuraciones adicionales a la ventana con la funcion config
ventana.config(bg="gray")

etiqueta = tk.Label(ventana, text="¡Hola, mundo!", font="Arial", bg="black", fg="blue", width="15" , height="5", anchor="center")
etiqueta.pack()

def cambiar_texto():
    etiqueta.config(text="¡Texto cambiado!")

etiqueta = tk.Label(ventana, text="Texto original")
etiqueta.pack()
# Crear un botón con texto y función de comando
boton1 = tk.Button(ventana, text="Cambiar", command=cambiar_texto)
boton1.pack()

# Crear un botón con colores de fondo y texto personalizados
boton2 = tk.Button(ventana, text="Botón 2", bg="blue", fg="white", font=("Arial", 12))
boton2.pack()

# Crear un botón deshabilitado
boton3 = tk.Button(ventana, text="Deshabilitado", state="disabled")
boton3.pack()

#Agrega texto y obtenerlo
def obtener_texto():
    texto_ingresado = cuadro_texto.get()
    etiqueta.config(text="Texto ingresado: " + texto_ingresado)

etiqueta = tk.Label(ventana, text="Texto ingresado: ")
etiqueta.pack()

cuadro_texto = tk.Entry(ventana, width=30)
cuadro_texto.pack()

boton = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton.pack()

marco1 = tk.Frame(ventana, width=200, height=100, bd=2, relief="solid")
marco1.pack()

# Agregar una etiqueta al marco1
etiqueta1 = tk.Label(marco1, text="Marco 1")
etiqueta1.pack()
etiqueta3 = tk.Label(marco1, text="Marco 1")
etiqueta3.pack()
# Crear un marco con borde en relieve
marco2 = tk.Frame(ventana, width=200, height=100, bd=2, relief="raised")
marco2.pack()

# Agregar una etiqueta al marco2
etiqueta2 = tk.Label(marco2, text="Marco 2")
etiqueta2.pack()

#Cuadro de seleccion
def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        print("Elemento seleccionado:", elemento)

cuadro_lista = tk.Listbox(ventana, width=30, selectmode="multiple"   , background="gray")
cuadro_lista.pack()

elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]

#Casilla Verificacion
for elemento in elementos:
    cuadro_lista.insert(tk.END, elemento)

boton = tk.Button(ventana, text="Obtener", command=obtener_seleccion, background="blue")
boton.pack()

def obtener_estado():
    if variable.get() == 1:
        print("La casilla de verificación está seleccionada")
    else:
        print("La casilla de verificación no está seleccionada")

variable = tk.IntVar()

casilla_verificacion = tk.Checkbutton(ventana, text="Seleccionar", variable=variable, command=obtener_estado)
casilla_verificacion.pack()

#Casillas de seleccion
def obtener_seleccion():
    seleccion = variable.get()
    if seleccion == 11:
        print("Opción 1 seleccionada")
    elif seleccion == 2:
        print("Opción 2 seleccionada")
    elif seleccion == 3:
        print("Opción 3 seleccionada")

opcion11 = tk.Radiobutton(ventana, text="Opción 1", variable=variable, value=11, command=obtener_seleccion)
opcion11.pack()

opcion2 = tk.Radiobutton(ventana, text="Opción 2", variable=variable, value=2, command=obtener_seleccion)
opcion2.pack()

opcion3 = tk.Radiobutton(ventana, text="Opción 3", variable=variable, value=3, command=obtener_seleccion)
opcion3.pack()


#Como mover elementos
ventana.geometry("900x900")

label = tk.Label(ventana, text="Moviendo" , background="Orange", font="Arial")
label.place(x=50, y=50)


boton = tk.Button(ventana, text="Aceptar")
boton.place(x=100, y=100, width=100, height=30)


#Agregando casilla en otra Ventana
master = tk.Tk()
master.geometry("800x600")

# Creacion de labels
l1 = tk.Label(master, text = "Nombre:")
l2 = tk.Label(master, text = "Apellido:")

#Definiendo posiciones 
l1.grid(row = 0, column = 0, pady = 2)
l2.grid(row = 1, column = 0, pady = 2)

# Creando cajas de texto con Entry
nombre = tk.Entry(master)
apellido = tk.Entry(master)

# Definiendo posisicones para cajas de texto
nombre.grid(row = 0, column = 1, pady = 4)
apellido.grid(row = 1, column = 1, pady = 4)

# Inicializamos la aplicacion
ventana.mainloop()