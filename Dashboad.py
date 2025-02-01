import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = { #estas son las rutas de mi proyecto
        '1': 'Unidad 1/Semana 2/1.2.Tecnicas de Programacion/1.2.1. Tecnica de Programacion.py', #Es una cadena que representa la ruta a un archivo llamado
        '2': 'Unidad 1/Semana 3/2.1. Programacion tradicional frente a POO/2.1. Programación Orientada a Objetos (POO).py', #ruta a un archivo sobre programación orientada a objetos
        '3': 'Unidad 1/Semana 4/Ejemplos del Mundo Real y Características de la Programación Orientada a Objetos/sistema de gestión de reservas.py', #ruta a un archivo sobre un sistema de gestión de reservas
        '4': 'Unidad 2/Semana 5/1.1. Tipos de Datos e Identificadores/2.1.1-1 - Nomenclatura en Python.py', #ruta a un archivo sobre nomenclatura en Python
        '5': 'Unidad 2/Semana 6/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-1 -Clase y Objeto (animal).py', #ruta a un archivo sobre clases y objetos en Python, con un ejemplo de un animal
        '6': 'Unidad 2/Semana 7/2.1. Constructores y Destructores/2.2.1-1 - Uso de constructor.py', #ruta a un archivo sobre constructores en Python

        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()