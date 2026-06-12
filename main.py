from funciones import opciones_menu, ingresar_opcion
from funciones import registrar_pokemon, eliminar_pokemon, modificar_pokemon, informe_general
from listas import cargar_pokemones

def main():    
    lst_pokemones = cargar_pokemones()
    opciones_menu()
    opcion = ingresar_opcion()

    while opcion != 5:
        
        if opcion == 1:
            print("REGISTRAR POKEMON")
            registrar_pokemon(lst_pokemones)       

        elif opcion == 2:
            print("ELIMINAR POKEMON")
            eliminar_pokemon(lst_pokemones)
          
        elif opcion == 3:
            print("MODIFICAR POKEMON")
            modificar_pokemon(lst_pokemones)
         

        elif opcion == 4:
            print("VISUALIZACION DE DATOS")
            informe_general(lst_pokemones)
        
        opciones_menu()
        opcion = ingresar_opcion()
                
    print("EL PROGRAMA HA FINALIZADO")

main()