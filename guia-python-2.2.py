# Saludo
print("Bienvenido al mundo de la programación")
nom = (input("Para comenzar, ingresa tu nombre: "))
def saludar(nom):
    print(f"¡Bienvenido {nom}!")
saludar(nom)


# Ecuación
x = int(input("Ingrese el valor de x: "))
resultado = (x**2 + 3*x + 1) / 4
print(f"El resultado de la ecuación (x^2 + 3x + 1) / 4 con x", x, "es: ", resultado)


# Datos
nombre = input("ingrese su nombre: ")
rut = input("ingrese su RUT: ")
correo = input("ingrese su correo electrónico: ")
telefono = input("ingrese su número telefonico: ")

print(f"NOMBRE:", nombre)
print(f"RUT:", rut)
print(f"CORREO:", correo)
print(f"TELEFONO:", telefono)


# Salto de línea
print("hola mundo \n soy un programador")


# Tabulación
print("Hol\ta \t\t\tsoy un programador")