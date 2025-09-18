def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Conversor de Temperatura")

try:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C es igual a {fahrenheit:.2f}°F")

    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit}°F es igual a {celsius:.2f}°C")

except ValueError:
    print("Por favor ingrese un número válido.")


