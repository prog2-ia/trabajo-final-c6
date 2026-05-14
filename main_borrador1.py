"""
main_artistas.py
----------------
Main de prueba aislado para el gestor de artistas.
"""

import json

from clases.Artistas.cantantes import Cantantes
from clases.Artistas.grupo import Grupos
from clases.Artistas.orquesta import Orquestas


# ------------------------------------------------------------
# Rutas de prueba

RUTAS = {
    "1": "cantantes.json",
    "2": "grupos.json",
    "3": "orquestas.json",
}

ETIQUETAS = {
    "1": "Cantante",
    "2": "Grupo",
    "3": "Orquesta",
}


# ------------------------------------------------------------
# Funciones auxiliares

def pedir_opcion():
    return input("Elige una opcion: ").strip()


def menu_artista():
    print("\n========== MENU ARTISTA ==========")
    print("(1) Añadir artista")
    print("(2) Eliminar artista")
    print("(3) Buscar artista")
    print("(4) Mostrar todos los artistas")
    print("(0) Salir")
    print("==================================")


def pedir_lista(mensaje):
    entrada = input(mensaje).strip()

    if not entrada:
        return []

    return [x.strip() for x in entrada.split(",") if x.strip()]


def pedir_tipo():
    print("\nTipo de artista:")
    print("  (1) Cantante")
    print("  (2) Grupo")
    print("  (3) Orquesta")

    tipo = pedir_opcion()

    while tipo not in ("1", "2", "3"):
        print("Opcion no valida.")
        tipo = pedir_opcion()

    return tipo


def crear_objeto_artista(
    tipo,
    nombre,
    fecha_formacion,
    pais_origen,
    activo,
    genero,
    canciones_pop,
    componentes
):

    if tipo == "1":

        tipo_voz = input("Tipo de voz: ").strip()

        return Cantantes(
            nombre=nombre,
            fecha_formacion=fecha_formacion,
            pais_origen=pais_origen,
            tipo_voz=tipo_voz,
            activo=activo,
            genero=genero,
            canciones_populares=canciones_pop,
            componentes=componentes
        )

    elif tipo == "2":

        lider = input("Líder del grupo: ").strip()

        return Grupos(
            nombre=nombre,
            fecha_formacion=fecha_formacion,
            pais_origen=pais_origen,
            lider=lider,
            activo=activo,
            genero=genero,
            canciones_populares=canciones_pop,
            componentes=componentes
        )

    elif tipo == "3":

        director = input("Director de la orquesta: ").strip()

        return Orquestas(
            nombre=nombre,
            fecha_formacion=fecha_formacion,
            pais_origen=pais_origen,
            director=director,
            activo=activo,
            genero=genero,
            canciones_populares=canciones_pop,
            componentes=componentes
        )

def leer_json(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def guardar_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)


def buscar_en_archivos(nombre):

    for ruta in RUTAS.values():

        datos = leer_json(ruta)

        for a in datos:

            if a.get("Nombre", "").lower() == nombre.lower():
                return a, ruta

    return None, None


def imprimir_artista(a):

    print(f"  Nombre:              {a.get('Nombre')}")
    print(f"  Fecha de formación:  {a.get('Fecha de formación')}")
    print(f"  País de origen:      {a.get('País de origen')}")
    print(f"  Activo:              {'Sí' if a.get('Activo') else 'No'}")
    print(f"  Género(s):           {a.get('Género', [])}")
    print(f"  Canciones populares: {a.get('Canciones populares', [])}")
    print(f"  Componentes:         {a.get('Componentes', [])}")


# ------------------------------------------------------------
# Opciones del menú

def opcion_anadir():

    print("\n=== AÑADIR ARTISTA ===")

    tipo = pedir_tipo()

    nombre = input("Nombre: ").strip()
    fecha_formacion = input("Fecha de formación: ").strip()
    pais_origen = input("País de origen: ").strip()

    activo_input = input("Activo (s/n): ").strip().lower()

    while activo_input not in ("s", "n"):
        print("Opcion no valida. Solo puedes poner (s/n).")
        activo_input = input("Activo (s/n): ").strip().lower()

    activo = activo_input == "s"

    genero = pedir_lista("Género(s) (separados por coma): ")
    canciones_pop = pedir_lista("Canciones populares (Enter si no hay): ")
    componentes = pedir_lista("Componentes (Enter si no hay): ")

    try:

        artista_nuevo = crear_objeto_artista(
            tipo,
            nombre,
            fecha_formacion,
            pais_origen,
            activo,
            genero,
            canciones_pop,
            componentes
        )

        artista_nuevo.guardar_artista(
            artista_nuevo,
            ruta=RUTAS[tipo]
        )

        print("Artista añadido correctamente.")

    except Exception as e:
        print(f"Error al añadir el artista: {e}")


def opcion_eliminar():

    print("\n=== ELIMINAR ARTISTA ===")

    nombre = input("Nombre del artista a eliminar: ").strip()

    a, ruta = buscar_en_archivos(nombre)

    if a is None:
        print(f"No se encontró el artista '{nombre}'.")
        return

    print("\nArtista encontrado:")
    imprimir_artista(a)

    confirmar = input(f"\n¿Eliminar a '{nombre}'? (s/n): ").strip().lower()

    while confirmar not in ("s", "n"):
        print("Opcion no valida.")
        confirmar = input("(s/n): ").strip().lower()

    if confirmar == "n":
        print("Eliminación cancelada.")
        return

    try:

        datos = leer_json(ruta)

        datos = [
            x for x in datos
            if x.get("Nombre", "").lower() != nombre.lower()
        ]

        guardar_json(ruta, datos)

        print(f"Artista '{nombre}' eliminado correctamente.")

    except Exception as e:
        print(f"Error al eliminar el artista: {e}")


def opcion_buscar():

    print("\n=== BUSCAR ARTISTA ===")

    nombre = input("Nombre del artista: ").strip()

    a, _ = buscar_en_archivos(nombre)

    if a is None:
        print(f"No se encontró el artista '{nombre}'.")

    else:
        print("\n== ARTISTA ENCONTRADO ==")
        imprimir_artista(a)


def opcion_mostrar_todos():

    print("\n== ARTISTAS REGISTRADOS ==")

    hay_artistas = False

    for tipo, ruta in RUTAS.items():

        datos = leer_json(ruta)

        if datos:

            hay_artistas = True

            print(f"\n-- {ETIQUETAS[tipo].upper()}S --")

            for i, a in enumerate(datos, 1):

                activo_str = "Sí" if a.get("Activo") else "No"

                generos = ", ".join(a.get("Género", [])) or "-"

                print(
                    f"  {i}. {a.get('Nombre')} | "
                    f"{a.get('País de origen')} | "
                    f"Activo: {activo_str} | "
                    f"Género: {generos}"
                )

    if not hay_artistas:
        print("No hay artistas registrados aún.")


# ------------------------------------------------------------
# Main

def main():

    print("==================================")
    print("      GESTOR DE ARTISTAS")
    print("==================================")

    running = True

    while running:

        menu_artista()

        opcion = pedir_opcion()

        while opcion not in ("0", "1", "2", "3", "4"):
            print("Opcion no valida.")
            opcion = pedir_opcion()

        if opcion == "0":

            print("Saliendo...")
            running = False

        elif opcion == "1":
            opcion_anadir()

        elif opcion == "2":
            opcion_eliminar()

        elif opcion == "3":
            opcion_buscar()

        elif opcion == "4":
            opcion_mostrar_todos()


if __name__ == "__main__":
    main()