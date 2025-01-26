class Libro:
    def __init__(self, titulo, autor):
        """Este es el constructor de la clase Libro.

        Aquí se inicializan el título y el autor del libro.
        """
        self.titulo = titulo  # Guardamos el título del libro
        self.autor = autor  # Guardamos el autor del libro
        print(f"Se ha creado el libro: '{self.titulo}' por {self.autor}")

    def __del__(self):
        """Este es el destructor de la clase Libro.

        Se llama cuando el libro ya no se necesita.
        Aquí podemos hacer limpieza si es necesario.
        """
        print(f"Se ha destruido el libro: '{self.titulo}' por {self.autor}")


class Biblioteca:
    def __init__(self):
        """Este es el constructor de la clase Biblioteca.

        Inicializa una lista vacía para almacenar libros.
        """
        self.libros = []  # Creamos una lista para los libros
        print("Se ha creado una nueva biblioteca.")

    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca."""
        self.libros.append(libro)  # Añadimos el libro a la lista
        print(f"Se ha agregado a la biblioteca: '{libro.titulo}'")

    def listar_libros(self):
        """Muestra todos los libros en la biblioteca."""
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        print("Libros en la biblioteca:")
        for libro in self.libros:
            print(f"- '{libro.titulo}' por {libro.autor}")

    def __del__(self):
        """Este es el destructor de la clase Biblioteca.

        Se llama cuando la biblioteca ya no se necesita.
        """
        print("Se ha destruido la biblioteca.")


# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una nueva biblioteca
    mi_biblioteca = Biblioteca()

    # Creamos algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

    # Agregamos los libros a la biblioteca
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)

    # Listamos los libros en la biblioteca
    mi_biblioteca.listar_libros()

    # Destruimos los objetos manualmente (opcional)
    del libro1
    del libro2

    # Destruimos la biblioteca
    del mi_biblioteca

