# from listas import lst_pokemones
#Funcion 1 -- registrar pokemones

def registrar_pokemon(lst_pokemones):
    nombre = input("Ingrese nombre del Pokemón: ").strip()
    while nombre == "":
        print("Error: valor nulo")
        nombre = input("Ingrese nombre del Pokemón").strip()
    
    tipos = ["Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Lucha", "Roca", "Fantasma", "Dragón", "Normal"]
    tipo = input("Ingrese el tipo del Pokemón: ").strip()
    while tipo not in tipos:
        print("Error: tipo no válido")
        tipo = input("Ingrese el tipo del Pokemón").strip()
    
    nivel_valido = False
    while not nivel_valido:
        try:
            nivel = int(input("Ingrese el nivel(1-100) del Pokemón: ")).strip()
            if 1 <= nivel_valido <= 100:
                nivel_valido = True
            else:
                print("Error: nivel no válido")
        except ValueError:
            print("Error: no es un número entero")
    
    poder_valido = False
    while not poder_valido:
        try:
            poder = int(input("Ingrese el poder del Pokemón: ")).strip()
            if poder > 0:
                poder_valido = True
            else:
                print("Error: poder no válido")
        except ValueError:
            print("Error: no es un número entero")
    
    tiene_letras = False
    entrenador = input("Ingrese nombre del entrenador: ").strip()
    tiene_letras = any(l.isalpha() for l in entrenador)
    while not tiene_letras:
        print("Error: nombre no válido")
        entrenador = input("Ingrese nombre del entrenador: ").strip()
        tiene_letras = any(l.isalpha() for l in entrenador)



    lst_pokemones.append(nombre, tipo, nivel, poder, entrenador, victorias, estado)


#Funcion 2 -- eliminar
#Funcion 3 -- modificar
#Funcion 4 -- visualizar
#Funcion 5 -- salir