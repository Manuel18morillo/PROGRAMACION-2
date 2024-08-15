import matplotlib 
matplotlib.use('TkAgg')
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from collections import deque

class Proceso:
    def __init__(self, nombre, llegada, rafaga):
        self.nombre = nombre
        self.llegada = llegada
        self.rafaga = rafaga
        self.rafaga_restante = rafaga
        self.tiempo_espera = 0
        self.tiempo_respuesta = 0

def fifo(procesos):
    procesos.sort(key=lambda x: x.llegada)
    tiempo_actual = 0
    tiempo_espera_total = 0
    tiempo_respuesta_total = 0

    # Graficar ráfaga de CPU
    fig, ax = plt.subplots(figsize=(10, 5))
    y_labels = [proceso.nombre for proceso in procesos]
    y_ticks = range(len(procesos))

    for i, proceso in enumerate(procesos):
        inicio = tiempo_actual
        duracion = proceso.rafaga
        ax.broken_barh([(inicio, duracion)], (i - 0.4, 0.8), facecolors='orange', edgecolors='orange')
        tiempo_actual += duracion

    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)
    ax.set_xlabel('Ráfaga de CPU')
    ax.set_ylabel('Procesos')
    ax.set_title('Gráfico de Ráfaga de CPU')

    plt.show()

    resultado_texto = "Proceso\t Llegada\tRáfaga\tT Espera\tT Respuesta\n"
    tiempo_actual = 0 
    for i, proceso in enumerate(procesos):
        if i == 0:
            tiempo_espera = 0
        else:
            tiempo_espera = tiempo_actual - proceso.llegada
            if tiempo_espera < 0:
                tiempo_espera = 0

        tiempo_respuesta = tiempo_espera + proceso.rafaga
        tiempo_espera_total += tiempo_espera
        tiempo_respuesta_total += tiempo_respuesta

        resultado_texto += f"{proceso.nombre}\t{proceso.llegada}\t{proceso.rafaga}\t{tiempo_espera}\t{tiempo_respuesta}\n"

        tiempo_actual += proceso.rafaga

    tiempo_promedio_espera = tiempo_espera_total / len(procesos)
    tiempo_promedio_respuesta = tiempo_respuesta_total / len(procesos)

    resultado_texto += f"\nTiempo promedio de espera: {tiempo_promedio_espera}\n"
    resultado_texto += f"Tiempo promedio de respuesta: {tiempo_promedio_respuesta}"

    # Mostrar resultados en una ventana emergente
    messagebox.showinfo("Resultados FIFO", resultado_texto)

def sjf(procesos):
    procesos.sort(key=lambda x: x.llegada)
    tiempo_actual = 0
    tiempo_espera_total = 0
    tiempo_respuesta_total = 0
    proceso_ejecutado = []

    # Graficar ráfaga de CPU
    fig, ax = plt.subplots(figsize=(10, 5))
    y_labels = [proceso.nombre for proceso in procesos]
    y_ticks = range(len(procesos))

    while len(proceso_ejecutado) < len(procesos):
        # Filtrar procesos que han llegado hasta el tiempo actual
        procesos_disponibles = [proceso for proceso in procesos if proceso.llegada <= tiempo_actual and proceso not in proceso_ejecutado]

        if len(procesos_disponibles) == 0:
            tiempo_actual += 1
            continue

        # Elegir el proceso con la ráfaga más corta
        proceso_actual = min(procesos_disponibles, key=lambda x: x.rafaga)
        proceso_ejecutado.append(proceso_actual)

        inicio = tiempo_actual
        duracion = proceso_actual.rafaga
        ax.broken_barh([(inicio, duracion)], (len(proceso_ejecutado) - 1 - 0.4, 0.8), facecolors='blue', edgecolors='blue')

        tiempo_espera = tiempo_actual - proceso_actual.llegada
        if tiempo_espera < 0:
            tiempo_espera = 0

        tiempo_respuesta = tiempo_espera + proceso_actual.rafaga
        tiempo_espera_total += tiempo_espera
        tiempo_respuesta_total += tiempo_respuesta

        tiempo_actual += proceso_actual.rafaga

    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)
    ax.set_xlabel('Ráfaga de CPU')
    ax.set_ylabel('Procesos')
    ax.set_title('Gráfico de Ráfaga de CPU')

    plt.show()

    resultado_texto = "Proceso\tT Llegada\tRáfaga\tT Espera\tT Respuesta\n"
    tiempo_actual = 0 
    for proceso in proceso_ejecutado:
        tiempo_espera = tiempo_actual - proceso.llegada
        if tiempo_espera < 0:
            tiempo_espera = 0

        tiempo_respuesta = tiempo_espera + proceso.rafaga

        resultado_texto += f"{proceso.nombre}\t{proceso.llegada}\t\t{proceso.rafaga}\t{tiempo_espera}\t{tiempo_respuesta}\n"

        tiempo_actual += proceso.rafaga

    tiempo_promedio_espera = tiempo_espera_total / len(procesos)
    tiempo_promedio_respuesta = tiempo_respuesta_total / len(procesos)

    resultado_texto += f"\nTiempo promedio de espera: {tiempo_promedio_espera:.1f}\n"
    resultado_texto += f"Tiempo promedio de respuesta: {tiempo_promedio_respuesta:.1f}"

    # Mostrar resultados en una ventana emergente
    messagebox.showinfo("Resultados SJF", resultado_texto)
    
def round_robin(procesos, quantum):
    # Ordenar los procesos por tiempo de llegada
    procesos.sort(key=lambda x: x.llegada)
    tiempo_actual = 0
    tiempo_espera_total = 0
    tiempo_retorno_total = 0
    cola = deque(procesos)
    eventos = []

    # Crear el gráfico de Gantt
    fig, gnt = plt.subplots()

    # Configurar el gráfico de Gantt
    gnt.set_xlabel('Tiempo')
    gnt.set_ylabel('Procesos')
    gnt.set_yticks([i + 1 for i in range(len(procesos))])
    gnt.set_yticklabels([proceso.nombre for proceso in procesos])
    gnt.grid(True)

    # Texto de resultados
    resultado_texto = "Proceso\tT Llegada\tRáfaga\tT Espera\tT Respuesta\n"

    while cola:
        proceso_actual = cola.popleft()

        if proceso_actual.rafaga_restante > quantum:
            eventos.append((proceso_actual.nombre, tiempo_actual, quantum))
            tiempo_actual += quantum
            proceso_actual.rafaga_restante -= quantum

            # Reinsertar el proceso en la cola si aún tiene tiempo restante
            cola.append(proceso_actual)
        else:
            eventos.append((proceso_actual.nombre, tiempo_actual, proceso_actual.rafaga_restante))
            tiempo_actual += proceso_actual.rafaga_restante
            proceso_actual.tiempo_espera = tiempo_actual - proceso_actual.llegada - proceso_actual.rafaga
            proceso_actual.tiempo_respuesta = tiempo_actual - proceso_actual.llegada
            tiempo_espera_total += proceso_actual.tiempo_espera
            tiempo_retorno_total += proceso_actual.tiempo_respuesta
            proceso_actual.rafaga_restante = 0

        # Actualizar el texto de resultados
        resultado_texto += f"{proceso_actual.nombre}\t{proceso_actual.llegada}\t\t{proceso_actual.rafaga}\t{proceso_actual.tiempo_espera}\t{proceso_actual.tiempo_respuesta}\n"

    tiempo_promedio_espera = tiempo_espera_total / len(procesos)
    tiempo_promedio_retorno = tiempo_retorno_total / len(procesos)

    resultado_texto += f"\nTiempo promedio de espera: {tiempo_promedio_espera:.1f}\n"
    resultado_texto += f"Tiempo promedio de respuesta: {tiempo_promedio_retorno:.1f}"

    # Añadir barras de tiempo al gráfico de Gantt
    for evento in eventos:
        nombre_proceso, inicio, duracion = evento
        y_index = next(i + 1 for i, proceso in enumerate(procesos) if proceso.nombre == nombre_proceso)
        gnt.broken_barh([(inicio, duracion)], (y_index - 0.4, 0.8), facecolors=('green'))

    plt.title('Gráfico Ráfaga CPU')
    plt.show()

    # Mostrar los resultados en un messagebox normal
    messagebox.showinfo("Resultados Round Robin", resultado_texto)

def ejecutar_algoritmo():
    algoritmo_seleccionado = algoritmo_var.get()
    
    procesos = []
    for i in range(len(entries_procesos)):
        nombre = entries_procesos[i][0].get()
        llegada = int(entries_procesos[i][1].get())
        rafaga = int(entries_procesos[i][2].get())
        procesos.append(Proceso(nombre, llegada, rafaga))

    if algoritmo_seleccionado == "FIFO":
        fifo(procesos)
    elif algoritmo_seleccionado == "SJF":
        sjf(procesos)  
    elif algoritmo_seleccionado == "Round Robin":
        quantum = int(quantum_entry.get())
        round_robin(procesos, quantum)  

# Crear ventana principal
root = tk.Tk()
root.title("Planificación de Procesos")
root.geometry("800x400")

# Crear y configurar marco para procesos
frame_procesos = tk.Frame(root)
frame_procesos.pack(padx=10, pady=10)

# Etiqueta y variable para seleccionar el algoritmo
algoritmo_label = tk.Label(root, text="Seleccione el algoritmo de planificación:")
algoritmo_label.pack()

algoritmo_var = tk.StringVar(root)
algoritmo_var.set("FIFO")  # Valor predeterminado

algoritmo_option_menu = tk.OptionMenu(root, algoritmo_var, "FIFO", "SJF", "Round Robin")
algoritmo_option_menu.pack()

def agregar_proceso():
    global contador_procesos
    nombre_label = tk.Label(frame_procesos, text=f"Proceso {contador_procesos + 1}:")
    nombre_label.grid(row=contador_procesos + 1, column=0, padx=5, pady=5)

    nombre_entry = tk.Entry(frame_procesos)
    nombre_entry.grid(row=contador_procesos + 1, column=1, padx=5, pady=5)

    llegada_label = tk.Label(frame_procesos, text="Tiempo de llegada:")
    llegada_label.grid(row=contador_procesos + 1, column=2, padx=5, pady=5)

    llegada_entry = tk.Entry(frame_procesos)
    llegada_entry.grid(row=contador_procesos + 1, column=3, padx=5, pady=5)

    rafaga_label = tk.Label(frame_procesos, text="Ráfaga de CPU:")
    rafaga_label.grid(row=contador_procesos + 1, column=4, padx=5, pady=5)

    rafaga_entry = tk.Entry(frame_procesos)
    rafaga_entry.grid(row=contador_procesos + 1, column=5, padx=5, pady=5)

    entries_procesos.append((nombre_entry, llegada_entry, rafaga_entry))
    contador_procesos += 1

# Etiqueta y entrada para el quantum (para Round Robin)
quantum_label = tk.Label(root, text="Quantum (Usar Solo En Round Robin):")
quantum_label.pack()

quantum_entry = tk.Entry(root)
quantum_entry.pack()
    
# Botón para agregar procesos
contador_procesos = 0
entries_procesos = []
agregar_proceso_btn = tk.Button(root, text="Agregar Proceso", command=agregar_proceso)
agregar_proceso_btn.pack(pady=5)

# Botón para ejecutar el algoritmo seleccionado
ejecutar_btn = tk.Button(root, text="Ejecutar Algoritmo", command=ejecutar_algoritmo)
ejecutar_btn.pack(pady=5)

root.mainloop()