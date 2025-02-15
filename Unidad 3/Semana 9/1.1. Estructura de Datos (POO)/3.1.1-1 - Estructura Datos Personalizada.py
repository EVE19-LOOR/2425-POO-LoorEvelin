class Producto:
    """
    Representa un producto en el inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Args:
        id_producto (str): Identificador único del producto.
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad disponible del producto.
        precio (float): Precio unitario del producto.
        """

    self.id_producto = id_producto
    self.nombre = nombre
    self.cantidad = cantidad
    self.precio = precio

    # Getters
    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    # Setters
    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


