from gestor import catalogo as cata
from gestor import consola


def crear_catalogo_inicial():
    catalogo = {}
    cata.agregar_videojuego(catalogo, "The Legend of Zelda", 1986, ["aventura"])
    cata.agregar_videojuego(catalogo, "Super Mario Bros", 1985, ["plataformas"])
    cata.agregar_videojuego(catalogo, "Hollow Knight", 2017, ["aventura", "plataformas"])
    cata.agregar_videojuego(catalogo, "Hades", 2020, ["acción", "rpg"])
    cata.agregar_videojuego(catalogo, "Celeste", 2018, ["plataformas"])
    return catalogo


def main():
    catalogo = crear_catalogo_inicial()
    consola.ejecutar_menu(catalogo)


main()