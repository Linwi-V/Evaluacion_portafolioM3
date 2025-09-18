def mostrar_contactos(agenda):
    if not agenda:
        print("\nLa agenda está vacía.\n")
        return
    print("\nAgenda de Contactos:")
    for nombre, info in agenda.items():
        print(f"{nombre}: Teléfono - {info['telefono']}, Email - {info['email']}")
    print()

def agregar_contacto(agenda):
    nombre = input("Nombre del contacto: ").strip()
    if nombre in agenda:
        print("Este contacto ya existe.\n")
        return
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    agenda[nombre] = {"telefono": telefono, "email": email}
    print("Contacto agregado exitosamente.\n")

def buscar_contacto(agenda):
    nombre = input("Nombre a buscar: ").strip()
    if nombre in agenda:
        contacto = agenda[nombre]
        print(f"{nombre}: Teléfono - {contacto['telefono']}, Email - {contacto['email']}\n")
    else:
        print("Contacto no encontrado.\n")

def menu_agenda():
    agenda = {}
    while True:
        print("1. Agregar contacto")
        print("2. Ver todos los contactos")
        print("3. Buscar contacto")
        print("4. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            mostrar_contactos(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu_agenda()

