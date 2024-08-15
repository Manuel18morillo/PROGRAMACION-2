import tkinter as tk
from tkinter import *
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Formulario Tkinter")
ventana.geometry("500x255")
ventana.resizable(True,True)

#ELEMENTOS DEL FORMULARIO
nombre = tk.Label(ventana, text="Nombre")
nombre.grid(row=1, column=1)
name= tk.Entry(ventana, width=30)
name.grid(row=1,column=2)

apellido = tk.Label(ventana, text="Apellido")
apellido.grid(row=2, column=1)
lastname= tk.Entry(ventana, width=30)
lastname.grid(row=2,column=2)

edad = tk.Label(ventana, text="Edad")
edad.grid(row=3, column=1)
age= tk.Entry(ventana, width=30)
age.grid(row=3,column=2)

direccion = tk.Label(ventana, text="Direccion")
direccion.grid(row=4, column=1)
adress= tk.Entry(ventana, width=30)
adress.grid(row=4,column=2)

sexo = tk.Label(ventana, text="Sexo")
sexo.grid(row=5, column=1)
genero = tk.StringVar()

tk.Radiobutton(ventana, text="Masculino", variable=genero, value="Masculino").grid(row=5, column=2)
tk.Radiobutton(ventana, text="Femenino", variable=genero, value="Femenino").grid(row=5, column=3)

city=tk.Label(ventana,text="Ciudad")
city.grid(row=6,column=1)
escogeciudad = tk.StringVar()
ciudades = ["Bogotá", "Medellín", "Barranquilla", "Cartagena"]

listciudad = tk.Listbox(ventana, listvariable=escogeciudad, height=5)
listciudad.grid(row=6, column=2)
for ciudad in ciudades:
    listciudad.insert(tk.END, ciudad)

telefono = tk.Label(ventana,text="Telefono")
telefono.grid(row=7,column=1)
phone=tk.Entry(ventana,width=30)
phone.grid(row=7,column=2)

def registrar():
    ciudad_index = listciudad.curselection()[0]
    ciudad_seleccionada = ciudades[ciudad_index]

    Datos = f"Nombre: {name.get()}\nApellido: {lastname.get()}\nEdad: {age.get()}\nDirección: {adress.get()}\nSexo: {genero.get()}\nTeléfono: {phone.get()}\nCiudad: {ciudad_seleccionada}"
    messagebox.showinfo("Datos Personales", Datos)
    
Registrar= tk.Button(ventana, text="Registrar", command=registrar)
Registrar.grid(row=8,column=2)

ventana.mainloop()