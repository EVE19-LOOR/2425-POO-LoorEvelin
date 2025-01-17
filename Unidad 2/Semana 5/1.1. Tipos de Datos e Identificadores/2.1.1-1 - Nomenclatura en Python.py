# Este programa calcula el área de un rectángulo y convierte entre metros y centímetros.
# Se utilizan diferentes tipos de datos y se siguen las convenciones de nomenclatura.

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo dado su base y altura.

    :param base: La base del rectángulo (en metros).
    :param altura: La altura del rectángulo (en metros).
    :return: El área del rectángulo (en metros cuadrados).
    """
    return base * altura


def convertir_a_centimetros(metros: float) -> float:
    """
    Convierte una medida de metros a centímetros.

    :param metros: La medida en metros.
    :return: La medida convertida a centímetros.
    """
    return metros * 100


def main():
    # Solicitar al usuario la base y altura del rectángulo
    base_rectangulo = float(input("Ingrese la base del rectángulo en metros: "))
    altura_rectangulo = float(input("Ingrese la altura del rectángulo en metros: "))

    # Calcular el área
    area = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

    # Convertir el área a centímetros cuadrados
    area_cm2 = convertir_a_centimetros(area)

    # Mostrar los resultados
    print(f"El área del rectángulo es: {area} m²")
    print(f"El área del rectángulo en centímetros cuadrados es: {area_cm2} cm²")


# Ejecutar el programa
if __name__ == "__main__":
    main()
