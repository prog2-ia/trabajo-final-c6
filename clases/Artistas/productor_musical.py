from clases.Artistas.artistas import Artista
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
    def guardar_productor(productor,ruta='archivos/productores_guardados.json'):
        with open(ruta, "r", encoding="utf-8") as f:
            productores = json.load(f)

        #anadimos productores al archivo json.
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

        #escribimos en el archivo json.
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(productores, f, ensure_ascii=False, indent=4)

        #mostramos el mensaje de que se ha guardado correctamente.
        print(f"Productor musical '{productor.nombre}' guardado correctamente.")


    #Metodo matemático para guardar productor

    def __iadd__(self, productor,ruta='archivos/productores_guardados.json'):
        with open(ruta, "r", encoding="utf-8") as f:
            productores = json.load(f)

        #anadimos productores al archivo json.
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

        #escribimos en el archivo json.
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(productores, f, ensure_ascii=False, indent=4)



#-----------------------------------------------

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

