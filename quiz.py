def guardar_informacion(nombre, edad, profesion):
    with open("informacion.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Profesión: {profesion}\n")
        archivo.write("=" * 30 + "\n")

def main():
    print("Ingrese su información:")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    profesion = input("Profesión: ")

    guardar_informacion(nombre, edad, profesion)
    print("Información guardada en 'informacion.txt'")

if __name__ == "__main__":
    main()