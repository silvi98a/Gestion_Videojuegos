# Gestor de Videojuegos

Práctica en Python para gestionar un catálogo de videojuegos.

## Descripción

Aplicación de consola en Python para gestionar un catálogo de videojuegos. El catálogo se guarda en memoria mientras el programa está en ejecución.

Funcionalidades:

- Listar los videojuegos del catálogo.
- Buscar por título exacto o parcial, sin distinguir mayúsculas ni espacios extra.
- Filtrar por género o por rango de años.
- Añadir, modificar y eliminar videojuegos.
- Mostrar estadísticas: total de videojuegos, número de videojuegos por género y videojuegos más antiguo y más reciente.

Cada videojuego tiene un título, un año de lanzamiento y uno o varios géneros.

El proyecto incluye también cuatro programas independientes (etapas 1 a 4) para practicar listas, tuplas, cadenas y conjuntos.

## Estructura

```
gestor-videojuegos/
├── main.py
├── gestor/
│   ├── __init__.py
│   ├── catalogo.py
│   ├── consultas.py
│   └── consola.py
├── etapas/
│   ├── etapa1_listas.py
│   ├── etapa2_tuplas.py
│   ├── etapa3_cadenas.py
│   └── etapa4_conjuntos.py
├── README.md
└── .gitignore
```

- `main.py`: crea el catálogo inicial con varios videojuegos y ejecuta la aplicación.
- `gestor/`: paquete con la lógica de la aplicación.
  - `catalogo.py`: operaciones para crear, leer, modificar y eliminar videojuegos.
  - `consultas.py`: búsquedas, filtros y estadísticas.
  - `consola.py`: menú interactivo y entrada/salida por consola.
- `etapas/`: programas independientes de las etapas 1 a 4 (listas, tuplas, cadenas y conjuntos).

## Ejecución

Requiere Python 3. Los comandos se ejecutan desde la carpeta raíz del proyecto.

Aplicación final:

```bash
python main.py
```

Etapas iniciales:

```bash
python etapas/etapa1_listas.py
python etapas/etapa2_tuplas.py
python etapas/etapa3_cadenas.py
python etapas/etapa4_conjuntos.py
```

## Equipo

- Silvia Utrero. Coordinadora. Encargada de repositorio, etapa 1 y estadísticas de `consultas.py`.
- Ángela Ruíz. Dev A. Encargada de etapa 2 y funciones de búsqueda y filtrado de `consultas.py`.
- Daniel De Vicente. Dev B. Encargado de etapa 3 y operaciones de `catalogo.py`.
- Yandrik Guzmán. Dev C. Encargado de etapa 4, `consola.py` y `main.py`.