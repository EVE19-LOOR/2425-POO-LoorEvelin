import tkinter as tk
from tkinter import messagebox

# Variable global para rastrear la última tarea seleccionada
last_selected_index = -1


def add_task(event=None):
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")


def mark_completed(event=None):
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)

        # Verifica si ya está marcada como completada
        if "(Tarea completada)" in task:
            messagebox.showinfo("Información", "La tarea ya está marcada como completada.")
            return

        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, f"✔ {task}   (Tarea completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcarla como completada.")


def delete_task(event=None):
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")


def close_app(event=None):
    root.destroy()


def select_task(event=None):
    """Selecciona la siguiente tarea al presionar Ctrl + A."""
    global last_selected_index

    # Obtiene todas las tareas de la lista
    tasks = task_listbox.get(0, tk.END)

    # Verifica si hay tareas en la lista
    if len(tasks) > 0:
        # Incrementa el índice de la tarea seleccionada
        last_selected_index = (last_selected_index + 1) % len(tasks)

        # Limpia cualquier selección anterior
        task_listbox.selection_clear(0, tk.END)

        # Selecciona la nueva tarea
        task_listbox.select_set(last_selected_index)
        task_listbox.activate(last_selected_index)


def focus_entry(event=None):
    """Coloca el cursor en el campo de entrada para escribir."""
    task_entry.focus_set()


# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")
root.configure(bg="#FFD1DC")  # Fondo rosado pastel

# Entrada para nuevas tareas
task_entry = tk.Entry(root, width=40, bg="#FFF0F5")
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)

# Botones
btn_frame = tk.Frame(root, bg="#FFD1DC")
btn_frame.pack()

button_style = {
    "bg": "#FFB6C1",
    "activebackground": "#FF69B4",
    "fg": "black",
    "relief": tk.FLAT,
    "width": 10
}

add_btn = tk.Button(btn_frame, text="Añadir", command=add_task, **button_style)
add_btn.pack(side=tk.LEFT, padx=5)

complete_btn = tk.Button(btn_frame, text="Completar", command=mark_completed, **button_style)
complete_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(btn_frame, text="Eliminar", command=delete_task, **button_style)
delete_btn.pack(side=tk.LEFT, padx=5)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=15, bg="#FFE4E1", fg="black")
task_listbox.pack(pady=10)

# Atajos de teclado
root.bind("<c>", mark_completed)
root.bind("<d>", delete_task)
root.bind("<Delete>", delete_task)
root.bind("<Escape>", close_app)
root.bind("<Control-a>", select_task)  # Ctrl + A para seleccionar la siguiente tarea
root.bind("<Control-e>", focus_entry)  # Ctrl + E para enfocar el campo de entrada

root.mainloop()



