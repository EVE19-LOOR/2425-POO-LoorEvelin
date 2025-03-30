import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Lista de Tareas")
        self.tasks = []

        # Configuración de la ventana
        self.root.geometry("700x450")
        self.root.configure(bg="#ffe4e1")  # Fondo rosa pastel

        # Frame superior para el título
        self.title_frame = tk.Frame(self.root, bg="#ffb6c1", height=50)  # Rosa claro
        self.title_frame.pack(fill=tk.X)
        self.title_label = tk.Label(self.title_frame, text="Aplicación de Lista de Tareas", bg="#ffb6c1", fg="white",
                                    font=("Arial", 16))
        self.title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Frame para el campo de entrada y botón de añadir tarea
        self.entry_frame = tk.Frame(self.root, bg="#ffe4e1")
        self.entry_frame.pack(padx=10, pady=10)
        tk.Label(self.entry_frame, text="Nueva Tarea:", bg="#ffe4e1", font=("Arial", 12)).pack(side=tk.LEFT)
        self.task_entry = tk.Entry(self.entry_frame, width=50, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT, padx=10)
        self.add_button = tk.Button(self.entry_frame, text="Añadir Tarea", command=self.add_task, bg="#ff69b4",
                                    fg="white", font=("Arial", 10))  # Botón rosa fuerte
        self.add_button.pack(side=tk.LEFT)

        # Treeview para mostrar las tareas y su estado
        self.tree_frame = tk.Frame(self.root, bg="#ffe4e1")
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.task_tree = ttk.Treeview(self.tree_frame, columns=("Tarea", "Estado"), show="headings",
                                      height=10)  # Reducir el tamaño del Treeview
        self.task_tree.heading("Tarea", text="Tarea")
        self.task_tree.heading("Estado", text="Estado")
        self.task_tree.column("Tarea", width=400)
        self.task_tree.column("Estado", width=100)

        # Scrollbar para el Treeview
        scrollbar = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL, command=self.task_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_tree.configure(yscrollcommand=scrollbar.set)

        self.task_tree.pack(fill=tk.BOTH, expand=True)

        # Frame para los botones de acción
        self.button_frame = tk.Frame(self.root, bg="#ffe4e1")
        self.button_frame.pack(padx=10, pady=10)

        self.complete_button = tk.Button(self.button_frame, text="Marcar como Completada", command=self.complete_task,
                                         bg="#ff1493", fg="white", font=("Arial", 10), width=20)  # Rosa oscuro
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar Tarea", command=self.delete_task, bg="#db7093",
                                       fg="white", font=("Arial", 10), width=15)  # Rosa medio
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append({"task": task, "status": "Pendiente"})
            self.task_tree.insert("", tk.END, values=(task, "Pendiente"))
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def complete_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            for item in selected_item:
                values = self.task_tree.item(item)["values"]
                task_name = values[0]
                status = values[1]

                new_status = "Completada" if status == "Pendiente" else "Pendiente"
                for task in self.tasks:
                    if task["task"] == task_name:
                        task["status"] = new_status

                # Actualizar visualmente en el Treeview
                self.task_tree.item(item, values=(task_name, new_status))
        else:
            messagebox.showinfo("Información", "Por favor selecciona una tarea.")

    def delete_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            for item in selected_item:
                values = self.task_tree.item(item)["values"]
                task_name = values[0]

                # Eliminar de la lista interna
                self.tasks = [task for task in self.tasks if task["task"] != task_name]

                # Eliminar del Treeview
                self.task_tree.delete(item)
        else:
            messagebox.showinfo("Información", "Por favor selecciona una tarea.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
