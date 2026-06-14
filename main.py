from funciones import registrar_pokemon, eliminar_pokemon, modificar_pokemon, informe_general, reporte_competitivo
from funciones import reporte_estadistico, reporte_matriz, promedio, promedio_victorias_tipo, reporte_por_tipo
from listas import cargar_pokemones
from colorama import init, Fore
init(autoreset= True)

#Funciones para el menú: Emi y Lola
def opciones_menu():
    #formato del titulo
    ancho= 60
    titulo= "SISTEMA DE GESTIÓN: POKÉTRAINER LEAGUE"
    espacios= (ancho - len(titulo))//2
    print("=" * ancho)
    print(espacios * " " + titulo + espacios * " ")
    print("=" * ancho)
    
    #formato del menu
    print(Fore.GREEN + "1. Registrar un Pokémon (Alta)")
    print(Fore.GREEN + "2. Eliminar un Pokémon (Baja)")
    print(Fore.GREEN + "3. Modificar atributos del Pokémon (Modificación)")
    print(Fore.GREEN + "4. Informe General – Visualización de los datos")
    print(Fore.GREEN + "5. Reporte Estadístico General")
    print(Fore.GREEN + "6. Reporte por Tipo de Pokémon")
    print(Fore.GREEN + "7. Reporte Tipo vs Estado")
    print(Fore.GREEN + "8. Reporte Competitivo")
    print(Fore.GREEN + "9. Salir")
       
def ingresar_opcion():
    opcion= input("Seleccione una opción: ").strip()
    #guarda el rango para que las opciones fuera de 1 y 8 no sean validas
    while not opcion.isdigit() or (int(opcion) < 1 or int(opcion) > 9):
                print(Fore.RED + "Error: opción no válida. Inténtelo de nuevo")
                opcion= input("Seleccione otra opcion: ").strip()
    opcion = int(opcion)
    return opcion

#Función del main: Emi y Lola
def main():   
    lst_pokemones = cargar_pokemones()
    opciones_menu()
    opcion = ingresar_opcion()

    while opcion != 9:
        
        #anlisis de opcion
        if opcion == 1:
            print(Fore.GREEN + "REGISTRAR POKEMON")
            print("")
            registrar_pokemon(lst_pokemones)       

        elif opcion == 2:
            print(Fore.GREEN + "ELIMINAR POKEMON")
            print("")
            eliminar_pokemon(lst_pokemones)
          
        elif opcion == 3:
            print(Fore.GREEN + "MODIFICAR POKEMON")
            print("")
            modificar_pokemon(lst_pokemones)
         

        elif opcion == 4:
            print(Fore.GREEN + "VISUALIZACION DE DATOS")
            print("")
            informe_general(lst_pokemones)
        
        elif opcion == 5:
             print(Fore.GREEN + "REPORTE ESTADÍSTICO GENERAL")
             print("")
             reporte_estadistico(lst_pokemones)
        
        elif opcion == 6:
             print(Fore.GREEN + "REPORTE POR TIPO DE POKÉMON")
             print("")
             reporte_por_tipo(lst_pokemones)
        
        elif opcion == 7:
             print(Fore.GREEN + "REPORTE TIPO VS ESTADO")
             print("")
             reporte_matriz(lst_pokemones)

        elif opcion == 8:
             print(Fore.GREEN + "REPORTE COMPETITIVO")
             print("")
             reporte_competitivo(lst_pokemones)   

        
 
        print("")
        opciones_menu()
        opcion = ingresar_opcion()
    print("")            
    print(Fore.GREEN + "EL PROGRAMA HA FINALIZADO")


main()