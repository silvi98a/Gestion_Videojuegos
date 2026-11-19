#Mostrar Géneros 
def mostrar_generos(generos):
    generos_ordenado = sorted(generos)
    for genero in generos_ordenado:
        print(genero)


def anadir_genero(generos, genero):
    generos.add(genero)


def eliminar_genero(generos, genero):
    if genero in generos:
        generos.remove(genero)
        return True
    else:
        return False


def existe_genero(generos, genero):
    generos_minuscula = set()
    for valor in generos:
        generos_minuscula.add(valor.lower())
    return genero.lower() in generos_minuscula


def union_generos(generos_a, generos_b):
    return generos_a.union(generos_b)


def interseccion_generos(generos_a, generos_b):
    return generos_a.intersection(generos_b)


def diferencia_generos(generos_a, generos_b):
    return generos_a.difference(generos_b)


def main():
    mis_generos = {"Aventura", "Narrativa Interactiva", "Plataformas", "Acción", "Plataformas"}
    otros_generos = {"Acción", "Fantasía", "Terror", "Misterio", "RPG"}

    print("Mis géneros: ")
    mostrar_generos(mis_generos)

    anadir_genero(mis_generos,"Terror")
    print("\nTras añadir Terror: ")
    mostrar_generos(mis_generos)
    eliminado = eliminar_genero(mis_generos,"Terror")
    eliminado2 = eliminar_genero(mis_generos,"Fantasía")
    if eliminado == True:
        print("Género eliminado")
    else:
        print("Ese género no existe")
    if eliminado2 == True:
        print("Género eliminado")
    else:
        print("Ese género no existe")

    print("\nTras eliminar: ")
    mostrar_generos(mis_generos)

    genero_usuario = input("Introduce un género para comprobar: ").strip()
    if existe_genero(mis_generos, genero_usuario):
        print(f"'{genero_usuario}' está en tu colección")
    else:
        print(f"'{genero_usuario}' no está en tu colección")
    print("\nGéneros de otra persona: ")
    mostrar_generos(otros_generos)
    union = union_generos(mis_generos, otros_generos)
    print("Unión: ")
    mostrar_generos(union)
    interseccion = interseccion_generos(mis_generos, otros_generos)
    print("Intersección: ")
    mostrar_generos(interseccion)
    diferencia = diferencia_generos(mis_generos, otros_generos)
    print("Diferencia: ")
    mostrar_generos(diferencia)


if __name__ == "__main__":
    main()

