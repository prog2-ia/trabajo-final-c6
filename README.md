# BIBLIOTECA MUSICAL

---
### Kacper Piklowski y Tegra Vuvu

---
La idea principal de este programa es ofrecer una gestion sencilla del contenido musical (canciones, playlists...), incluyendo posibilidad de guardar informacion (con archivos `.json`) sobre los _grupos/artistas_, y todo esto controlado por una funcion logica con bucles. 

---

\
**El programa contiene:**
1. **Archivo `main.py`**: contiene la parte fundamental del proyecto, es decir el menu controlado por los bucles y condicionales.

2. **Carpeta `Archivos`**: esta carpeta contiene todos los archivos que vamos a utilizar para montar el programa. Destacamos:
- **Carpeta `albumes`**: contendra albumes que se van a crear\guardar. 
- **Carpeta `playlists`**: la misma logica que con albumes. Se podran crear y modificar playlists.
- **Carpeta `artistas_guardados`**: una carpeta que dentro contiene archivos `.json` donde vamos a guardar los grupos, cantantes...
- **Archivos `canciones_guardadas` y `generos_disponibles`**: sirven para guardar las canciones y los generos disponibles, respectivamente. 

3. **Carpeta `clases`**: esta carpeta contiene el contenido importante que aprendemos en esta asignatura. Dividimos las clases en varias carpetas:
- `Atristas`: contiene un archivo principal `artistas` y otros archivos que **heredan** de la clase principal. Es una **clase abstracta** 
- Del mismo modo tenemos las carpetas `Contenido` y que contienen las clases que nos serviran para gestinar el contenido musical (canciones, albumes...).

---
A lo largo de la practica hemos intentado introducir todo lo que hemos visto en clases. La idea es manejar los archivos `.json` para guardar la informacion. A dia de hoy, hemos intentado implementar un poco de `.json`, pero por ahora nos hemos centrado mas en las clases y objetos vistas en clase. Hemos implementado una herencia multiple en el archivo `productor_musical.py`, y convertimos la clase `Artistas` en una clase abstracta.

---

---


