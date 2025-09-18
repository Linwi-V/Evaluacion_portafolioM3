import math

def area_circulo(radio):
    return math.pi * radio ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def solicitar_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Por favor, ingresa un valor positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

def menu_areas():
    while True:
        print("\nCalculadora de Áreas")
        print("1. Área de círculo")
        print("2. Área de rectángulo")
        print("3. Área de triángulo")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            radio = solicitar_float("Ingresa el radio del círculo: ")
            print(f"Área del círculo: {area_circulo(radio):.2f}")
        elif opcion == "2":
            base = solicitar_float("Ingresa la base del rectángulo: ")
            altura = solicitar_float("Ingresa la altura: ")
            print(f"Área del rectángulo: {area_rectangulo(base, altura):.2f}")
        elif opcion == "3":
            base = solicitar_float("Ingresa la base del triángulo: ")
            altura = solicitar_float("Ingresa la altura: ")
            print(f"Área del triángulo: {area_triangulo(base, altura):.2f}")
        elif opcion == "4":
            print("Gracias por usar la calculadora de áreas.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu_areas()

