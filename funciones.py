#Funciones de menú : Emilia y Lola
def opciones_menu():
    print("=" * 40)
    print("MENU".center(40))
    print("=" * 40)
    print("1. Registrar Pokémon (Alta)")
    print("2. Eliminar Pokémon (Baja)")
    print("3. Modificar Pokémon (Modificación)")
    print("4. Informe General – Visualización de los datos")
    print("5. Salir")
    
def ingresar_opcion():
    opcion_valida = False
    while not opcion_valida:
        try:
            opcion= int(input("Seleccione una opcion: ").strip())
            while opcion < 1 or opcion > 5:
                print("La seleccion es invalida. Intentelo de nuevo: ")
                opcion= int(input("Seleccione otra opcion: ").strip())
            if opcion >= 1 or opcion <= 5:
                opcion_valida = True
        except ValueError:
            print("Error: no es un número entero")
        
    return opcion


#Funciones de validación : Alejo
def validar_nombre(lst_pokemones):
    nombre = input("Ingrese nombre del Pokemón: ").strip().capitalize()
    while nombre == "":
        print("Error: valor nulo")
        print("--")
        nombre = input("Ingrese nombre del Pokemón: ").strip().capitalize()
    for n in lst_pokemones:
        if nombre == n[0]:
            print("El Pokemón ya se encuentra registrado")
            return
    return nombre

def validar_tipo():
    tipos = ["Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Lucha", "Roca", "Fantasma", "Dragón", "Normal"]
    print ("Los tipos disponibles son:", tipos)
    print("")
    tipo = input("Ingrese el tipo del Pokemón: ").strip().capitalize()
    while tipo not in tipos:
        print("Error: tipo no válido")
        print("--")
        tipo = input("Ingrese el tipo del Pokemón: ").strip().capitalize()
    return tipo

def validar_nivel():
    nivel_valido = False
    while not nivel_valido:
        try:
            nivel = int(input("Ingrese el nivel (1-100) del Pokemón: ").strip())
            if 1 <= nivel <= 100:
                nivel_valido = True
            else:
                print("Error: nivel no válido")
        except ValueError:
            print("Error: no es un número entero")
    return nivel

def validar_poder():
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
    return poder

def validar_entrenador():
    entrenador = input("Ingrese nombre del entrenador: ").strip()
    tiene_letras = any(l.isalpha() for l in entrenador)
    while not tiene_letras:
        print("Error: nombre no válido")
        print("--")
        entrenador = input("Ingrese nombre del entrenador: ").strip()
        tiene_letras = any(l.isalpha() for l in entrenador)
    return entrenador

def validar_victoria():
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
    return victorias

def validar_estado():
    estado_valido = ["Disponible", "Entrenamiento", "Lesionado", "Liberado"]
    print("Los estados disponibles son:", estado_valido)
    print("")
    estado = input("Ingrese el estado del Pokemón: ").strip().capitalize()
    while estado not in estado_valido:
        print("Error: estado no válido")
        print("--")
        estado = input("Ingrese el estado del Pokemón: ").strip().capitalize()
    return estado

# Función 1 -- registrar pokemones : Alejo

def registrar_pokemon(lst_pokemones):
    
    nombre = validar_nombre(lst_pokemones)
    if nombre is None:
        return
    tipo = validar_tipo()
    nivel = validar_nivel()
    poder = validar_poder()
    entrenador = validar_entrenador()
    victorias = validar_victoria()
    estado = validar_estado()

    lst_pokemones.append([nombre, tipo, nivel, poder, entrenador, victorias, estado])
    print("Pokemón registrado")

#Funcion 2 -- eliminar : Alejo
def eliminar_pokemon(lst_pokemones):
    nombre = input("Ingrese nombre del Pokemón: ").strip()
    while nombre == "":
        print("Error: valor nulo")
        print("--")
        nombre = input("Ingrese nombre del Pokemón: ").strip()

    indice = -1
    for i, p in enumerate(lst_pokemones):
        if p[0].capitalize() == nombre.capitalize():
            indice = i

    if indice == -1:
        print("No se encontró el Pokemón", nombre)
    else:
        if lst_pokemones[indice][6] == "Liberado":
            print(lst_pokemones[indice])
            eliminar = input("Desea eliminar el Pokemón? (s/n): ").strip().lower()
            while eliminar != "s" and eliminar != "n":
                print("Ingrese una respuesta válida")
                print("--")
                eliminar = input("Desea eliminar el Pokemón? (s/n): ").strip().lower()
            if eliminar == "s":
                lst_pokemones.pop(indice)
                print("Se eliminó el Pokemón", nombre)
            else:
                print("Eliminación cancelada. No hubo cambios")
        else:
            print("El Pokemón no se encuentra Liberado")

#Funcion 3 -- modificar : Alejo
def modificar_pokemon(lst_pokemones):
    mod_pokemon = input("Ingrese el Pokemón que desea modificar: ").strip()
    while mod_pokemon == "":
        print("Error: valor nulo")
        print("--")
        mod_pokemon = input("Ingrese el Pokemón que desea modificar: ").strip()

    indice = -1
    for i, p in enumerate(lst_pokemones):
        if p[0].capitalize() == mod_pokemon.capitalize():
            indice = i
        
    if indice == -1:
        print("No se encontró el Pokemón", mod_pokemon)
    else:
        categoria = ["Nombre", "Tipo", "Nivel", "Poder", "Entrenador", "Victorias", "Estado"]
        print("Las categorías disponibles son", categoria)
        print("")
        print(lst_pokemones[indice])
        print("")
        termino = False
        while not termino:
            cambiar = input("Ingrese la categoría a modificar: ").strip().capitalize()
            while cambiar not in categoria:
                print("Categoría no encontrada")
                print("--")
                cambiar = input("Ingrese la categoría a modificar: ").strip().capitalize()
            if cambiar == "Nombre":
                    nombre = validar_nombre(lst_pokemones)
                    if nombre is None:
                        return
                    lst_pokemones[indice][0] = nombre
            elif cambiar == "Tipo":
                tipo = validar_tipo()
                lst_pokemones[indice][1] = tipo
            elif cambiar == "Nivel":
                nivel = validar_nivel()
                lst_pokemones[indice][2] = nivel
            elif cambiar == "Poder":
                poder = validar_poder()
                lst_pokemones[indice][3] = poder
            elif cambiar == "Entrenador":
                entrenador = validar_entrenador()
                lst_pokemones[indice][4] = entrenador
            elif cambiar == "Victorias":
                victorias = validar_victoria()
                lst_pokemones[indice][5] = victorias
            elif cambiar == "Estado":
                estado = validar_estado()
                lst_pokemones[indice][6] = estado
            
            print("")
            print(lst_pokemones[indice])
            print("")
            seguir = input("Desea modificar otra categoría? (s/n): ").strip().lower()
            while seguir != "s" and seguir != "n":
                print("Ingrese una respuesta válida")
                print("--")
                seguir = input("Desea modificar otra categoría? (s/n): ").strip().lower()
            if seguir == "s":
                print("Confirmado")
            else:
                print("Se detuvo la modificación. Se guardaron los cambios")
                termino = True

    


#Funcion 4 -- visualizar : Male
def ordenar_pokemones(lst_pokemones):

    for i in range(len(lst_pokemones)-1):

        for j in range(len(lst_pokemones)-1-i):

            poder_actual = lst_pokemones[j][3]
            poder_siguiente = lst_pokemones[j+1][3]

            nombre_actual = lst_pokemones[j][0]
            nombre_siguiente = lst_pokemones[j+1][0]

            if poder_actual < poder_siguiente:

                aux = lst_pokemones[j]
                lst_pokemones[j] = lst_pokemones[j+1]
                lst_pokemones[j+1] = aux

            elif poder_actual == poder_siguiente:

                if nombre_actual > nombre_siguiente:

                    aux = lst_pokemones[j]
                    lst_pokemones[j] = lst_pokemones[j+1]
                    lst_pokemones[j+1] = aux


def informe_general(lst_pokemones):

    if len(lst_pokemones) == 0:
        print("No hay Pokémon registrados.")
        return

    ordenar_pokemones(lst_pokemones)

    for pokemon in lst_pokemones:

        print("\nNombre:", pokemon[0])
        print("Tipo:", pokemon[1])
        print("Nivel:", pokemon[2])
        print("Poder:", pokemon[3])
        print("Entrenador:", pokemon[4])
        print("Victorias:", pokemon[5])
        print("Estado:", pokemon[6])