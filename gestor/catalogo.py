#Titulo en minúsculas y todo junto (sin espacios)
def tituloNormalizado(titulo):
    return "".join(titulo.split()).casefold()

#para generar titulo
def crearId(titulo):
    return tituloNormalizado(titulo)

#para validar el titulo y quitar espacios extra
def validarTit(titulo):
    if not isinstance(titulo,str) or not titulo.strip():
            raise ValueError("El titulo no puedo estar vacío")
    return " ".join(titulo.split())

#para validar el año, devuelve string normalizado
def validarAnio(anio):
    if isinstance(anio,bool) or not isinstance(anio,int) or anio <= 0:
        raise ValueError("El año tiene que ser entero")
    return anio

#para validar el género, devuelve un string normalizado
def validarGenero(genero):
    if isinstance(genero,str):
        raise ValueError("")
    normalizar = {
        " ".join(genero.split()).capitalize()
        for genero in genero
        if isinstance(genero,str) and genero.strip()
    }
    if not normalizar:
        raise ValueError("El juego tiene que tener un genero")
    return normalizar



            
#crea el catálogo
def nuevoCatalogo():
    return {}

#para añadir un juego nuevo, en caso de existir una misma ID en el catálogo, salta error
def anadirJuego(catalogo,titulo,anio,genero):
    titulo = validarTit(titulo)
    anio =validarAnio(anio)
    genero = validarGenero(genero)

    idJuego = crearId(titulo)
    if idJuego in catalogo:
        raise ValueError(f"Ya existe `{titulo}` ")
    catalogo[idJuego] = {"titulo":titulo, "anio":anio,"geneor":genero}
    return idJuego

#para obteener un juego en concreto
def obtenerJuego (catalogo,titulo):
    return catalogo.get(crearId(titulo))

#lista todos los juegos
def listarJuegos(catalogo):
    return [catalogo[idJuego] for idJuego in sorted(catalogo)]

#actualizar un juego con datos nuevos, en caso de que el título ya exista, o la id no exista, salta error
def actualizarJuego(catalogo,titulo,nuevoTit =None,nuevoAnio=None,nuevoGenero=None):
    idActual = crearId(titulo)
    if idActual not in catalogo:
        raise KeyError(f"No existe `{titulo}`.")

    datosJuego = catalogo[idActual]
    tituloFinal = (datosJuego["titulo"] if nuevoTit is None else validarTit(nuevoTit))
    anioFinal = (datosJuego["anio"] if nuevoAnio is None else validarAnio(nuevoAnio))
    generoFinal = (datosJuego["genero"] if nuevoGenero is None else validarGenero(nuevoGenero))

    idNuevo = crearId(tituloFinal)
    if idNuevo != idActual and idNuevo in catalogo:
        raise ValueError(f"Ya exite `{tituloFinal}`.")

    del catalogo[idActual]
    catalogo[idNuevo] = {
        "titulo": tituloFinal,
        "anio": anioFinal,
        "genero": generoFinal
    }
    return idNuevo

#eliminar juego, error si no existe la id en concreto
def eliminarJuego(catalogo,titulo):
    idJuego = crearId(titulo)
    if idJuego not in catalogo:
        raise ValueError(f"No existe ´{titulo}´.")
    return catalogo.pop(idJuego)


