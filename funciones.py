from colorama import init, Fore

#Funciones de validar: Alejo
def validar_nombre(lst_pokemones):
    nombre = input("Ingrese nombre del Pokemón: ").strip().capitalize()
    #Validar que no esté vacío y si se repite
    while nombre == "":
            print("")
            print(Fore.RED + "Error: el nombre no puede estar vacío")
            print("--")
            nombre = input("Ingrese nombre del Pokemón: ").strip().capitalize()
    
    existe = False
    for n in lst_pokemones:
        if nombre == n[0]:
            existe = True
    

    #Si el Pokemón existe, pide dato del entrenador para separar el nuevo del que ya está cargado
    entrenador = ""
    if existe:
        entrenador = validar_entrenador()
        repite = False
        for n in lst_pokemones:
            if nombre == n[0] and entrenador == n[4]:
                repite = True
        while repite:
            print(f"El Pokemón {nombre} ya tiene asignado al entrenador {entrenador}")
            print("--")
            entrenador = validar_entrenador()
            repite = False
            for n in lst_pokemones:
                if nombre == n[0] and entrenador == n[4]:
                    repite = True

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
    #Valida que sea un número y que esté dentro del rango
    while not nivel.isdigit() or (int(nivel) < 1 or int(nivel) > 100):
        print("")
        print(Fore.RED + "Error: Se requiere un número entero entre 1 y 100")
        print("--")
        nivel = input("Ingrese el nivel (1-100) del Pokemón: ").strip()
    nivel = int(nivel)
    return nivel

def validar_poder():
    poder = input("Ingrese el nivel de poder del Pokemón: ").strip()
    #Valida que sea un número y que esté dentro del rango
    while not poder.isdigit() or int(poder) <= 0:
        print("")
        print(Fore.RED + "Error: Ingrese un número entero mayor a 0")
        print("--")
        poder = input("Ingrese el nivel de poder del Pokemón: ").strip()
    poder = int(poder)
    return poder

def validar_entrenador():
    entrenador = input("Ingrese nombre del entrenador: ").strip()
    #Valida que tenga letras o esté vacío
    tiene_letras = False
    for l in entrenador:
        if l.isalpha():
            tiene_letras = True

    while not tiene_letras and entrenador != "":
        print("")
        print(Fore.RED + "Error: nombre no válido")
        print("--")
        entrenador = input("Ingrese nombre del entrenador: ").strip()
        tiene_letras = False
        for l in entrenador:
            if l.isalpha():
                tiene_letras = True
    return entrenador

def validar_victoria():
    victorias = input("Ingrese el número de victorias del Pokemón: ").strip()
    #Valida que sea un número
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
        print(Fore.RED + "Error: estado no válido")
        print("--")
        estado = input("Ingrese el estado del Pokemón: ").strip().capitalize()
    return estado

#Función para Estética al imprimir: Male
def mostrar_pokemon(pokemon):
    # :<15 define que el espacio sea de 15 caracteres
    print("")
    print(f"{'Nombre':<15}"
        f"{'Tipo':<15}"
        f"{'Nivel':<15}"
        f"{'Poder':<15}"
        f"{'Entrenador':<15}"
        f"{'Victorias':<15}"
        f"{'Estado':<15}")
    print("")
    print(f"{pokemon[0]:<15}"
        f"{pokemon[1]:<15}"
        f"{pokemon[2]:<15}"
        f"{pokemon[3]:<15}"
        f"{pokemon[4]:<15}"
        f"{pokemon[5]:<15}"
        f"{pokemon[6]:<15}")
    print("")

# Función Registrar Pokemones : Alejo
def registrar_pokemon(lst_pokemones):
    
    nombre, entrenador = validar_nombre(lst_pokemones)
    tipo = validar_tipo()
    nivel = validar_nivel()
    poder = validar_poder()
    #Verifica si el Pokemón existe
    existe = False
    for n in lst_pokemones:
        if nombre == n[0]:
            existe = True
    #Si el Pokemón no existe y entrenador está vacío, significa que todavía no pidió el dato entrenador
    if entrenador == "" and not existe:
        entrenador = validar_entrenador()
    
    victorias = validar_victoria()
    #Si no se registró un Pokemón, el estado es liberado
    if entrenador == "":
        estado = "Liberado"
    else:
        estado = validar_estado()

    lst_pokemones.append([nombre, tipo, nivel, poder, entrenador, victorias, estado])
    print("Pokemón registrado")

#Función Eliminar Pokemones: Alejo
def eliminar_pokemon(lst_pokemones):
    nombre = input("Ingrese nombre del Pokemón: ").strip()
    while nombre == "":
        print(Fore.RED + "Error: valor nulo")
        print("--")
        nombre = input("Ingrese nombre del Pokemón: ").strip()

    #Asigna un índice al Pokemón, si lo encuentra. Si no lo encuentra, es que no existe
    #También revisa si hay más de un Pokemón
    coincide = 0
    indice = -1
    i = 0
    for p in lst_pokemones:
        if p[0].capitalize() == nombre.capitalize():
            indice = i
            coincide += 1
        i += 1

    if indice == -1:
        print(Fore.RED + "Error: no se encontró el Pokemón", nombre)
    elif coincide == 1:
        if lst_pokemones[indice][6] == "Liberado":
            pokemon= lst_pokemones[indice]
            mostrar_pokemon(pokemon)

            eliminar = input("Desea eliminar el Pokemón? (s/n): ").strip().lower()
            while eliminar != "s" and eliminar != "n":
                print(Fore.RED + "Error: ingrese una respuesta válida")
                print("--")
                eliminar = input("Desea eliminar el Pokemón? (s/n): ").strip().lower()
            if eliminar == "s":
                lst_pokemones.pop(indice)
                print("Se eliminó el Pokemón", nombre)
            else:
                print("Eliminación cancelada. No hubo cambios")
        else:
            print(Fore.RED + "Error: Modifique el estado del Pokemón a Liberado para poder eliminarlo")
    elif coincide > 1:
        print("Hay más de un Pokemón con el nombre", nombre)
        for n in lst_pokemones:
            if n[0].capitalize() == nombre.capitalize():
                print(f"Pokemón: {n[0]} / Entrenador: {n[4]}")

        print("")
        entrenador = validar_entrenador()
        indice = -1
        i = 0
        for p in lst_pokemones:
            if p[0].capitalize() == nombre.capitalize() and p[4].capitalize() == entrenador.capitalize():
               indice = i
            i += 1

        
        while indice == -1:
            print(Fore.RED + f"Error: no se encontró un Pokémon {nombre} cuyo entrenador sea {entrenador}")
            entrenador = validar_entrenador()
            i = 0
            for p in lst_pokemones:
                if p[0].capitalize() == nombre.capitalize() and p[4].capitalize() == entrenador.capitalize():
                    indice = i
                i += 1

        if lst_pokemones[indice][6] == "Liberado":
            pokemon = lst_pokemones[indice]
            mostrar_pokemon(pokemon)

            eliminar = input("Desea eliminar el Pokemón? (s/n): ").strip().lower()
            while eliminar != "s" and eliminar != "n":
                print(Fore.RED + "Error: ingrese una respuesta válida")
                print("--")
                eliminar = input("Desea eliminar el Pokemón? (s/n): ").strip().lower()
            if eliminar == "s":
                lst_pokemones.pop(indice)
                print("Se eliminó el Pokemón", nombre)
            else:
                print("Eliminación cancelada. No hubo cambios")
        else:
            print(Fore.RED + "Error: modifique el estado del Pokemón a Liberado para poder eliminarlo")

    

#Función Modificar Pokemones: Alejo
def modificar_pokemon(lst_pokemones):
    mod_pokemon = input("Ingrese el Pokemón que desea modificar: ").strip()
    while mod_pokemon == "":
        print(Fore.RED + "Error: valor nulo")
        print("--")
        mod_pokemon = input("Ingrese el Pokemón que desea modificar: ").strip()
    
    coincide = 0
    indice = -1
    i = 0
    for p in lst_pokemones:
        if p[0].capitalize() == mod_pokemon.capitalize():
            indice = i
            coincide +=1
        i += 1

    if indice == -1:
        print(Fore.RED + "Error: no se encontró el Pokemón", mod_pokemon)
    elif coincide == 1:
        categoria = ["Nombre", "Tipo", "Nivel", "Poder", "Entrenador", "Victorias", "Estado"]
        print("Los atributos disponibles son:")
        pokemon = lst_pokemones[indice]
        mostrar_pokemon(pokemon)

        
        seguir = input("Desea realizar una modificación en este Pokemón? (s/n): ").strip().lower()
        while seguir != "s" and seguir != "n":
                print("")
                print(Fore.RED + "Error: ingrese una respuesta válida")
                print("--")
                seguir = input("Desea realizar una modificación en este Pokemón? (s/n): ").strip().lower()
        if seguir == "n":
            print("")
            print("No se realizaron modificaciones")
        else:
            while seguir == "s":
                cambiar = input("Ingrese el atributo a modificar: ").strip().capitalize()
                while cambiar not in categoria:
                    print(Fore.RED + "Error: atributo no encontrado")
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
                mostrar_pokemon(pokemon)

                seguir = input("Desea modificar otro atributo? (s/n): ").strip().lower()
                while seguir != "s" and seguir != "n":
                    print("")
                    print(Fore.RED + "Error: ingrese una respuesta válida")
                    print("--")
                    seguir = input("Desea modificar otro atributo? (s/n): ").strip().lower()
                if seguir == "s":
                    print("Confirmado")
                    print("")
                else:
                    print("Se guardaron los cambios")
    else:
        print("Hay más de un Pokemón con el nombre", mod_pokemon)
        for n in lst_pokemones:
            if n[0].capitalize() == mod_pokemon.capitalize():
                print(f"Pokemón: {n[0]} / Entrenador: {n[4]}")

        print("")
        entrenador = validar_entrenador()
        indice = -1
        i = 0
        for p in lst_pokemones:
            if p[0].capitalize() == mod_pokemon.capitalize() and p[4].capitalize() == entrenador.capitalize():
               indice = i
            i += 1
        
        
        while indice == -1:
            print(Fore.RED + f"Error: no se encontró un Pokémon {mod_pokemon} cuyo entrenador sea {entrenador}")
            entrenador = validar_entrenador()
            i = 0
            for p in lst_pokemones:
                if p[0].capitalize() == mod_pokemon.capitalize() and p[4].capitalize() == entrenador.capitalize():
                    indice = i
                i += 1
        
        print("")
        categoria = ["Nombre", "Tipo", "Nivel", "Poder", "Entrenador", "Victorias", "Estado"]
        print("Los atributos disponibles son:")
        pokemon = lst_pokemones[indice]
        mostrar_pokemon(pokemon)
        
        seguir = input("Desea realizar una modificación en este Pokemón? (s/n): ").strip().lower()
        while seguir != "s" and seguir != "n":
                print("")
                print(Fore.RED + "Error: ingrese una respuesta válida")
                print("--")
                seguir = input("Desea realizar una modificación en este Pokemón? (s/n): ").strip().lower()
        if seguir == "n":
            print("")
            print("No se realizaron modificaciones")
        else:
            while seguir == "s":
                cambiar = input("Ingrese el atributo a modificar: ").strip().capitalize()
                while cambiar not in categoria:
                    print(Fore.RED + "Error: atributo no encontrado")
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
                mostrar_pokemon(pokemon)

                seguir = input("Desea modificar otro atributo? (s/n): ").strip().lower()
                while seguir != "s" and seguir != "n":
                    print("")
                    print(Fore.RED + "Error: ingrese una respuesta válida")
                    print("--")
                    seguir = input("Desea modificar otro atributo? (s/n): ").strip().lower()
                if seguir == "s":
                    print("Confirmado")
                    print("")
                else:
                    print("Se guardaron los cambios")



#Función Ordenar los pokemones : Male
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


# Función Visualizar la matriz de Pokemones: Emi y Lola
def informe_general(lst_pokemones):

    if len(lst_pokemones) == 0:
        print(Fore.RED + "Error: No hay Pokémon registrados.")
        return

    #Armamos la tabla, utilizando formatos
    ordenar_pokemones(lst_pokemones)
    print(f"{'Nombre':<15}"
          f"{'Tipo':<15}"
          f"{'Nivel':<15}"
          f"{'Poder':<15}"
          f"{'Entrenador':<15}"
          f"{'Victorias':<15}"
          f"{'Estado':<15}")

    for pokemon in lst_pokemones:
         print(f"{pokemon[0]:<15}"
               f"{pokemon[1]:<15}"
               f"{pokemon[2]:<15}"
               f"{pokemon[3]:<15}"
               f"{pokemon[4]:<15}"
               f"{pokemon[5]:<15}"
               f"{pokemon[6]:<15}")
         
#Función Reporte Estadístico General: Emi y Lola
def reporte_estadistico(lst_pokemones):
    cant_pokemones= len(lst_pokemones)
    
    suma_nivel= 0 
    suma_poder= 0
    suma_victorias= 0
    
    max_poder= lst_pokemones[0]
    min_poder= lst_pokemones[0]
    max_victorias = lst_pokemones[0]
 
   #calcula la suma total para los tres
    for p in lst_pokemones:
        suma_nivel= suma_nivel + p[2]
        suma_poder= suma_poder + p[3]
        suma_victorias= suma_victorias + p[5]
    
        #comparamos el valor del pokemon con los datos que guardamos 
        if p[3] > max_poder[3]:
            max_poder= p
        if p[3] < min_poder[3]:
            min_poder= p
        if p[5] > max_victorias[5]:
            max_victorias = p


    promedio_nivel= suma_nivel/cant_pokemones
    promedio_poder= suma_poder/cant_pokemones

    print(f"Hay un total de {cant_pokemones} Pokemones")
    print("--")
    print("El nivel promedio es:", round(promedio_nivel, 3))
    print("El poder promedio es:", round(promedio_poder, 3))
    print("El total de victorias es:", suma_victorias)
    print("")
    promedio_victorias_tipo(lst_pokemones)
    print("")
    print(f"El Pokemón {max_victorias[0]} tiene la mayor cantidad de victorias ({max_victorias[5]})")
    print(f"El Pokemon {max_poder[0]} tiene el mayor poder ({ max_poder[3]})")
    print(f"El Pokemon {min_poder[0]} tiene el menor poder ({ min_poder[3]})")

#Función Calcular Victorias por tipo: Emi y Lola
def promedio_victorias_tipo(lst_pokemones):

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

    #compara el tipo del pokemon con todos los tipos
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

    #calcula el promedio para cada tipo       
    print("El promedios de victorias de cada uno de los tipos de los pokemones es:")
    print("Fuego:", promedio(victoria_fuego, cant_fuego))
    print("Agua:", promedio(victoria_agua,cant_agua))
    print("Planta:", promedio(victoria_planta,cant_planta))
    print("Electrico:", promedio(victoria_electrico,cant_electrico))
    print("Psiquico:", promedio(victoria_psiquico,cant_psiquico))
    print("Lucha:", promedio(victoria_lucha,cant_lucha))
    print("Roca:", promedio(victoria_roca,cant_roca))
    print("Fantasma:", promedio(victoria_fantasma,cant_fantasma))
    print("Dragón", promedio(victoria_dragon,cant_dragon))
    print("Normal", promedio(victoria_normal,cant_normal))

 
#Función Promedio: Male
def promedio(a, b):
    c = a / b
    c = round(c, 2)
    return c

#Función Reporte Tipo Vs Estado: Alejo
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




#Función Reporte por tipo de Pokemón: Emi y Lola
def reporte_por_tipo(lst_pokemones):
    tipos = ["Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Lucha", "Roca", "Fantasma", "Dragón", "Normal"]
    matriz = []

    #reinicia los contadores para cada tipo
    for t in tipos:
        cant_pokemon = 0
        suma_nvl = 0
        suma_poder = 0
        suma_victorias = 0

        #recorre cada pokemon y compara si el tipo es igaul al tipo del for
        for p in lst_pokemones:
            if p[1] == t:
                cant_pokemon += 1
                suma_nvl += p[2]
                suma_poder += p[3]
                suma_victorias += p[5]
        
        if cant_pokemon > 0:
            promedio_nivel = promedio(suma_nvl, cant_pokemon)
            promedio_poder = promedio(suma_poder, cant_pokemon)
            #guarda los valores del tipo que recorrimos con cada pokemon
            fila = [t, cant_pokemon, promedio_nivel, promedio_poder, suma_victorias]
            matriz.append(fila)
    
    print(f"{'Tipo':<15}{'Cantidad':<15}{'Nivel Prom.':<15}{'Poder Prom.':<15}{'Victorias':<15}")
    for fila in matriz:
        print(f"{fila[0]:<15}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")

    
#Función Pokemones Competitivos: Alejo 
def reporte_competitivo(lst_pokemones):
    suma_nvl = 0
    suma_poder = 0
    for p in lst_pokemones:
        suma_nvl += p[2]
        suma_poder += p[3]

    cant_pokemon = len(lst_pokemones)
    nvl_prom = promedio(suma_nvl, cant_pokemon)
    poder_prom = promedio(suma_poder, cant_pokemon)

    print(f"{'Nombre':<15}{'Tipo':<15}{'Nivel':<15}{'Poder':<15}{'Entrenador':<15}{'Victorias':<15}")
    for p in lst_pokemones:
        if p[2] >= nvl_prom and p[3] >= poder_prom and p[6] == "Disponible":
            print(f"{p[0]:<15}{p[1]:<15}{p[2]:<15}{p[3]:<15}{p[4]:<15}{p[5]:<15}")

