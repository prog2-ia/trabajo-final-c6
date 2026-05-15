from clases.Artistas.artistas import Artista, ArtistaError
from clases.Artistas.productor import Productor
import json

#clase de herencia multiple
class ProductorMusical(Artista,Productor):
    def __init__(self,nombre: str,fecha_formacion: str ,pais_origen: str, activo: bool, genero=None,canciones_populares= None, componentes =None, producciones = None):
        Artista.__init__(self,nombre,fecha_formacion,pais_origen, activo, genero, canciones_populares, componentes)
        Productor.__init__(self,producciones)

#-------------------------------------------

    # metodo donde abrimos json y guardamos el productor.
    @staticmethod
    def guardar_productor(productor, ruta='archivos/productores_guardados.json'):
        if not isinstance(productor, ProductorMusical):
            raise TypeError("Solo se pueden guardar objetos ProductorMusical.")

        try:
            with open(ruta, "r", encoding="utf-8") as f:
                productores = json.load(f)

        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

        except json.JSONDecodeError:
            raise ArtistaError("El archivo JSON está corrupto o mal formado.")

        else:
            productores.append({
                "Nombre": productor.nombre,
                "Fecha de formación": productor.fecha_formacion,
                "País de origen": productor.pais_origen,
                "Activo": productor.activo,
                "Genero": productor.genero,
                "Canciones populares": productor.canciones_populares,
                "Componentes": productor.componentes,
                "Producciones": productor.producciones
            })

            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(productores, f, ensure_ascii=False, indent=4)

        finally:
            print(f"Intento de guardar productor musical '{productor.nombre}' finalizado.")
#-----------------------------------------------

    #Metodo para eliminar el productor
    @staticmethod
    def eliminar_productor(productor, ruta='archivos/productores_guardados.json'):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)

        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

        except json.JSONDecodeError:
            raise ArtistaError("El archivo JSON está corrupto o mal formado.")

        encontrado = False

        for p in datos:
            if p.get("Nombre", "").lower() == productor.lower():

                datos.remove(p)
                encontrado = True
                break

        if not encontrado:
            raise ValueError(f"No se encontró el productor '{productor}'.")

        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

        print(f"Productor '{productor}' eliminado correctamente.")



    #Metodo para buscar productor por nombre y mostrar su información
    @staticmethod
    def buscar_productor(productor, ruta='archivos/productores_guardados.json'):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                productores = json.load(f)

        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

        except json.JSONDecodeError:
            raise ArtistaError("El archivo JSON está corrupto o mal formado.")

        else:
            encontrado = False
            for p in productores:
                if p.get("Nombre", "").lower() == productor.lower():
                    encontrado = True

                    # Mostrar info
                    # .get() evita errores si la clave NO existe.
                    print("=== PRODUCTOR MUSICAL ===")
                    print(f"Nombre: {p.get('Nombre')}")
                    print(f"Fecha de formación: {p.get('Fecha de formación')}")
                    print(f"País de origen: {p.get('País de origen')}")
                    print(f"Activo: {p.get('Activo')}")
                    print(f"Género: {p.get('Genero')}")
                    print(f"Canciones populares: {p.get('Canciones populares')}")
                    print(f"Componentes: {p.get('Componentes')}")
                    print(f"Producciones: {p.get('Producciones')}")

                    return p



            if not encontrado:
                raise ValueError(f'No se encontró el productor {productor.nombre}.')
            return None

    @staticmethod
    def mostrar_productores( ruta='archivos/productores_guardados.json'):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                productores = json.load(f)

        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

        except json.JSONDecodeError:
            raise ArtistaError("El archivo JSON está corrupto o mal formado.")

        else:
            if not productores:
                print("No hay productores registrados.")
                return

            for p in productores:
                # Mostrar info
                # .get() evita errores si la clave NO existe.
                print("\n=== PRODUCTOR MUSICAL ===")
                print(f"Nombre: {p.get('Nombre')}")
                print(f"Fecha de formación: {p.get('Fecha de formación')}")
                print(f"País de origen: {p.get('País de origen')}")
                print(f"Activo: {p.get('Activo')}")
                print(f"Género: {p.get('Genero')}")
                print(f"Canciones populares: {p.get('Canciones populares')}")
                print(f"Componentes: {p.get('Componentes')}")
                print(f"Producciones: {p.get('Producciones')}")

    #creamos un metodo para mostrar info sobre el productor musical.
    def mostrar_info(self):
        print("=== PRODUCTOR MUSICAL ===")
        # usa el me_todo abstracto comun de la clase artista que hereda.
        super().mostrar_info()
        #anadimos producciones que es especifico de esta clase.
        print(f"Producciones: {self.producciones}")


    def __str__(self):
        return (
            f"INFORMACION PRODUCTOR MUSICAL"
            f"{Artista.__str__(self)}\n"
            f"Producciones: {self.producciones}"
        )

    def __repr__(self):
        return ( f'{type(self)}\n"'
                 f'{Artista.__str__(self)}\n'
                 f'Producciones: {self.producciones}'
        )

