def solicitar_datos():
    nombre = input("Ingresa tu nombre: ")
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            break
        except ValueError:
            print("Por favor, ingresa un número entero para la edad.")
    while True:
        try:
            altura = float(input("Ingresa tu altura en metros: "))
            break
        except ValueError:
            print("Por favor, ingresa un número válido para la altura.")
    instrumento = input("¿Tocas algún instrumento? (si/no): ").strip().lower() == 'si'
    return nombre, edad, altura, instrumento

def mostrar_datos(nombre, edad, altura, instrumento):
    print(f"\nNombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Altura: {altura:.2f} metros")
    print(f"Tocas algún instrumento: {'Sí' if instrumento else 'No'}")

nombre, edad, altura, instrumento = solicitar_datos()
mostrar_datos(nombre, edad, altura, instrumento)
