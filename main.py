# from funciones import <nombre funcion>
# Llamar todas las funciones al main antes de arrancar
#el main mas mainioso del mainverso
# lst_pokemones([nombre, tipo, nivel, poder, entrenador, victorias, estado])

from funciones import opciones_menu, ingresar_opcion

        
def main(): 
    print("=" * 40)
    print("MENU".center(40))
    print("=" * 40)
    print(opciones_menu())
    
    #analizamos las opciones
    opcion = ingresar_opcion()
    if opcion == 1:
        print("REGISTRAR POKEMON")
        # registrar_pokemon(lst_pokemones)
    elif opcion == 2:
        print("ELIMINAR POKEMON")
        # eliminar_pokemon(lst_pokemones)
    elif opcion == 3:
        print ("MODIFICAR POKEMON")
        # modificar al fucking pokemon
    elif opcion == 4:
        print ("VISUALIZACION DE DATOS")
        # visualizar a los pokemones
    elif opcion == 5:
        print("Vero aprobanos, besito besito chau chua")
        
main()
