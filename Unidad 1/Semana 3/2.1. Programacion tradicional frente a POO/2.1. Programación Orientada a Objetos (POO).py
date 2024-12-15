class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        if isinstance(temperatura, (int, float)):
            self.temperaturas.append(temperatura)
        else:
            raise ValueError("La temperatura debe ser un número.")

    def calcular_promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

class ClimaSemanal:
    def __init__(self):
        self.clima_diario = ClimaDiario()

    def ingresar_temperaturas_semanales(self):
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    self.clima_diario.ingresar_temperatura(temp)
                    break
                except ValueError as e:
                    print(e)

    def mostrar_promedio_semanal(self):
        promedio = self.clima_diario.calcular_promedio()
        print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

def main():
    print("Cálculo del promedio semanal del clima utilizando POO")
    clima_semanal = ClimaSemanal()
    clima_semanal.ingresar_temperaturas_semanales()
    clima_semanal.mostrar_promedio_semanal()

if __name__ == "__main__":
    main()
