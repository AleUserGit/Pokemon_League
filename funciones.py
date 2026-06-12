from colorama import init, Fore


#Funciones de menú : Emilia y Lola
def opciones_menu():
    ancho= 60
    titulo= "SISTEMA DE GESTIÓN: POKÉTRAINER LEAGUE"
    espacios= (ancho - len(titulo))//2
    print("=" * ancho)
    print(espacios * " " + titulo + espacios * " ")
    print("=" * ancho)
    
    print(Fore.GREEN + "1. Registrar un Pokémon (Alta)")
    print(Fore.GREEN + "2. Eliminar un Pokémon (Baja)")
    print(Fore.GREEN + "3. Modificar atributos del Pokémon (Modificación)")
    print(Fore.GREEN + "4. Informe General – Visualización de los datos")
    print(Fore.GREEN + "5. Salir")
    
def ingresar_opcion():
    opcion= input("Seleccione una opción: ").strip()
    while not opcion.isdigit() or (int(opcion) < 1 or int(opcion) > 5):
                print(Fore.RED + "Error: opción no válida. Inténtelo de nuevo")
                opcion= input("Seleccione otra opcion: ").strip()
    opcion = int(opcion)
    return opcion


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
            entrenador = validar_entrenador()
            repite = any(nombre == n[0] and entrenador == n[4] for n in lst_pokemones)
    return nombre, entrenador

def validar_tipo():
    tipos = ["Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Lucha", "Roca", "Fantasma", "Dragón", "Normal"]
    print ("Los tipos disponibles son:", tipos)
    print("")
    tipo = input("Ingrese el tipo del Pokemón: ").strip().capitalize()
    while tipo not in tipos:
        print(Fore.RED + "Error: tipo no válido")
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
        print(Fore.RED + "Error: estado no válido")
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
    for i, p in enumerate(lst_pokemones):
        if p[0].capitalize() == nombre.capitalize():
            indice = i

    if indice == -1:
        print(Fore.RED + "Error: no se encontró el Pokemón", nombre)
    else:
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
            print(Fore.RED + "Error: el Pokemón no se encuentra Liberado")

#Funcion 3 -- modificar : Alejo
def modificar_pokemon(lst_pokemones):
    mod_pokemon = input("Ingrese el Pokemón que desea modificar: ").strip()
    while mod_pokemon == "":
        print(Fore.RED + "Error: valor nulo")
        print("--")
        mod_pokemon = input("Ingrese el Pokemón que desea modificar: ").strip()

    indice = -1
    for i, p in enumerate(lst_pokemones):
        if p[0].capitalize() == mod_pokemon.capitalize():
            indice = i
        
    if indice == -1:
        print(Fore.RED + "Error: no se encontró el Pokemón", mod_pokemon)
    else:
        categoria = ["Nombre", "Tipo", "Nivel", "Poder", "Entrenador", "Victorias", "Estado"]
        print("Los atributos disponibles son:")
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
        else:
            min_poder= p
    promedio_nivel= suma_nivel/cant_pokemones
    promedio_poder= suma_poder/cant_pokemones

    print("La cantidad total de pokemones es:", cant_pokemones)
    print("El nivel promedio es:", promedio_nivel)
    print("El poder promedio es:", promedio_poder)
    print("El total de vistorias es:", suma_victorias)
    #falta promedio de viotorias por pokemon.
    print("El pokemon con mayor poder es:", max_poder[0],"-", max_poder[3])
    print("El pokemon con menor poder es:",min_poder[0],"-", min_poder[3])