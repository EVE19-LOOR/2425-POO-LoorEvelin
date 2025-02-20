import os

class Producto:
    """
    Representa un producto en el inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

    def to_dict(self):
        """Convierte el producto a un formato de texto para fácil almacenamiento."""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_dict(line):
        """Crea un objeto Producto desde una línea de texto."""
        try:
            id_producto, nombre, cantidad, precio = line.strip().split(",")
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            print("Error: Formato de datos incorrecto en el archivo.")
            return None


class Inventario:
    """
    Maneja la gestión de productos en el inventario y su almacenamiento en archivos.
    """
    ARCHIVO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        if not os.path.exists(self.ARCHIVO):
            print("El archivo no existe. Se creará uno nuevo.")
            open(self.ARCHIVO, 'w').close()  # Crea el archivo si no existe
            return
        try:
            with open(self.ARCHIVO, "r", encoding="utf-8") as file:
                for line in file:
                    producto = Producto.from_dict(line)
                    if producto:
                        self.productos.append(producto)
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("El archivo de inventario no se encontró.")
        except PermissionError:
            print("Error: No tienes permiso para acceder al archivo.")

    def guardar_en_archivo(self):
        """Guarda el inventario en el archivo."""
        try:
            with open(self.ARCHIVO, "w", encoding="utf-8") as file:
                for producto in self.productos:
                    file.write(producto.to_dict())
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No tienes permiso para modificar el archivo.")

    def agregar_producto(self, producto):
        """Añade un nuevo producto al inventario y lo guarda en el archivo."""
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return
        self.productos.append(producto)
        self.guardar_en_archivo()  # Guardar después de agregar
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario y actualiza el archivo."""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_en_archivo()  # Guardar después de eliminar
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto y guarda los cambios."""
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_en_archivo()  # Guardar después de actualizar
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre y devuelve una lista de coincidencias."""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return encontrados if encontrados else None

    def mostrar_productos(self):
        """Muestra todos los productos del inventario."""
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    inventario = Inventario()
    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("Ingrese ID del producto: ")
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad disponible: "))
                precio = float(input("Ingrese precio del producto: "))
                inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            except ValueError:
                print("Error: Ingrese valores válidos para cantidad y precio.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            try:
                inventario.actualizar_producto(
                    id_producto,
                    int(cantidad) if cantidad else None,
                    float(precio) if precio else None
                )
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema de inventario.")
            break
        else:
            print("Opción no válida, intente nuevamente.")


# Ejecutar el menú interactivo
if __name__ == "__main__":
    menu()


