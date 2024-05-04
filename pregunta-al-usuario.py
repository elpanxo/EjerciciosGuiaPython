# Pregunta al usuario
print("¿Cuál de los siguientes animales vive en el agua?")
print("a. Perro")
print("b. Cocodrilo")
print("c. Conejo")
print("d. Tiburon")
respuesta = input("Ingresa la letra correspondiente a tu respuesta: ")

puntaje = 0

if respuesta == "b":
    puntaje = 0.5 
elif respuesta == "d":
    puntaje = 1.0 
    
print("Tu puntaje es:", puntaje)


# Pregunta de tema a elección
print("1. ¿A que casa pertenece Harry Potter?")
print("a. Hufflepuff")
print("b. Slytherin")
print("c. Gryffindor")
print("d. Ravenclaw")
respuesta = input("Ingresa la letra correspondiente a tu respuesta: ")

puntaje = 0

if respuesta == "c":
    puntaje = 1.0 

print("Tu puntaje es:", puntaje) 

print("2. ¿Que hechizo sirve para desarmar al rival?")
print("a. Expecto Patronus")
print("b. Expelliarmus")
print("c. Diffindo")
print("d. Wingardium Leviosa")
respuesta = input("Ingresa la letra correspondiente a tu respuesta: ")

puntaje = 0

if respuesta == "b":
    puntaje = 1.0

print("Tu puntaje es:", puntaje)

print("3. ¿Que hechizo uso Harry para derrotar a Voldemort?")
print("a. Expelliarmus")
print("b. Diffindo")
print("c. Crucio")
print("d. Avada Kedavra")
respuesta = input("Ingresa la letra correspondiente a tu respuesta: ")

puntaje = 0

if respuesta == "a":
    puntaje = 1.0 
elif respuesta == "d":
    puntaje = 0.5 

print ("Tu puntaje es:", puntaje)