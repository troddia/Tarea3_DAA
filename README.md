# Tarea 3 - Implementación y prueba de filtro Bloom

## Integrantes

- Oscar Quezada
- Camila Reyes
- Tomas Rodriguez

## Librerías utilizadas

- matplotlib
- random
- csv
- numpy
- pandas
- time
- math
- os

## Cómo ejecutar el código


Existen 5 archivos python: 
- hash.py es donde se encuentra la estructura del filtro de bloom
- test_m_k.py, es donde se realizan los test para los parametros m (100 000 a 1 000 000, cada 100 000 con 10 iteraciones) y k (de 1 a 10, 10 iteraciones), en este script se prueba para distintos N modificando la variable en la linea 69 del script. Todos los N (nobres a buscar) tendran 3000 busquedas infructuosas solamente.
**IMPORTANTE: test_m_k.py crea 3 archivos un txt y 2 graficos (porcentaje de errror y tiempo de ejecucion) pero si se quiere correr para otro N guardar resultados antes ya que se se sobreescriben al correr el test de nuevo**
- test_3_n.py, es un script que lee los resultados y grafica para los N (nombres a buscar): 4500, 6000, 12000 con 3000 busquedas infructuosas en cada uno para k=5 con m desde 100 000 a 1 000 000.
- test_n_porcentaje.py, compara el algoritmo sin y con filtro variando los porcentajes de busquedas infructuosas.
- test_n_tamanno.py, compara el algoritmo sin y con filtro variando los tamannos de n dejando siempre la mitad de N(nombres a buscar) con busquedas infuctuosas.
## Descripción del programa

## Logica de los TEST
Para los test se generan las funciones de hash para los k y m seleccionados, para despues medir el tiempo de busqueda, la tasa de error, etc. Esto para un arreglo de N palabras.
## EXTRA
Se dejaron en la carpeta tests pasados para que se vean el tipo de archivos creados en caso de que el ayudante tenga problemas de compilacion o quiera comparar. Estos graficos se usaron para 

Los tests anteriores guardados se utilizaron para el analisis en el informe (graficos y conclusiones).