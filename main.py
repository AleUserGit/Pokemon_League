from funciones import opciones_menu, ingresar_opcion
from funciones import registrar_pokemon, eliminar_pokemon, modificar_pokemon, informe_general
from funciones import reporte_estadistico
from listas import cargar_pokemones
from colorama import init, Fore

init(autoreset= True)

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
'''
