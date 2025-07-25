import math

def area_circulo(radio):
    return math.pi * radio ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def menu_areas():
    while True:
        print("\nCalculadora de Áreas")
        print("1. Área de círculo")
        print("2. Área de rectángulo")
        print("3. Área de triángulo")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            radio = float(input("Ingresa el radio del círculo: "))
            print(f"Área del círculo: {area_circulo(radio):.2f}")
        elif opcion == "2":
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura: "))
            print(f"Área del rectángulo: {area_rectangulo(base, altura):.2f}")
        elif opcion == "3":
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura: "))
            print(f"Área del triángulo: {area_triangulo(base, altura):.2f}")
        elif opcion == "4":
            print("Gracias por usar la calculadora de áreas.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_areas()
