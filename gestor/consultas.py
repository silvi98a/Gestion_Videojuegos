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
