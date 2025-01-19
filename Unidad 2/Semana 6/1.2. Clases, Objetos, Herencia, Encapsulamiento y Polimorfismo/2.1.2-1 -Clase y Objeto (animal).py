# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Este método será diferente para cada tipo de animal
    def hacer_sonido(self):
        pass

# Clase para representar un perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.__raza = raza

    def hacer_sonido(self):
        return "¡Guau!"

    def get_raza(self):
        return self.__raza

# Clase para representar un gato
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.__color = color

    def hacer_sonido(self):
        return "¡Miau!"

    def get_color(self):
        return self.__color

# Función principal para mostrar cómo funciona
def main():
    perro = Perro("Rex", 5, "Labrador")
    gato = Gato("Miau", 3, "Negro")

    print(f"El perro se llama {perro.get_nombre()}, tiene {perro.get_edad()} años y es un {perro.get_raza()}.")
    print(f"Sonido del perro: {perro.hacer_sonido()}")

    print(f"El gato se llama {gato.get_nombre()}, tiene {gato.get_edad()} años y es de color {gato.get_color()}.")
    print(f"Sonido del gato: {gato.hacer_sonido()}")

if __name__ == "__main__":
    main()



