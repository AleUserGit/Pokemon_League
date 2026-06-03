# ============================
# MODULO POKEDEX
# Autor: Male y equipo
# ============================

# Listas paralelas

# Usar LISTAS DE LISTAS, no listas paralelas
# O las funciones van a ser imposibles
# Actualizar las categorías

lst_nombre = []
lst_tipo = []
lst_vida = []
lst_ataque = []
lst_entrenador = []
lst_batallas_ganadas =[]
lst_est_comp = []


def cargarPokemon(nombre, tipo, vida, ataque, entrenador, batallas):
    '''
    Guarda un pokemon en las listas paralelas
    '''

    lst_nombre.append(nombre)
    lst_tipo.append(tipo)
    lst_vida.append(vida)
    lst_ataque.append(ataque)
    lst_entrenador.append(entrenador)
    lst_batallas_ganadas.append(batallas)


def cargarPokemonesIniciales():
    '''
    Carga algunos pokemones iniciales
    '''

    cargarPokemon("Bulbasaur", "Planta/Veneno", 45, 49, 49, 45)
    cargarPokemon("Ivysaur", "Planta/Veneno", 60, 62, 63, 60)
    cargarPokemon("Venusaur", "Planta/Veneno", 80, 82, 83, 80)

    cargarPokemon("Charmander", "Fuego", 39, 52, 43, 65)
    cargarPokemon("Charmeleon", "Fuego", 58, 64, 58, 80)
    cargarPokemon("Charizard", "Fuego/Volador", 78, 84, 78, 100)

    cargarPokemon("Squirtle", "Agua", 44, 48, 65, 43)
    cargarPokemon("Wartortle", "Agua", 59, 63, 80, 58)
    cargarPokemon("Blastoise", "Agua", 79, 83, 100, 78)

    cargarPokemon("Pikachu", "Eléctrico", 35, 55, 40, 90)
    cargarPokemon("Raichu", "Eléctrico", 60, 90, 55, 110)

    cargarPokemon("Jigglypuff", "Normal/Hada", 90, 45, 20, 20)
    cargarPokemon("Meowth", "Normal", 40, 45, 35, 90)

    cargarPokemon("Psyduck", "Agua", 50, 52, 48, 55)
    cargarPokemon("Machop", "Lucha", 70, 80, 50, 35)

    cargarPokemon("Geodude", "Roca/Tierra", 40, 80, 100, 20)
    cargarPokemon("Gastly", "Fantasma/Veneno", 30, 35, 30, 80)

    cargarPokemon("Onix", "Roca/Tierra", 35, 45, 160, 70)

    cargarPokemon("Cubone", "Tierra", 50, 50, 95, 35)

    cargarPokemon("Magikarp", "Agua", 20, 10, 55, 80)
    cargarPokemon("Gyarados", "Agua/Volador", 95, 125, 79, 81)

    cargarPokemon("Snorlax", "Normal", 160, 110, 65, 30)

    cargarPokemon("Articuno", "Hielo/Volador", 90, 85, 100, 85)
    cargarPokemon("Zapdos", "Eléctrico/Volador", 90, 90, 85, 100)
    cargarPokemon("Moltres", "Fuego/Volador", 90, 100, 90, 90)

    cargarPokemon("Dratini", "Dragons", 41, 64, 45, 50)
    cargarPokemon("Dragonair", "Dragon", 61, 84, 65, 70)
    cargarPokemon("Dragonite", "Dragon/Volador", 91, 134, 95, 80)

    cargarPokemon("Mewtwo", "Psíquico", 106, 110, 90, 130)
    cargarPokemon("Mew", "Psíquico", 100, 100, 100, 100)


def mostrarPokemones():
    '''
    Muestra todos los pokemones
    '''

    for i in range(len(lst_nombre)):
        print("--------------------------------")
        print("Nombre:", lst_nombre[i])
        print("Tipo:", lst_tipo[i])
        print("Vida:", lst_vida[i])
        print("Ataque:", lst_ataque[i])
        print("Defensa:", lst_defensa[i])
        print("Velocidad:", lst_velocidad[i])