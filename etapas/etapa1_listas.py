def crear_lista_favoritos(): #1. para crear la lista de videojuegos
    return [
        "The Last of Us I",
        "Kingdom Hearts",
        "Cyberpunk 2077",
        "Resident Evil",
        "Final Fantasy"
    ]


def anadir_juego(lista, titulo_juego): #2. para añadir un juego al final de la lista
    lista.append(titulo_juego)


def insertar_juego_posicion(lista, pos, titulo): #3. insertar un videojuego en una posición determinada.
    if pos >= 0 and pos <= len(lista):
        lista.insert(pos, titulo)
        print("Videojuego insertado")
    else:
        print("No existe esa posición")


def eliminar_juego(lista, pos): #4. eliminar un videojuego de la lista.
    if 0 <= pos < len(lista): # pos es mayor o igual que 0 y menor que la longitud de la lista o de otra forma pos está entre 0 (incluido) y len(lista) (sin incluir)      
        del lista[pos]
        print("Juego eliminado")
    else:
        print("No existe esa posición")


def recorrer_lista(lista): #5 recorrer la lista y mostrar los títulos numerados.
    for indice, titulo in enumerate(lista): # para enumerar desde el num 1 --> enumerate(lista, start=1)
        print(f"{indice}: {titulo}")


def mostrar_ordenados(lista): #6 mostrar los videojuegos ordenados alfabéticamente.
    for titulo in sorted(lista): # sorted lo que hace es que no modifica la lista, crea una nueva ordenada.
        print(titulo)


print("Lista de juegos") #1
videojuegos = crear_lista_favoritos()
print(videojuegos)

print("Añadir juego") #2
anadir_juego(videojuegos, "Hellraiser")
print(videojuegos)

print("Insertar juego en una posición") #3
pos = int(input("Dime la posición: ")) #convertirlo a int porque input devuelve texto.
titulo = input("Dime el título: ")
insertar_juego_posicion(videojuegos, pos, titulo)
print(videojuegos)

print("Eliminar juego") #4
pos_elim = int(input("Dime la posición para borrar: ")) #convertirlo a int porque input devuelve texto.
eliminar_juego(videojuegos, pos_elim)
print(videojuegos)

print("Recorrer lista") #5
recorrer_lista(videojuegos)

print("Mostrar el listado ordenado") #6
mostrar_ordenados(videojuegos)






