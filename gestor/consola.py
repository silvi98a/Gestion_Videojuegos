def mostrar_menu():
    print("---Menú Videojuegos---")
    print("1. Listar videojuegos")
    print("2. Buscar por título (exacto)")
    print("3. Buscar por título (parcial)")
    print("4. Filtrar por género")
    print("5. Filtrar por rango de años")
    print("6. Añadir videojuego")
    print("7. Modificar videojuego")
    print("8. Eliminar videojuego")
    print("9. Estadísticas")
    print("0. Salir")

def ejecutar_menu(catalogo):
    repetir = True
    while repetir == True:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opción: ")) 
        except ValueError:
            print("Error, introduce un número")
            continue
        match opcion:
            case 1: 
                print("Has elegido listar")       
            case 2:
                print("Has elegido buscar exacto")
            case 3: 
                print("Has elegido buscar parcial")
            case 4:
                print("Has elegido filtrar por género")
            case 5: 
                print("Has elegido filtrar por años")
            case 6:
                print("Has elegido añadir")
            case 7: 
                print("Has elegido modificar")
            case 8:
                print("Has elegido eliminar")
            case 9:
                print("Has elegido estadísticas")
            case 0:
                print("Programa terminado")
                repetir = False
            case _:
                print("Opción no válida")


if __name__ == "__main__":
    ejecutar_menu({})