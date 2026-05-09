from clases.Artistas.productor_musical import ProductorMusical

#Añadir a un productor-----------------------------------------------------------------------


print("\n=== ANADIR PRODUCTOR ===")

nombre = input('Introduce el nombre del productor: ').strip()
fecha_de_formacion = input('Introduce la fecha de la formacion: ').strip()
pais_origen = input('Introduce la pais de la origen: ').strip()

activo_input = input('Introduce la actividad (True/False): ').strip().lower()
activo = activo_input == "true"

genero = input('Introduce los generos separados por coma: ').split(',')
canciones_populares = input('Introduce canciones separadas por coma: ').split(',')
componentes = input('Introduce componentes separados por coma: ').split(',')
producciones = input('Introduce producciones separadas por coma: ').split(',')
print(f'Anadiendo productor...')

#Creamos un objeto ProductorMusical
productor = ProductorMusical(
    nombre = nombre,
    fecha_formacion = fecha_de_formacion,
    pais_origen = pais_origen,
    activo = activo,
    genero = genero,
    canciones_populares = canciones_populares,
    componentes = componentes,
    producciones = producciones,
)

productor.guardar_productor(productor, ruta='archivos/artistas_guardados/productores_guardados.json')









#Eliminar canciones de la base de datos-----------------------------------------------------------------------
#Pedimos datos para eliminar -> Por nombre
nombre = input('Introduce el nombre del productor: ').strip()
print()
print("Buscando el productor...")
#Buscamos el productor en nuestra base
productor_encontrado = productor.buscar_productor(nombre)

#Si no la encontramos
if productor_encontrado is None:
    print('El productor {p.nombre} no existe}')

#Si la encontramos
else:
    #Nos aseguramos de que no ha sido un missclick
    opcion_eliminar_productor = input(f'¿Eliminar el productor {productor_encontrado.nombre}? (s/n)').strip()
    #Validamos la peticion
    while opcion_eliminar_productor not in ('s', 'n'):
        print('Opcion no valida. Solo puedes poner (s/n)')
        opcion_eliminar_productor = input(f'¿Eliminar el productor {productor_encontrado.nombre}? (s/n)').strip().lower()

     #si decimos que si:
    if opcion_eliminar_productor == "s":
        print(f"Eliminando el productor {productor_encontrado.nombre}...")
        productor.eliminar_productor(nombre)
        print(f"Productor '{productor_encontrado.nombre}' eliminada correctamente.")
    #si ha sido un missclick
    else:
        print("La eliminacion se ha canceldado.")




#Buscar productor------------------------------------------------------------------------------
nombre = input('Introduce el nombre del productor: ').strip()
print()
print("Buscando el productor...")
#Buscamos el productor en nuestra base
productor_encontrado = productor.buscar_productor(nombre)

#Si no la encontramos
if productor_encontrado is None:
    print('El productor {p.nombre} no existe}')

#Si la encontramos
else:
    print(f'== PRODUCTOR ENCONTRADO ==')
    productor_encontrado.mostrar_info()


#Mostrar todos los productores-----------------------------------------------------------------------
ProductorMusical.mostrar_productores()