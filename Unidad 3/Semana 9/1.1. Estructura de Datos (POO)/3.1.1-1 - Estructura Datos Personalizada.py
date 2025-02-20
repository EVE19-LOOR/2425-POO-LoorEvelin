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


class Inventario:
    """
    Maneja la gestión de productos en el inventario.
    """

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return
        self.productos.append(producto)
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return encontrados if encontrados else None

    def mostrar_productos(self):
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
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad disponible: "))
            precio = float(input("Ingrese precio del producto: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)

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
