import json


class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalles = (autor, titulo)  # Tupla para autor y título (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def to_dict(self):
        return {"titulo": self.detalles[1], "autor": self.detalles[0], "categoria": self.categoria, "isbn": self.isbn}

    @staticmethod
    def from_dict(data):
        return Libro(data["titulo"], data["autor"], data["categoria"], data["isbn"])

    def __str__(self):
        return f"{self.detalles[1]} por {self.detalles[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def to_dict(self):
        return {"nombre": self.nombre, "user_id": self.user_id,
                "libros_prestados": [libro.to_dict() for libro in self.libros_prestados]}

    @staticmethod
    def from_dict(data):
        usuario = Usuario(data["nombre"], data["user_id"])
        usuario.libros_prestados = [Libro.from_dict(libro) for libro in data["libros_prestados"]]
        return usuario

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros Prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.cargar_datos()

    def guardar_datos(self):
        datos = {
            "libros": {isbn: libro.to_dict() for isbn, libro in self.libros.items()},
            "usuarios": {user_id: usuario.to_dict() for user_id, usuario in self.usuarios.items()}
        }
        try:
            with open("biblioteca.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_datos(self):
        try:
            with open("biblioteca.json", "r") as archivo:
                datos = json.load(archivo)
                self.libros = {isbn: Libro.from_dict(libro) for isbn, libro in datos["libros"].items()}
                self.usuarios = {user_id: Usuario.from_dict(usuario) for user_id, usuario in datos["usuarios"].items()}
        except FileNotFoundError:
            print("No se encontró el archivo de datos, creando uno nuevo.")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_datos()

    def mostrar_libros(self):
        for libro in self.libros.values():
            print(libro)

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros.pop(isbn)  # Elimina el libro del diccionario de libros
            usuario.libros_prestados.append(libro)
            self.guardar_datos()
            print(f"Libro '{libro}' prestado a {usuario.nombre}.")
        else:
            print("Error: Libro o usuario no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro  # Devuelve el libro al diccionario
                    self.guardar_datos()
                    print(f"Libro '{libro}' devuelto por {usuario.nombre}.")
                    return
            print("Error: El libro no estaba prestado a este usuario.")
        else:
            print("Error: Usuario no encontrado.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_datos()

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.user_id] = usuario
        self.guardar_datos()

    def mostrar_usuarios(self):
        for usuario in self.usuarios.values():
            print(usuario)

    def eliminar_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.guardar_datos()

    def buscar_libro(self, **kwargs):
        for libro in self.libros.values():
            if ('titulo' in kwargs and kwargs['titulo'].lower() in libro.detalles[1].lower()) or \
                    ('autor' in kwargs and kwargs['autor'].lower() in libro.detalles[0].lower()) or \
                    ('categoria' in kwargs and kwargs['categoria'].lower() == libro.categoria.lower()):
                print(libro)

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                print(libro)


biblioteca = Biblioteca()

while True:
    print("\n=== Sistema de Gestión de Biblioteca Digital ===")
    print("1. Añadir Libro")
    print("2. Mostrar Libros")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Quitar Libro")
    print("6. Registrar Usuario")
    print("7. Mostrar Usuarios")
    print("8. Eliminar Usuario")
    print("9. Buscar Libro por Título")
    print("10. Buscar Libro por Autor")
    print("11. Buscar Libro por Categoría")
    print("12. Listar Libros Prestados de un Usuario")
    print("13. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "13":
        biblioteca.guardar_datos()
        break
    elif opcion == "1":
        # Añadir libro
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        isbn = input("ISBN: ")
        libro = Libro(titulo, autor, categoria, isbn)
        biblioteca.agregar_libro(libro)
    elif opcion == "2":
        biblioteca.mostrar_libros()
    elif opcion == "3":
        user_id = input("ID de Usuario: ")
        isbn = input("ISBN del libro: ")
        biblioteca.prestar_libro(user_id, isbn)
    elif opcion == "4":
        user_id = input("ID de Usuario: ")
        isbn = input("ISBN del libro: ")
        biblioteca.devolver_libro(user_id, isbn)
    elif opcion == "5":
        isbn = input("ISBN del libro a quitar: ")
        biblioteca.eliminar_libro(isbn)
    elif opcion == "6":
        nombre = input("Nombre de Usuario: ")
        user_id = input("ID de Usuario: ")
        usuario = Usuario(nombre, user_id)
        biblioteca.registrar_usuario(usuario)
    elif opcion == "7":
        biblioteca.mostrar_usuarios()
    elif opcion == "8":
        user_id = input("ID de Usuario a eliminar: ")
        biblioteca.eliminar_usuario(user_id)
    elif opcion == "9":
        titulo = input("Título a buscar: ")
        biblioteca.buscar_libro(titulo=titulo)
    elif opcion == "10":
        autor = input("Autor a buscar: ")
        biblioteca.buscar_libro(autor=autor)
    elif opcion == "11":
        categoria = input("Categoría a buscar: ")
        biblioteca.buscar_libro(categoria=categoria)
    elif opcion == "12":
        user_id = input("ID de Usuario: ")
        biblioteca.listar_libros_prestados(user_id)

