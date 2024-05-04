usuarios = {
    'pedro': '1234',
    'angel': 'a4s1'
}

username = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

if username in usuarios and usuarios[username] == contraseña:
    print("¡Bienvenido,", username, "!")
else:
    print("Nombre de usuario o contraseña incorrectos.")