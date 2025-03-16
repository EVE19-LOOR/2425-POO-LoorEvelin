import tkinter as tk
from tkinter import messagebox

def convertir_temperatura():
    try:
        celsius = float(entrada.get())
        fahrenheit = (celsius * 9/5) + 32
        area_texto.insert(tk.END, f"{celsius}°C = {fahrenheit:.2f}°F\n")
        entrada.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Ingresa un valor numérico válido")

def limpiar_historial():
    area_texto.delete(1.0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("500x450")

# Menú superior
barra_menu = tk.Menu(ventana)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Salir", command=ventana.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
ventana.config(menu=barra_menu)

# Contenido principal
tk.Label(ventana, text="Conversor Celsius a Fahrenheit", font=("Arial", 14)).pack(pady=10)

frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=15)

tk.Label(frame_entrada, text="Temperatura en Celsius:").pack(side=tk.LEFT)
entrada = tk.Entry(frame_entrada, width=15)
entrada.pack(side=tk.LEFT, padx=10)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Convertir", command=convertir_temperatura).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Limpiar Historial", command=limpiar_historial).pack(side=tk.LEFT, padx=5)

area_texto = tk.Text(ventana, height=15, width=40, wrap=tk.WORD)
area_texto.pack(pady=10)
area_texto.insert(tk.END, "Historial de conversiones:\n" + "="*30 + "\n")

ventana.mainloop()



