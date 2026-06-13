from colorama import init, Fore

#Funciones de validación : Alejo
def validar_nombre(lst_pokemones):
    nombre = input("Ingrese nombre del Pokemón: ").strip().capitalize()
    while nombre == "":
            print("")
            print(Fore.RED + "Error: el nombre no puede estar vacío")
            print("--")
            nombre = input("Ingrese nombre del Pokemón: ").strip().capitalize()
    
    existe = any(nombre == n[0] for n in lst_pokemones)
    entrenador = ""
    if existe:
        entrenador = validar_entrenador()
        repite = any(nombre == n[0] and entrenador == n[4] for n in lst_pokemones)
        while repite:
            print(f"El Pokemón {nombre} ya tiene asignado al entrenador {entrenador}")
            print("--")
            entrenador = validar_entrenador()
            repite = any(nombre == n[0] and entrenador == n[4] for n in lst_pokemones)
    return nombre, entrenador

def validar_tipo():
    tipos = ["Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Lucha", "Roca", "Fantasma", "Dragón", "Normal"]
    print ("Los tipos disponibles son:", tipos)
    print("")
    tipo = input("Ingrese el tipo del Pokemón: ").strip().capitalize()
    while tipo not in tipos:
        print("")
        print( Fore.RED + "Error: tipo no válido")
        print("--")
        tipo = input("Ingrese el tipo del Pokemón: ").strip().capitalize()
    return tipo

def validar_nivel():
    nivel = input("Ingrese el nivel (1-100) del Pokemón: ").strip()
    while not nivel.isdigit() or (int(nivel) < 1 or int(nivel) > 100):
        print("")
        print(Fore.RED + "Error: Se requiere un número entero entre 1 y 100")
        print("--")
        nivel = input("Ingrese el nivel (1-100) del Pokemón: ").strip()
    nivel = int(nivel)
    return nivel

def validar_poder():
    poder = input("Ingrese el nivel de poder del Pokemón: ").strip()
    while not poder.isdigit() or int(poder) <= 0:
        print("")
        print(Fore.RED + "Error: Ingrese un número entero mayor a 0")
        print("--")
        poder = input("Ingrese el nivel de poder del Pokemón: ").strip()
    poder = int(poder)
    return poder

def validar_entrenador():
    entrenador = input("Ingrese nombre del entrenador: ").strip()
    tiene_letras = any(l.isalpha() for l in entrenador)
    while not tiene_letras and entrenador != "":
        print("")
        print(Fore.RED + "Error: nombre no válido")
        print("--")
        entrenador = input("Ingrese nombre del entrenador: ").strip()
        tiene_letras = any(l.isalpha() for l in entrenador)
    return entrenador

def validar_victoria():
    victorias = input("Ingrese el número de victorias del Pokemón: ").strip()
    while not victorias.isdigit():
        print("")
        print(Fore.RED + "Error: Se requiere un número mayor a cero")
        print("--")
        victorias = input("Ingrese el número de victorias del Pokemón: ").strip()
    victorias = int(victorias)
    return victorias

def validar_estado():
    estado_valido = ["Disponible", "Entrenamiento", "Lesionado", "Liberado"]
    print("Los estados disponibles son:", estado_valido)
    print("")
    estado = input("Ingrese el estado del Pokemón: ").strip().capitalize()
    while estado not in estado_valido:
        print("")
        print("Error: estado no válido")
        print("--")
        estado = input("Ingrese el estado del Pokemón: ").strip().capitalize()
    return estado

# Función 1 -- registrar pokemones : Alejo

def registrar_pokemon(lst_pokemones):
    
    nombre, entrenador = validar_nombre(lst_pokemones)
    tipo = validar_tipo()
    nivel = validar_nivel()
    poder = validar_poder()
    nombre_existe = any(nombre == n[0] for n in lst_pokemones)
    if entrenador == "" and not nombre_existe:
        entrenador = validar_entrenador()
    
    victorias = validar_victoria()
    if entrenador == "":
        estado = "Liberado"
    else:
        estado = validar_estado()

    lst_pokemones.append([nombre, tipo, nivel, poder, entrenador, victorias, estado])
    print("Pokemón registrado")

#Funcion 2 -- eliminar : Alejo
def eliminar_pokemon(lst_pokemones):
    nombre = input("Ingrese nombre del Pokemón: ").strip()
    while nombre == "":
        print(Fore.RED + "Error: valor nulo")
        print("--")
        nombre = input("Ingrese nombre del Pokemón: ").strip()

    indice = -1
    coincide = 0
    for i, p in enumerate(lst_pokemones):
        if p[0].capitalize() == nombre.capitalize():
            indice = i
            coincide += 1

    if indice == -1:
        print("No se encontró el Pokemón", nombre)
    elif coincide == 1:
        if lst_pokemones[indice][6] == "Liberado":
            pokemon= lst_pokemones[indice]
            print("")   
            print(f"{'Nombre':<15}"
                f"{'Tipo':<15}"
                f"{'Nivel':<10}"
                f"{'Poder':<10}"
                f"{'Entrenador':<20}"
                f"{'Victorias':<12}"
                f"{'Estado':<15}")
            print("")
            print(f"{pokemon[0]:<15}"
                f"{pokemon[1]:<15}"
                f"{pokemon[2]:<10}"
                f"{pokemon[3]:<10}"
                f"{pokemon[4]:<20}"
                f"{pokemon[5]:<12}"
                f"{pokemon[6]:<15}")
            print("")

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
    elif coincide > 1:
        print("Hay más de un Pokemón con el nombre", nombre)
        for r in lst_pokemones:
            if r[0].capitalize() == nombre.capitalize():
                print(f"Pokemón: {r[0]} / Entrenador: {r[4]}")

        print("")
        entrenador = input("Ingrese el nombre del entrenador correspondiente: ").strip()
        indice = -1
        for i, p in enumerate(lst_pokemones):
            if p[0].capitalize() == nombre.capitalize() and p[4].capitalize() == entrenador.capitalize():
               indice = i
        
        while indice == -1:
            print(f"No se encontró un Pokémon {nombre} cuyo entrenador sea {entrenador}")
            entrenador = input("Ingrese el entrenador: ").strip().capitalize()
            for i, p in enumerate(lst_pokemones):
                if p[0].capitalize() == nombre.capitalize() and p[4].capitalize() == entrenador.capitalize():
                    indice = i

        if lst_pokemones[indice][6] == "Liberado":
            pokemon= lst_pokemones[indice]
            print("")   
            print(f"{'Nombre':<15}"
                f"{'Tipo':<15}"
                f"{'Nivel':<10}"
                f"{'Poder':<10}"
                f"{'Entrenador':<20}"
                f"{'Victorias':<12}"
                f"{'Estado':<15}")
            print("")
            print(f"{pokemon[0]:<15}"
                f"{pokemon[1]:<15}"
                f"{pokemon[2]:<10}"
                f"{pokemon[3]:<10}"
                f"{pokemon[4]:<20}"
                f"{pokemon[5]:<12}"
                f"{pokemon[6]:<15}")
            print("")

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
        print(Fore.RED + "Error: valor nulo")
        print("--")
        mod_pokemon = input("Ingrese el Pokemón que desea modificar: ").strip()
    
    coincide = 0
    indice = -1
    for i, p in enumerate(lst_pokemones):
        if p[0].capitalize() == mod_pokemon.capitalize():
            indice = i
            coincide +=1

    if indice == -1:
        print("No se encontró el Pokemón", mod_pokemon)
    elif coincide == 1:
        categoria = ["Nombre", "Tipo", "Nivel", "Poder", "Entrenador", "Victorias", "Estado"]
        print("Los atributos disponibles son:")
        pokemon = lst_pokemones[indice]
        print("")   
        print(f"{'Nombre':<15}"
            f"{'Tipo':<15}"
            f"{'Nivel':<10}"
            f"{'Poder':<10}"
            f"{'Entrenador':<20}"
            f"{'Victorias':<12}"
            f"{'Estado':<15}")
        print("")
        print(f"{pokemon[0]:<15}"
            f"{pokemon[1]:<15}"
            f"{pokemon[2]:<10}"
            f"{pokemon[3]:<10}"
            f"{pokemon[4]:<20}"
            f"{pokemon[5]:<12}"
            f"{pokemon[6]:<15}")
        print("")
        
        termino = False
        while not termino:
            cambiar = input("Ingrese el atributo a modificar: ").strip().capitalize()
            while cambiar not in categoria:
                print("Atributo no encontrado")
                print("--")
                cambiar = input("Ingrese el atributo a modificar: ").strip().capitalize()
            if cambiar == "Nombre":
                nombre, entrenador = validar_nombre(lst_pokemones)
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
            
            pokemon= lst_pokemones[indice]
            print("")   
            print(f"{'Nombre':<15}"
                f"{'Tipo':<15}"
                f"{'Nivel':<10}"
                f"{'Poder':<10}"
                f"{'Entrenador':<20}"
                f"{'Victorias':<12}"
                f"{'Estado':<15}")
            print("")
            print(f"{pokemon[0]:<15}"
                f"{pokemon[1]:<15}"
                f"{pokemon[2]:<10}"
                f"{pokemon[3]:<10}"
                f"{pokemon[4]:<20}"
                f"{pokemon[5]:<12}"
                f"{pokemon[6]:<15}")
            print("")
            seguir = input("Desea modificar otro atributo? (s/n): ").strip().lower()
            while seguir != "s" and seguir != "n":
                print("")
                print("Ingrese una respuesta válida")
                print("--")
                seguir = input("Desea modificar otro atributo? (s/n): ").strip().lower()
            if seguir == "s":
                print("Confirmado")
            else:
                print("Se guardaron los cambios")
                termino = True
    else:
        print("Hay más de un Pokemón con el nombre", mod_pokemon)
        for r in lst_pokemones:
            if r[0].capitalize() == mod_pokemon.capitalize():
                print(f"Pokemón: {r[0]} / Entrenador: {r[4]}")

        print("")
        entrenador = input("Ingrese el nombre del entrenador correspondiente: ").strip()
        indice = -1
        for i, p in enumerate(lst_pokemones):
            if p[0].capitalize() == mod_pokemon.capitalize() and p[4].capitalize() == entrenador.capitalize():
               indice = i
        
        while indice == -1:
            print(f"No se encontró un Pokémon {mod_pokemon} cuyo entrenador sea {entrenador}")
            entrenador = input("Ingrese el entrenador: ").strip().capitalize()
            for i, p in enumerate(lst_pokemones):
                if p[0].capitalize() == mod_pokemon.capitalize() and p[4].capitalize() == entrenador.capitalize():
                    indice = i
        
        print("")
        categoria = ["Nombre", "Tipo", "Nivel", "Poder", "Entrenador", "Victorias", "Estado"]
        print("Los atributos disponibles son:")
        pokemon = lst_pokemones[indice]
        print("")   
        print(f"{'Nombre':<15}"
            f"{'Tipo':<15}"
            f"{'Nivel':<10}"
            f"{'Poder':<10}"
            f"{'Entrenador':<20}"
            f"{'Victorias':<12}"
            f"{'Estado':<15}")
        print("")
        print(f"{pokemon[0]:<15}"
            f"{pokemon[1]:<15}"
            f"{pokemon[2]:<10}"
            f"{pokemon[3]:<10}"
            f"{pokemon[4]:<20}"
            f"{pokemon[5]:<12}"
            f"{pokemon[6]:<15}")
        print("")

        
        termino = False
        while not termino:
            cambiar = input("Ingrese el atributo a modificar: ").strip().capitalize()
            while cambiar not in categoria:
                print(Fore.RED + "Error: atributo no encontrado")
                print("--")
                cambiar = input("Ingrese el atributo a modificar: ").strip().capitalize()
            if cambiar == "Nombre":
                nombre = validar_nombre(lst_pokemones)
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
            
            pokemon= lst_pokemones[indice]
            print("")   
            print(f"{'Nombre':<15}"
                f"{'Tipo':<15}"
                f"{'Nivel':<10}"
                f"{'Poder':<10}"
                f"{'Entrenador':<20}"
                f"{'Victorias':<12}"
                f"{'Estado':<15}")
            print("")
            print(f"{pokemon[0]:<15}"
                f"{pokemon[1]:<15}"
                f"{pokemon[2]:<10}"
                f"{pokemon[3]:<10}"
                f"{pokemon[4]:<20}"
                f"{pokemon[5]:<12}"
                f"{pokemon[6]:<15}")
            print("")
            seguir = input("Desea modificar otro atributo? (s/n): ").strip().lower()
            while seguir != "s" and seguir != "n":
                print("")
                print(Fore.RED + "Error: ingrese una respuesta válida")
                print("--")
                seguir = input("Desea modificar otro atributo? (s/n): ").strip().lower()
            if seguir == "s":
                print("Confirmado")
            else:
                print("Se guardaron los cambios")
                termino = True
    


#Funcion para ordenar los pokemones : Male
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


# Función 4 -- visualizar : Emi y Lola
def informe_general(lst_pokemones):

    if len(lst_pokemones) == 0:
        print("No hay Pokémon registrados.")
        return

    ordenar_pokemones(lst_pokemones)
    print(f"{'Nombre':<15}"
          f"{'Tipo':<15}"
          f"{'Nivel':<10}"
          f"{'Poder':<10}"
          f"{'Entrenador':<20}"
          f"{'Victorias':<12}"
          f"{'Estado':<15}")

    for pokemon in lst_pokemones:
         print(f"{pokemon[0]:<15}"
               f"{pokemon[1]:<15}"
               f"{pokemon[2]:<10}"
               f"{pokemon[3]:<10}"
               f"{pokemon[4]:<20}"
               f"{pokemon[5]:<12}"
               f"{pokemon[6]:<15}")
         

def reporte_estadistico(lst_pokemones):
    cant_pokemones= len(lst_pokemones)
    suma_nivel= 0 
    suma_poder= 0
    #esto sirve tmb para hacer el total de las victorias para dividir en los p y el promedio de cada tipo
    suma_victorias= 0
    max_poder= lst_pokemones[0]
    min_poder= lst_pokemones[0]
 
    #p es un pokemon completo de informacion
    for p in lst_pokemones:
        suma_nivel= suma_nivel + p[2]
        suma_poder= suma_poder + p[3]
        suma_victorias= suma_victorias + p[5]
        #print directo hago el promedio de los dos separdo
    
        #en la primera vuelta los dos sun iguales entonces no cambia nada
        if p[3] > max_poder[3]:
            max_poder= p
        if p[3] < min_poder[3]:
            min_poder= p
    promedio_nivel= suma_nivel/cant_pokemones
    promedio_poder= suma_poder/cant_pokemones

    print(f"Hay un total de {cant_pokemones} Pokemones")
    print("El nivel promedio es:", round(promedio_nivel, 3))
    print("El poder promedio es:", round(promedio_poder, 3))
    print("El total de vistorias es:", suma_victorias)
    #falta promedio de viotorias por pokemon.
    print(f"El Pokemon {max_poder[0]} tiene el mayor poder ({ max_poder[3]})")
    print(f"El Pokemon {min_poder[0]} tiene el menor poder ({ min_poder[3]})")

'''
def reporte_tipo(lst_pokemones)

victoria_fuego= 0
victoria_agua= 0
victoria_planta= 0
victoria_electrico= 0
victoria_psiquico= 0
victoria_lucha= 0
victoria_roca= 0
victoria_fantasma= 0
victoria_dragon= 0
victoria_normal= 0

cant_fuego= 0
cant_agua= 0
cant_planta= 0
cant_electrico= 0
cant_psiquico= 0
cant_lucha= 0
cant_roca= 0
cant_fantasma= 0
cant_dragon= 0
cant_normal= 0

for p in lst_pokemones:
    if p[1] == "Fuego":
        victoria_fuego = victoria_fuego + p[5]
        cant_fuego += 1
    elif p[1] == "Agua":
        victoria_agua = victoria_agua + p[5]
        cant_agua += 1
    elif p[1] == "Planta":
        victoria_planta = victoria_planta + p[5]
        cant_planta += 1
    elif p[1] == "Eléctrico":
        victoria_electrico = victoria_electrico + p[5]
        cant_electrico += 1    
    elif p[1] == "Psíquico":
        victoria_psiquico = victoria_psiquico + p[5]
        cant_psiquico += 1
    elif p[1] == "Lucha":
        victoria_lucha= victoria_lucha + p[5]
        cant_lucha += 1
    elif p[1] == "Roca":
        victoria_roca= victoria_roca + p[5]
        cant_roca += 1
    elif p[1] == "Fantasma":
        victoria_fantasma= victoria_fantasma + p[5]
        cant_fantasma += 1
    elif p[1] == "Dragón":
        victoria_dragon= victoria_dragon + p[5]
        cant_dragon += 1
    elif p[1] == "Normal":
        victoria_normal= victoria_normal + p[5]
        cant_normal += 1

#ahora viene la parte de calcular el promedio
        
print("El promedios de victorias de cada uno de los tipos de los pokemones es:")
print("Fuego:", round(victoria_fuego/cant_fuego,2))
print("Agua:", round(victoria_agua/cant_agua,2))
print("Planta:", round(victoria_planta/cant_planta,2))
print("Electrico:", round(victoria_electrico/cant_electrico,2))
print("Psiquico:", round(victoria_psiquico/cant_psiquico,2))
print("Lucha:", round(victoria_lucha/cant_lucha,2))
print("Roca:", round(victoria_roca/cant_roca,2))
print("Fantasma:", round(victoria_fantasma/cant_fantasma,2))
print("Dragón", round(victoria_dragon/cant_dragon,2))
print("Normal", round(victoria_normal/cant_normal,2))
print("Normal", round(promedio(victoria_normal, cant_normal),2))

''' 
def promedio(a, b):
    c = a / b
    return c


def reporte_matriz(lst_pokemones):
    tipos = ["Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Lucha", "Roca", "Fantasma", "Dragón", "Normal"]
    estados = ["Disponible", "Entrenamiento", "Lesionado", "Liberado"]
    matriz = []
    

    for t in tipos:
        fila = [0, 0, 0, 0]
        matriz.append(fila)

    for p in lst_pokemones:
        #Recorre cada tipo, buscando coincidencias para p[1] / tipo:
        indice = 0
        for t in tipos:
            if t == p[1]:
                fila = indice
            indice +=1

        #Recorre cada estado, buscando coincidencias para p[1] / tipo:
        indice = 0
        for e in estados:
            if e == p[6]:
                columna = indice    
            indice += 1

        #Suma 1 a la fila y columna que corresponda en la matriz:
        matriz[fila][columna] += 1

    print(f"{'Tipo': <12}", end ="")
    for e in estados:
        print(f"{e: <12}", end = "")
    print("Total")
    
    fila = 0
    for t in tipos:
        total = 0
        print(f"{t: <12}", end= "")
        columna = 0
        for e in estados:
            print(f"{matriz[fila][columna]: <15}", end="")
            total += matriz[fila][columna]
            columna += 1
        print(total)
        fila += 1