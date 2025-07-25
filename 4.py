print("Generador de Tablas de Multiplicar")

cantidad = 0
while cantidad <= 0:
    try:
        cantidad = int(input("¿Cuántas tablas de multiplicar deseas ver? (1 o más): "))
        if cantidad <= 0:
            print("Por favor, ingresa un número positivo.")
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

numero_actual = 1

while numero_actual <= cantidad:
    if numero_actual == 5:
        print(f"\n*** Saltando la tabla del {numero_actual} (usando continue) ***")
        numero_actual += 1
        continue  # Salta la tabla del 5 como ejemplo

    if numero_actual == 10:
        print(f"\n*** Deteniendo en la tabla del {numero_actual} (usando break) ***")
        break  # Detiene el programa si llega al 10

    print(f"\nTabla del {numero_actual}:")

    for i in range(1, 11):
        print(f"{numero_actual} x {i} = {numero_actual * i}")

    numero_actual += 1
