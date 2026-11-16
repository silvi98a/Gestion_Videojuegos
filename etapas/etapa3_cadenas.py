#tupla ocmpuesto por titulo, año y género
def crearJuegos():
    return[
         ("The Legend of Zelda", 1986, "Aventura"),
        ("Super Mario Bros", 1985, "Plataformas"),
        ("Tetris", 1984, "Puzle"),
        ("Zelda II: The Adventure of Link", 1987, "Aventura"),
        ("Doom", 1993, "Disparos"),
        ("Minecraft", 2011, "Sandbox"),
    ]

#descompone la tupla y cada valor pasa a ser una variable
def formatearJuego(juego):
    titulo, anio, genero = juego
    return f"{titulo} {anio} {genero}"

def normalizarJuego(texto):
    return " ".join(texto.split()).casefold()

def buscarJuegoExacto(juegos,titulo):
    titEquivalente = normalizarJuego(titulo)
    for videojuego in juegos:
        if normalizarJuego(juegos[0] == titEquivalente):
            return videojuego
    return None

def buscarTextoParcial(juegos, texto):
    textoParcial = normalizarJuego(texto)
    return [valor for valor in juegos if textoParcial in normalizarJuego(valor[0])]

def mostrarJuego(juego):
    if not juego:
        print ("No hay coincidencias")
        return

def pedirTexto():
    return input("Dame el nombre del juego o parte de el (no escribas nada para salir del buscador): ")

def principal():
    juegos = crearJuegos()
    print("Buscar juego:")
    while True:
        texto = pedirTexto()
        if not texto.strip():
            print(" Fin de la búsqueda")
            break

        busquedaExacta = buscarJuegoExacto(juegos,texto)
        if busquedaExacta is not None:
            print (f"{formatearJuego(busquedaExacta)}")
        
        mostrarJuego(buscarTextoParcial(juegos,texto))