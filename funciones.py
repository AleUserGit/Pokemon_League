#Funcion 1 -- registrar pokemones

def registrar_pokemon(lst_pokemones):
    nombre = input("Ingrese nombre del Pokemón: ").strip().capitalize()
    while nombre == "":
        print("Error: valor nulo")
        nombre = input("Ingrese nombre del Pokemón").strip().capitalize()
    
    tipos = ["Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Lucha", "Roca", "Fantasma", "Dragón", "Normal"]
    tipo = input("Ingrese el tipo del Pokemón: ").strip().capitalize()
    while tipo not in tipos:
        print("Error: tipo no válido")
        tipo = input("Ingrese el tipo del Pokemón").strip().capitalize()
    
    nivel_valido = False
    while not nivel_valido:
        try:
            nivel = int(input("Ingrese el nivel(1-100) del Pokemón: ").strip())
            if 1 <= nivel <= 100:
                nivel_valido = True
            else:
                print("Error: nivel no válido")
        except ValueError:
            print("Error: no es un número entero")
    
    poder_valido = False
    while not poder_valido:
        try:
            poder = int(input("Ingrese el poder del Pokemón: ").strip())
            if poder > 0:
                poder_valido = True
            else:
                print("Error: poder no válido")
        except ValueError:
            print("Error: no es un número entero")
    
    entrenador = input("Ingrese nombre del entrenador: ").strip()
    tiene_letras = any(l.isalpha() for l in entrenador)
    while not tiene_letras:
        print("Error: nombre no válido")
        entrenador = input("Ingrese nombre del entrenador: ").strip()
        tiene_letras = any(l.isalpha() for l in entrenador)
    
    victoria_valida = False
    while not victoria_valida:
        try:
            victorias = int(input("Ingrese el número de victorias del Pokemón: ").strip())
            if victorias >= 0:
                victoria_valida = True
            else:
                print("Error: valor no válido")
        except ValueError:
            print("Error: no es un número entero")

    estado_valido = ["Disponible", "Entrenamiento", "Lesionado", "Liberado"]
    estado = input("Ingrese el estado del Pokemón: ").strip().capitalize()
    while estado not in estado_valido:
        print("Error: estado no válido")
        estado = input("Ingrese el estado del Pokemón: ").strip().capitalize()



    lst_pokemones.append([nombre, tipo, nivel, poder, entrenador, victorias, estado])



#Funcion 2 -- eliminar
def eliminar_pokemon(lst_pokemones):
    nombre = input("Ingrese el nombre del Pokemon a eliminar: ").strip()
    '''
    Buscar en la lista
    Si existe y es "liberado" pedir confirmación
        eliminar
    Si no existe
        avisar
    Si existe pero no está liberado
        avisar 
    '''
    

#Funcion 3 -- modificar
#Funcion 4 -- visualizar
#Funcion 5 -- salir