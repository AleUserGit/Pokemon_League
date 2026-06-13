from funciones import registrar_pokemon, eliminar_pokemon, modificar_pokemon, informe_general
from funciones import reporte_estadistico, reporte_matriz
from listas import cargar_pokemones
from colorama import init, Fore
init(autoreset= True)

#Funciones de menú: Emi y Lola
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

#Funciones de menú: Emi y Lola    
def ingresar_opcion():
    opcion= input("Seleccione una opción: ").strip()
    while not opcion.isdigit() or (int(opcion) < 1 or int(opcion) > 5):
                print(Fore.RED + "Error: opción no válida. Inténtelo de nuevo")
                opcion= input("Seleccione otra opcion: ").strip()
    opcion = int(opcion)
    return opcion

#Función main: Emi y Lola
def main():   
    lst_pokemones = cargar_pokemones()
    opciones_menu()
    opcion = ingresar_opcion()

    while opcion != 5:
        
        if opcion == 1:
            print(Fore.GREEN + "REGISTRAR POKEMON" + Fore.RESET)
            registrar_pokemon(lst_pokemones)       

        elif opcion == 2:
            print(Fore.GREEN + "ELIMINAR POKEMON")
            eliminar_pokemon(lst_pokemones)
          
        elif opcion == 3:
            print(Fore.GREEN + "MODIFICAR POKEMON")
            modificar_pokemon(lst_pokemones)
         

        elif opcion == 4:
            print(Fore.GREEN + "VISUALIZACION DE DATOS")
            informe_general(lst_pokemones)
        
        opciones_menu()
        opcion = ingresar_opcion()
                
    print("EL PROGRAMA HA FINALIZADO")


main()

'''
lst_pokemones = cargar_pokemones()
print(reporte_estadistico(lst_pokemones))
reporte_matriz(lst_pokemones)
'''