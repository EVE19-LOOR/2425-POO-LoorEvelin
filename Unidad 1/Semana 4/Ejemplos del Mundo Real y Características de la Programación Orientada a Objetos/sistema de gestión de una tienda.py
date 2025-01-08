# Clase que representa un Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"

# Clase que representa un Cliente
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre  # Nombre del cliente
        self.email = email  # Correo electrónico del cliente

    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"

# Clase que representa una Orden
class Orden:
    def __init__(self, cliente):
        self.cliente = cliente  # Cliente que realiza la orden
        self.productos = []  # Lista de productos en la orden

    def agregar_producto(self, producto):
        self.productos.append(producto)  # Agrega un producto a la orden

    def calcular_total(self):
        total = sum(producto.precio for producto in self.productos)  # Suma los precios de los productos
        return total

    def mostrar_detalle(self):
        detalles = [producto.mostrar_info() for producto in self.productos]
        total = self.calcular_total()
        return f"Orden para {self.cliente.mostrar_info()}:\n" + "\n".join(detalles) + f"\nTotal: ${total:.2f}"

# Ejemplo de uso
if __name__ == "__main__":
    cliente1 = Cliente("Ana Gómez", "ana.gomez@example.com")
    producto1 = Producto("Laptop", 1200.00)
    producto2 = Producto("Mouse", 25.50)

    orden1 = Orden(cliente1)
    orden1.agregar_producto(producto1)  # Agregar producto a la orden
    orden1.agregar_producto(producto2)  # Agregar otro producto a la orden

    print(orden1.mostrar_detalle())  # Mostrar detalles de la orden
