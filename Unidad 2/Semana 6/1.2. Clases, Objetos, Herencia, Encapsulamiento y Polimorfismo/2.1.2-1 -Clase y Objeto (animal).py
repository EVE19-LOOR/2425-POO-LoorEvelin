# Clase base: Animal
class Animal:
    def __init__(self, nombre, edad):
        # Encapsulación: atributo privado
        self.__nombre = nombre  # Atributo privado
        self.edad = edad        # Atributo público

    # Método para obtener el nombre (getter)
    def get_nombre(self):
        return self.__nombre

    # Método para establecer el nombre (setter)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Método genérico
    def hacer_sonido(self):
        return "El animal hace un sonido"

# Clase derivada: Perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamar al constructor de la clase base
        super().__init__(nombre, edad)
        self.raza = raza  # Atributo propio de la clase derivada

    # Sobrescritura de método (polimorfismo)
    def hacer_sonido(self):
        return "El perro ladra"

    # Método adicional
    def traer_pelota(self):
        return f"{self.get_nombre()} está trayendo la pelota."

# Clase derivada: Gato
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Llamar al constructor de la clase base
        super().__init__(nombre, edad)
        self.color = color  # Atributo propio de la clase derivada

    # Sobrescritura de método (polimorfismo)
    def hacer_sonido(self):
        return "El gato maúlla"

# Función principal para demostrar la funcionalidad
def main():
    # Crear instancias de las clases
    perro = Perro("Max", 5, "Labrador")
    gato = Gato("Luna", 3, "Gris")

    # Encapsulación: uso de getter y setter
    print(f"Nombre del perro (antes): {perro.get_nombre()}")
    perro.set_nombre("Rocky")
    print(f"Nombre del perro (después): {perro.get_nombre()}")

    # Herencia: usar métodos heredados
    print(f"Edad del perro: {perro.edad}")
    print(f"Edad del gato: {gato.edad}")

    # Polimorfismo: llamar a métodos sobrescritos
    print(perro.hacer_sonido())  # El perro ladra
    print(gato.hacer_sonido())  # El gato maúlla

    # Métodos específicos de las clases derivadas
    print(perro.traer_pelota())

# Ejecutar el programa
if __name__ == "__main__":
    main()

