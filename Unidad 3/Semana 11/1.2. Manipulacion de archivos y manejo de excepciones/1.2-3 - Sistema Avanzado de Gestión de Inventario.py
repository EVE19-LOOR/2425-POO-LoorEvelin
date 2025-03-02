import json
import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado")

    def actualizar_cantidad(self, id, cantidad):
        if id in self.productos:
            self.productos[id].set_cantidad(cantidad)
        else:
            print("Producto no encontrado")

    def actualizar_precio(self, id, precio):
        if id in self.productos:
            self.productos[id].set_precio(precio)
        else:
            print("Producto no encontrado")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.get_nombre().lower() == nombre.lower():
                return producto
        return None

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        print("\nInventario Actual:")
        for id, producto in self.productos.items():
            print(f"{producto}")

    def mostrar_inventario_txt(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        print("\nInventario en formato texto:")
        for id, producto in self.productos.items():
            print(f"{producto}")


def guardar_inventario_json(inventario, archivo):
    try:
        datos = {}
        for id, producto in inventario.productos.items():
            datos[id] = {
                "nombre": producto.get_nombre(),
                "cantidad": producto.get_cantidad(),
                "precio": producto.get_precio()
            }
        with open(archivo, "w") as f:
            json.dump(datos, f)
        print("Inventario guardado en formato JSON correctamente.")
        return True
    except Exception as e:
        print(f"Error al guardar el inventario en formato JSON: {e}")
        return False


def cargar_inventario_json(archivo):
    try:
        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                datos = json.load(f)
            inventario = Inventario()
            for id, producto in datos.items():
                inventario.agregar_producto(Producto(id, producto["nombre"], producto["cantidad"], producto["precio"]))
            return inventario
        else:
            return Inventario()
    except Exception as e:
        print(f"Error al cargar el inventario: {e}")
        return Inventario()


def obtener_input_numerico(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un valor positivo.")
            else:
                return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")


def obtener_input_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un valor positivo.")
            else:
                return valor
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


def main():
    archivo_json = "inventario.json"
    inventario = cargar_inventario_json(archivo_json)

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar producto")
        print("6. Mostrar productos")
        print("7. Ver inventario en formato texto")
        print("8. Salir y guardar")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = obtener_input_entero("Ingrese la cantidad del producto: ")
            precio = obtener_input_numerico("Ingrese el precio del producto: ")
            inventario.agregar_producto(Producto(id, nombre, cantidad, precio))
            print("Producto agregado correctamente.")
        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = obtener_input_entero("Ingrese la nueva cantidad del producto: ")
            inventario.actualizar_cantidad(id, cantidad)
            print("Cantidad actualizada correctamente.")
        elif opcion == "4":
            id = input("Ingrese el ID del producto a actualizar: ")
            precio = obtener_input_numerico("Ingrese el nuevo precio del producto: ")
            inventario.actualizar_precio(id, precio)
            print("Precio actualizado correctamente.")
        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado")
        elif opcion == "6":
            inventario.mostrar_productos()
        elif opcion == "7":
            inventario.mostrar_inventario_txt()
            input("Presione Enter para continuar...")
        elif opcion == "8":
            inventario.mostrar_inventario_txt()
            if guardar_inventario_json(inventario, archivo_json):
                print("Inventario guardado correctamente. Saliendo...")
                break
            else:
                print("No se pudo guardar el inventario. Por favor, revise el archivo.")
        else:
            print("Opción inválida. Por favor, intente nuevamente.")


if __name__ == "__main__":
    main()
