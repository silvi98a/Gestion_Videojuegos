from gestor import catalogo as cata
from gestor import consultas as cons


def crear_catalogo_prueba():
    catalogo = {}
    cata.agregar_videojuego(catalogo, "The Legend of Zelda", 1986, ["aventura"])
    cata.agregar_videojuego(catalogo, "Super Mario Bros", 1985, ["plataformas"])
    cata.agregar_videojuego(catalogo, "Hollow Knight", 2017, ["aventura", "plataformas"])
    cata.agregar_videojuego(catalogo, "Hades", 2020, ["acción", "rpg"])
    cata.agregar_videojuego(catalogo, "Celeste", 2018, ["plataformas"])
    return catalogo


# 1. Añadir un videojuego correctamente
def test_agregar_videojuego():
    catalogo = crear_catalogo_prueba()
    cata.agregar_videojuego(catalogo, "Kingdom Hearts", 2002, ["acción", "rpg"])
    assert len(catalogo) == 6 # Assert lo usamos para comprobar que, en este caso, la longitu de catalogo es igual a 6 porque hemos añadido un nuevo juego
    assert "kingdom hearts" in catalogo 


# 2. Intentar añadir un título duplicado
def test_anadir_titulo_duplicado():
    catalogo = crear_catalogo_prueba()
    error = False
    try:
        cata.agregar_videojuego(catalogo, "hades", 2020, ["rpg"])
    except ValueError:
        error = True
    assert error == True
    assert len(catalogo) == 5  # no se ha añadido nada


# 3. Buscar un videojuego que no existe
def test_buscar_videojuego_inexistente():
    catalogo = crear_catalogo_prueba()
    resultado = cons.buscar_por_titulo(catalogo, "Minecraft")
    assert resultado == []


# 4. Búsqueda parcial sin distinguir mayúsculas y minúsculas
def test_busqueda_parcial():
    catalogo = crear_catalogo_prueba()
    resultado = cons.buscar_por_titulo(catalogo, "ZELDA")
    assert len(resultado) == 1
    assert resultado[0]["titulo"] == "The Legend of Zelda"


# 5. Modificar el título de un videojuego
def test_modificar_titulo():
    catalogo = crear_catalogo_prueba()
    cata.modificar_videojuego(catalogo, "Hades", "Hades II")
    assert "hades ii" in catalogo
    assert "hades" not in catalogo


# 6. Eliminar un videojuego
def test_eliminar():
    catalogo = crear_catalogo_prueba()
    cata.eliminar_videojuego(catalogo, "Celeste")
    assert "celeste" not in catalogo
    assert len(catalogo) == 4


# 7. Estadísticas con el catálogo vacío
def test_estadisticas_catalogo_vacio():
    estadisticas = cons.calcular_estadisticas({})
    assert estadisticas["total"] == 0
    assert estadisticas["mas_antiguo"] is None