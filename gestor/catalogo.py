def normalizar_titulo(titulo):
    return " ".join(titulo.split()).lower()


def normalizar_genero(genero):
    return " ".join(genero.split()).capitalize()


def validar_titulo(titulo):
    if not isinstance(titulo, str) or not titulo.strip():
        raise ValueError("El título no puede estar vacío")
    return " ".join(titulo.split())


def validar_anio(anio):
    if isinstance(anio, bool) or not isinstance(anio, int) or anio <= 0:
        raise ValueError("El año tiene que ser un entero positivo")
    return anio


def validar_generos(generos):
    if isinstance(generos, str):
        generos = [generos]
    resultado = set()
    for genero in generos:
        if isinstance(genero, str) and genero.strip():
            resultado.add(normalizar_genero(genero))
    if not resultado:
        raise ValueError("El videojuego tiene que tener al menos un género")
    return resultado


def agregar_videojuego(catalogo, titulo, anio, generos):
    titulo = validar_titulo(titulo)
    anio = validar_anio(anio)
    generos = validar_generos(generos)

    id_juego = normalizar_titulo(titulo)
    if id_juego in catalogo:
        raise ValueError(f"Ya existe el videojuego '{titulo}'")

    catalogo[id_juego] = {"titulo": titulo, "anio": anio, "generos": generos}
    return id_juego


def obtener_videojuego(catalogo, titulo):
    return catalogo.get(normalizar_titulo(titulo))


def listar_videojuegos(catalogo):
    return [catalogo[id_juego] for id_juego in sorted(catalogo)]


def modificar_videojuego(
    catalogo, titulo, nuevo_titulo=None, nuevo_anio=None, nuevos_generos=None
):
    id_actual = normalizar_titulo(titulo)
    if id_actual not in catalogo:
        raise ValueError(f"No existe el videojuego '{titulo}'")

    juego = catalogo[id_actual]
    titulo_final = juego["titulo"]
    anio_final = juego["anio"]
    generos_final = juego["generos"]

    if nuevo_titulo is not None:
        titulo_final = validar_titulo(nuevo_titulo)
    if nuevo_anio is not None:
        anio_final = validar_anio(nuevo_anio)
    if nuevos_generos is not None:
        generos_final = validar_generos(nuevos_generos)

    id_nuevo = normalizar_titulo(titulo_final)
    if id_nuevo != id_actual and id_nuevo in catalogo:
        raise ValueError(f"Ya existe el videojuego '{titulo_final}'")

    del catalogo[id_actual]
    catalogo[id_nuevo] = {
        "titulo": titulo_final,
        "anio": anio_final,
        "generos": generos_final,
    }
    return id_nuevo


def eliminar_videojuego(catalogo, titulo):
    id_juego = normalizar_titulo(titulo)
    if id_juego not in catalogo:
        raise ValueError(f"No existe el videojuego '{titulo}'")
    return catalogo.pop(id_juego)
