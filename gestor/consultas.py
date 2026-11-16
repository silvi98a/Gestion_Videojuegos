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
