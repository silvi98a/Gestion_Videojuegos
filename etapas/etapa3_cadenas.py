def crear_juegos():
    return [
        ("The Legend of Zelda", 1986, "Aventura"),
        ("Super Mario Bros", 1985, "Plataformas"),
        ("Tetris", 1984, "Puzle"),
        ("Zelda II: The Adventure of Link", 1987, "Aventura"),
        ("Doom", 1993, "Disparos"),
        ("Minecraft", 2011, "Sandbox"),
    ]


def formatear_juego(juego):
    titulo, anio, genero = juego
    return f"{titulo} ({anio}) - {genero}"


def normalizar_texto(texto):
    return " ".join(texto.split()).casefold()


def buscar_juego_exacto(juegos, titulo):
    titulo_normalizado = normalizar_texto(titulo)
    for juego in juegos:
        if normalizar_texto(juego[0]) == titulo_normalizado:
            return juego
    return None


def buscar_texto_parcial(juegos, texto):
    texto_normalizado = normalizar_texto(texto)
    return [
        juego for juego in juegos if texto_normalizado in normalizar_texto(juego[0])
    ]


def mostrar_juegos(juegos):
    if not juegos:
        print("No hay coincidencias")
        return
    for juego in juegos:
        print(formatear_juego(juego))


def pedir_texto():
    return input(
        "Dame el nombre del juego o parte de él " "(no escribas nada para salir): "
    )


def principal():
    juegos = crear_juegos()
    print("Buscar juego:")
    while True:
        texto = pedir_texto()
        if not texto.strip():
            print("Fin de la búsqueda")
            break

        exacto = buscar_juego_exacto(juegos, texto)
        if exacto is not None:
            print(formatear_juego(exacto))
        else:
            mostrar_juegos(buscar_texto_parcial(juegos, texto))


if __name__ == "__main__":
    principal()
