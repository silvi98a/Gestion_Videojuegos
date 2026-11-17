from gestor import catalogo as cata


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


def mostrar_videojuegos(videojuegos):
    if len(videojuegos) == 0:
        print("No hay videojuegos")
    else:
        for juego in videojuegos:
            generos = juego["generos"] #sacamos los generos del juego
            generos_ordenados = sorted(generos)  #ordenamos
            generos_ordenados_con_comas = ", ".join(generos_ordenados)
            print(f"Título: {juego['titulo']}, Año: {juego['anio']}, Géneros: {generos_ordenados_con_comas}")


def opcion_listar(catalogo):
    videojuegos = cata.listar_videojuegos(catalogo) #Devuelve una lista y lo metemos en una variable
    mostrar_videojuegos(videojuegos)

    
def opcion_eliminar(catalogo):
    titulo = input("Dime el título del videojuego que quieres eliminar: ")
    try: #Usamos el try para poder atrapar el error almacenado en la función a la que llamamos(en caso de que no esté ese videojuego que queremos eliminar)
        cata.eliminar_videojuego(catalogo, titulo)
        print("Videojuego eliminado")
    except ValueError as error: #Coge el error de la función llamada y lo almacena en la variable error
        print(f"Error: {error}") # Imprime Error: No existe el videojuego


def opcion_buscar_exacto(catalogo):
    titulo = input("Dime el título del videojuego: ")
    juego = cata.obtener_videojuego(catalogo,titulo)
    if juego != None:
         resultado = [] #Creamos el array para poder meter el juego
         resultado.append(juego) #Añado el juego al array
         mostrar_videojuegos(resultado) #Se encargará de ponerlo bonito porque si ponemos print(juego) saldrá con caracteres especiales
    else:
        print("No se ha encontrado ningún videojuego con este título")


def opcion_anadir(catalogo):
    titulo = input("Dime el título: ")
    anio_string = input("Dime el año: ")
    generos = input("Dime los géneros (separados por comas): ").split(",")
    try:
        anio = int(anio_string)
    except ValueError:
        print("Error: el año debe ser un número entero")
        return
    try:
        cata.agregar_videojuego(catalogo, titulo, anio, generos)
        print("Videojuego añadido")
    except ValueError as error:
        print(f"Error: {error}")


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
                opcion_listar(catalogo)
            case 2:
                opcion_buscar_exacto(catalogo)
            case 3: 
                print("Has elegido buscar parcial")
            case 4:
                print("Has elegido filtrar por género")
            case 5: 
                print("Has elegido filtrar por años")
            case 6:
                opcion_anadir(catalogo)
            case 7: 
                print("Has elegido modificar")
            case 8:
                opcion_eliminar(catalogo)
            case 9:
                print("Has elegido estadísticas")
            case 0:
                print("Programa terminado")
                repetir = False
            case _:
                print("Opción no válida")

catalogo_prueba = {}
cata.agregar_videojuego(catalogo_prueba, "Hades", 2020, ["acción", "rpg"])
cata.agregar_videojuego(catalogo_prueba, "Celeste", 2018, ["plataformas"])
ejecutar_menu(catalogo_prueba)