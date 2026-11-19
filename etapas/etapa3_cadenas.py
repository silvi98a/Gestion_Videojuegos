#tupla ocmpuesto por titulo, año y género
def crear_juegos():
    return[
         ("The Legend of Zelda", 1986, "Aventura"),
        ("Super Mario Bros", 1985, "Plataformas"),
        ("Tetris", 1984, "Puzle"),
        ("Zelda II: The Adventure of Link", 1987, "Aventura"),
        ("Doom", 1993, "Disparos"),
        ("Minecraft", 2011, "Sandbox"),
    ]

#descompone la tupla y cada valor pasa a ser una variable
def formatear_juego(juego):
    titulo, anio, genero = juego
    return f"{titulo} ({anio}) - {genero}"

def normalizar_juego(texto):
    return " ".join(texto.split()).casefold()

def buscar_juego_exacto(juegos,titulo):
    tit_equivalente = normalizar_juego(titulo)
    for videojuego in juegos:
        if normalizar_juego(videojuego[0]) == tit_equivalente:
            return videojuego
    return None

def buscar_texto_parcial(juegos, texto):
    texto_parcial = normalizar_juego(texto)
    return [valor for valor in juegos if texto_parcial in normalizar_juego(valor[0])]

def mostrar_juego(juegos):
    if not juegos:
        print ("No hay coincidencias")
        return
    for juego in juegos:
        print(formatear_juego(juego))

def pedir_texto():
    return input("Dame el nombre del juego o parte de el (no escribas nada para salir del buscador): ")

def principal():
    juegos = crear_juegos()
    print("Buscar juego:")
    while True:
        texto = pedir_texto()
        if not texto.strip():
            print(" Fin de la búsqueda")
            break

        busqueda_exacta = buscar_juego_exacto(juegos,texto)
        if busqueda_exacta is not None:
            print (f"{formatear_juego(busqueda_exacta)}")
        else:
            mostrar_juego(buscar_texto_parcial(juegos,texto))

if __name__ == "__main__":
    principal()
