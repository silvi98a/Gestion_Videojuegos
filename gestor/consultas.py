# Buscar por el título de la película
def buscar_por_titulo(catalogo, texto):
    resultado = []

    # normalizamos lo que ha escrito el usuario (sin mayusculas, sin espacios extra...)
    texto_normalizado = " ".join(texto.lower().split())

    # recorremos el catálogo
    for videojuego in catalogo.values():
        # Normalizamos el titulo:
        titulo_buscado = " ".join(videojuego["titulo"].lower().split())
        # Si encuentra el texto normalizado (escrito por el user) en titulos...
        if texto_normalizado in titulo_buscado:
            # añade el viideojuego en la ultima posicion de la lista RESULTADO
            resultado.append(videojuego)

    return resultado  # devuelve la lista (vacía si no hubo coincidencias)


def filtrar_por_genero(catalogo, genero):
    resultado = []

    # normalizamos lo que ha escrito el usuario (sin mayusculas, sin espacios extra...)
    texto_normalizado = " ".join(genero.lower().split())

    # recorremos el catálogo
    for videojuego in catalogo.values():
        # recorremos cada género del videojuego ( se hace así porque es un conjunto)
        for g in videojuego["generos"]:
            # normalizamos ese género y lo comparamos con el buscado
            if " ".join(g.lower().split()) == texto_normalizado:
                resultado.append(videojuego)
                break  # para salir del bucle y pasar al siguiente videojuego

    return resultado  # devuelve la lista (vacía si no hubo coincidencias)


def filtrar_por_anios(catalogo, anio_min, anio_max):
    resultado = []

    # recorremos el catálogo
    for videojuego in catalogo.values():
        # si el año del videojuego está dentro del rango...
        if videojuego["anio"] >= anio_min and videojuego["anio"] <= anio_max:
            # ...lo añadimos al final de la lista RESULTADO
            resultado.append(videojuego)

    return resultado  # devuelve la lista (vacía si no hubo coincidencias)
def contar_por_genero(catalogo): # devuelve cuántos videojuegos hay de cada género.
    conteo = {} #tiene que ser diccionario {} porque añade clave->valor {"Aventura": 2, "Acción": 1}
    for videojuego in catalogo.values(): #recorre los juegos del catalogo(por values)
        for genero in videojuego["generos"]: #recorre los generos del videojuego anterior
            conteo[genero] = conteo.get(genero, 0) + 1 #si un valor no existe, pone 0 y le suma 1. Cuando existe el valor, le sumará el +1 al número que tenga(que es las veces que sale)
    return conteo


def juego_mas_antiguo(catalogo):
    antiguo = None #variable sin nada
    for videojuego in catalogo.values(): #values() da los diccionarios de los juegos (titulo, anio y generos) y las claves las ignora.
        if antiguo is None or videojuego["anio"] < antiguo["anio"]: #si la variable no tiene nada o el año del juego actual es menor que el del guardado, o sea, es más antiguo, se guarda el juego.
            antiguo = videojuego # actualizo
    return antiguo


def juego_mas_reciente(catalogo):
    reciente = None
    for videojuego in catalogo.values():
        if reciente is None or videojuego["anio"] > reciente["anio"]:
            reciente = videojuego
    return reciente


def calcular_estadisticas(catalogo):
    total = len(catalogo)
    por_genero = contar_por_genero(catalogo)
    mas_antiguo = juego_mas_antiguo(catalogo)
    mas_reciente = juego_mas_reciente(catalogo)
    return {
        "total": total,
        "por_genero": por_genero,
        "mas_antiguo": mas_antiguo,
        "mas_reciente": mas_reciente,
    }
