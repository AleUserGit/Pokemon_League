from funciones import opciones_menu, ingresar_opcion
from funciones import registrar_pokemon, eliminar_pokemon, modificar_pokemon, informe_general
from listas import lst_pokemones

def main():    
    
    while True:
        
        opciones_menu()
        opcion = ingresar_opcion()


        #analizamos las opciones

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
            
                
        elif opcion == 5:
            print("EL PROGRAMA HA FINALIZADO")
            break
            

main()