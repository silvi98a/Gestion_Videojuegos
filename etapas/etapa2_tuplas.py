# 1. Creamos una lista con 5 videojuegos representados mediante tuplas.
def crear_videojuegos():
    return [
        ("The Legend of Zelda", 1986, "Aventura"),
        ("Super Mario Bros", 1985, "Plataformas"),
        ("The Last of Us", 2013, "Acción"),
        ("Hollow Knight", 2017, "Plataformas"),
        ("Life is Strange 2", 2018, "Narrativa Interactiva"),
    ]


# 2. Recibe una tupla y devuelva una cadena con la información del videojuego formateada.
def formatear_videojuego(videojuego):
    titulo, anio, genero = videojuego
    return f"{titulo} ({anio}) - {genero}"


# 3. Recorrer la lista y mostrar los datos de cada videojuego.
def mostrar_videojuego(videojuegos):
    for videojuego in videojuegos:
        print(formatear_videojuego(videojuego))


# Llamadas a las funciones
videojuegos = crear_videojuegos()
mostrar_videojuego(videojuegos)
