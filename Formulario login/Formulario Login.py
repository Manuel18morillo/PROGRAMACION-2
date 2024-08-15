import tkinter as tk
from tkinter import *
from PIL import *

ventana = tk.Tk()
ventana.title("Formulario Login")
ventana.resizable(False,False)
ventana.geometry("800x500")

frame_izquierdo = tk.Frame(ventana, bg="#33FFF0")
frame_izquierdo.pack(side="left", fill="both", expand=True)

logo = PhotoImage(file='usuario.png')
logo_a =tk.Label(frame_izquierdo, image=logo, justify="center")
logo_a.pack(fill="both", expand=True)

frame_derecho = tk.Frame(ventana, bg="gray")
frame_derecho.pack(side="right", fill="both", expand=True)

title = tk.Label(frame_derecho, text="LOGIN", font=("Arial", 40), justify="center")
title.pack(pady=20)

usuario = tk.Label(frame_derecho, text="Usuario:", font=("Arial", 12))
usuario.pack()
user = tk.Entry(frame_derecho, font=("Arial", 12), border=2, bg="#33FFF0")
user.pack(pady=5)

clave = tk.Label(frame_derecho, text="Clave:", font=("Arial", 12))
clave.pack()
key = tk.Entry(frame_derecho, show="*", font=("Arial", 12), border=2, bg="#33FFF0")
key.pack(pady=5)

def ingresar():
    usuario = user.get()
    clave = key.get()
    print("Usuario:", usuario)
    print("Clave:", clave)

boton_ingresar = tk.Button(frame_derecho, text="Ingresar", font=("Helvetica", 12), foreground="blue" ,command=ingresar)
boton_ingresar.pack(pady=20)

ventana.mainloop()