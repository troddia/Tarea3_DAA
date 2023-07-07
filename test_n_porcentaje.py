from hash import Filter
import random
import pandas as pd
import math
import time
import csv
import matplotlib.pyplot as plt
import numpy as np

# Creamos los arreglos con N = 3000, variando el porcentaje de nombres de peliculas

porcentajes = [0, 0.25, 0.50, 0.75, 1]
nombres_por_porcentaje = []
tiempo_filtro = []
tiempo_sin_filtro = []

# Se calculan los distintos N
for porcentaje in porcentajes:

    data = pd.read_csv('Popular-Baby-Names-Final.csv', header=None) 
    data_2 = pd.read_csv('Film-Names.csv', header=None)

    total_nombres = len(data)
    total_nombres_2 = len(data_2)

    cantidad_indices_aleatorios = math.ceil(3000*(1-porcentaje))

    indices_aleatorios = random.sample(range(total_nombres), cantidad_indices_aleatorios)
    indices_aleatorios_2 = random.sample(range(total_nombres_2), 3000 - cantidad_indices_aleatorios)

    nombres_aleatorios = data.iloc[indices_aleatorios][0].tolist()
    nombres_aleatorios_2 = data_2.iloc[indices_aleatorios_2][0].tolist()

    nombres_combinados = nombres_aleatorios + nombres_aleatorios_2

    for nombre in nombres_combinados:
        if type(nombre) == float :
            print(f"hay un nan en el porcentaje {porcentaje}" )


    random.shuffle(nombres_combinados)

    nombres_por_porcentaje.append(nombres_combinados)
 
# Se crea el filtro
hash_family = Filter(1000000007, 500000, 3)

hash_family.generate_hash_functions()

csv_file = 'Popular-Baby-Names-Final.csv'

hash_family.fill_filter(csv_file)

#//
positive = 0
false_positive = 0
negative = 0

# con filtro
for index, nombres in enumerate(nombres_por_porcentaje):

    start_time = time.time()
    for i in range(3000):
        name = nombres[i]
        if hash_family.pass_filter(name):
            #loop through the csv list
            csv_file = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
            for row in csv_file:
                state = 0

                # Si el elemento existe, se imprime lo siguiente
                if (name == row[0]):   
                    positive +=1
                    state = 1
                    break 
            
            if (state == 0):
                false_positive +=1    
        else:
            negative += 1     
                
    end_time = time.time()
    execution_time = end_time - start_time 
    tiempo_filtro.append(execution_time)

    false_positive_rate = (false_positive / 25000) * 100
    with open('resultados_comparacion.txt', 'a') as file:
        file.write("Test for porcentaje con filtro = " + str(porcentajes[index])+ "\n")
        file.write("Execution Time: " + str(execution_time) + "\n")
        file.write("Positive: " + str(positive) + "\n")
        file.write("False Positive: " + str(false_positive) + "\n")
        file.write("Negative: " + str(negative) + "\n")
        file.write("Error %: " + str(false_positive_rate) + "%\n")
        file.write("--------------------------------------------------------------" + "%\n")


# sin filtro
for index, nombres in enumerate(nombres_por_porcentaje):

    start_time = time.time()
    for i in range(3000):
        name = nombres[i]

        #loop through the csv list
        csv_file = csv.reader(open('Popular-Baby-Names-Final.csv', "r"), delimiter=",")
        for row in csv_file:
            # Si el elemento existe, se imprime lo siguiente
            if (name == row[0]):   
                break 
        
    end_time = time.time()
    execution_time = end_time - start_time 
    tiempo_sin_filtro.append(execution_time)


    with open('resultados_comparacion.txt', 'a') as file:
        file.write("Test for porcentaje sin filtro = " + str(porcentajes[index])+ "\n")
        file.write("Execution Time: " + str(execution_time) + "\n")
        file.write("--------------------------------------------------------------" + "%\n")


# Datos para la primera curva
x = porcentajes  
y1 = tiempo_filtro 
y2 = tiempo_sin_filtro

# Crear el gráfico
plt.plot(x, y1,'-o',label='Con filtro')
plt.plot(x, y2,'-o',label='Sin filtro')

# Configurar etiquetas y leyenda
plt.xlabel('Porcentaje de búsquedas infructuosas')
plt.ylabel('Tiempo Ejecución [s]')
plt.title('Comparación búsquedas con y sin filtro')
plt.legend()
plt.savefig('comparacion.png')
plt.close()