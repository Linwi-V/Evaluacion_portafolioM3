temp = None
while temp is None:
    try:
        temp = int(input("¿Cuál es la temperatura en tu territorio?: "))
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

if temp < 5:
    print("Parka y guantes, hace mucho frío")
elif temp < 15:
    print("Polerón o chaqueta ligera")
else:
    print("Con polera estás bien")
