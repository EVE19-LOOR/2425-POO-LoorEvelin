# Clase que representa un Cliente
class Cliente:
    def __init__(self, nombre, documento):
        self.nombre = nombre  # Nombre del cliente
        self.documento = documento  # Documento de identidad del cliente

    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Documento: {self.documento}"

# Clase que representa una Habitacion
class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación (ej. sencillo, doble)
        self.disponible = True  # Estado de disponibilidad

    def reservar(self):
        if self.disponible:
            self.disponible = False  # Cambia el estado a no disponible
            return True
        return False

    def liberar(self):
        self.disponible = True  # Cambia el estado a disponible

# Clase que representa una Reserva
class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente  # Cliente asociado a la reserva
        self.habitacion = habitacion  # Habitación reservada

    def confirmar_reserva(self):
        if self.habitacion.reservar():
            return f"Reserva confirmada para {self.cliente.mostrar_info()} en habitación {self.habitacion.numero}."
        return "La habitación no está disponible."

# Ejemplo de uso
if __name__ == "__main__":
    cliente1 = Cliente("Juan Pérez", "12345678")
    habitacion1 = Habitacion(101, "Doble")

    reserva1 = Reserva(cliente1, habitacion1)
    print(reserva1.confirmar_reserva())  # Confirmar la reserva
