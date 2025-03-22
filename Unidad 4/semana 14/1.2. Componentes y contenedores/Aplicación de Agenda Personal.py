import tkinter as tk
from tkinter import ttk, messagebox


def main():
    root = tk.Tk()
    root.title("Agenda Personal")

    # Frame superior para TreeView
    top_frame = ttk.Frame(root)
    top_frame.pack(pady=20, fill='both', expand=True)

    # TreeView para mostrar eventos
    tree = ttk.Treeview(top_frame, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
    tree.heading('Fecha', text='Fecha')
    tree.heading('Hora', text='Hora')
    tree.heading('Descripción', text='Descripción')
    tree.column('Fecha', width=120)
    tree.column('Hora', width=80)
    tree.pack(side='left', fill='both', expand=True)

    # Scrollbar para TreeView
    scrollbar = ttk.Scrollbar(top_frame, orient='vertical', command=tree.yview)
    scrollbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scrollbar.set)

    # Frame medio para entrada de datos
    mid_frame = ttk.Frame(root)
    mid_frame.pack(pady=10, fill='x')

    # Entrada para fecha
    ttk.Label(mid_frame, text="Fecha (dd/mm/aaaa):").grid(row=0, column=0, padx=5)
    date_entry = ttk.Entry(mid_frame, width=10)
    date_entry.grid(row=0, column=1, padx=5)

    # Entrada para hora
    ttk.Label(mid_frame, text="Hora:").grid(row=0, column=2, padx=5)
    time_entry = ttk.Entry(mid_frame, width=8)
    time_entry.grid(row=0, column=3, padx=5)

    # Entrada para descripción
    ttk.Label(mid_frame, text="Descripción:").grid(row=0, column=4, padx=5)
    desc_entry = ttk.Entry(mid_frame, width=30)
    desc_entry.grid(row=0, column=5, padx=5)

    # Frame inferior para botones
    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=15)

    def add_event():
        fecha = date_entry.get()
        hora = time_entry.get()
        desc = desc_entry.get()

        if not all([fecha, hora, desc]):
            messagebox.showwarning("Campos vacíos", "Complete todos los campos")
            return

        tree.insert('', 'end', values=(fecha, hora, desc))
        date_entry.delete(0, 'end')
        time_entry.delete(0, 'end')
        desc_entry.delete(0, 'end')

    def delete_event():
        selected = tree.focus()
        if not selected:
            messagebox.showinfo("Evento no seleccionado", "Por favor, seleccione un evento")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?"):
            tree.delete(selected)

    # Botones de acción
    ttk.Button(btn_frame, text="Agregar Evento", command=add_event).grid(row=0, column=0, padx=10)
    ttk.Button(btn_frame, text="Eliminar Evento", command=delete_event).grid(row=0, column=1, padx=10)
    ttk.Button(btn_frame, text="Salir", command=root.destroy).grid(row=0, column=2, padx=10)

    root.mainloop()


if __name__ == "__main__":
    main()


