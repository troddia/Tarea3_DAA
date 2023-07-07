from hash import Filter
import random
import pandas as pd
import time
import csv
import matplotlib.pyplot as plt
import numpy as np



# Numero primo muy grande, este debe ser mas grande que la cantidad de datos en el filtro. (Nos aseguramos usando uno muy grande)
p = 1000000007  
def test(m, k, n, names):

    hash_family = Filter(p, m, k)

    hash_family.generate_hash_functions()

    csv_file = 'Popular-Baby-Names-Final.csv'

    hash_family.fill_filter(csv_file)

    

    positive = 0
    false_positive = 0
    negative = 0
    
    start_time = time.time()
    for i in range(n):
        name = names[i]
        if hash_family.pass_filter(name):
            #recorre el archivo csv
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
    false_positive_rate = (false_positive / n) * 100
    with open('resultados_k'+str(k)+'.txt', 'a') as file:
        file.write("Test for m = " + str(m) + " and k = " + str(k) + "\n")
        file.write("Execution Time: " + str(execution_time) + "\n")
        file.write("Positive: " + str(positive) + "\n")
        file.write("False Positive: " + str(false_positive) + "\n")
        file.write("Negative: " + str(negative) + "\n")
        file.write("Error %: " + str(false_positive_rate) + "%\n")
        file.write("--------------------------------------------------------------" + "%\n")
    return execution_time, false_positive_rate


data = pd.read_csv('Popular-Baby-Names-Final.csv', header=None) 
data_2 = pd.read_csv('Film-Names.csv', header=None)

total_nombres = len(data)
total_nombres_2 = len(data_2)
# ESCOGER 'n', tamano de la lista de los elementos que se buscan (este debe ser mayor a 3000)
n = 6000

indices_aleatorios = random.sample(range(total_nombres), n-3000)
indices_aleatorios_2 = random.sample(range(total_nombres_2), 3000)

nombres_aleatorios = data.iloc[indices_aleatorios][0].tolist()
nombres_aleatorios_2 = data_2.iloc[indices_aleatorios_2][0].tolist()

nombres_combinados = nombres_aleatorios + nombres_aleatorios_2
random.shuffle(nombres_combinados)

# Define el rango de los distintos 'm' que vamos a testear y graficar
m_values = range(100000, 1000001, 100000)

# Para graficar tenemos que guardar los tiempos de ejecucion y porcentajes de error
# Probamos los k desde 1 a 10
for k in range(1,11):
    execution_times = []
    error_percentages = []
    for m in m_values:
        t, error = test(m, k, n, nombres_combinados)
        execution_times.append(t)
        error_percentages.append(error)


    # Ploteamos el execution time vs. m
    plt.plot(m_values, execution_times)
    plt.xlabel('m')
    plt.ylabel('Execution Time')
    plt.title('Execution Time vs. m for k='+ str(k))
    plt.savefig('execution_time_k' + str(k) + '.png')
    plt.close()

    # Ploteamos el error percentage vs. m
    plt.plot(m_values, error_percentages)
    plt.xlabel('m')
    plt.ylabel('error_percentages')
    plt.title('error_percentages vs. m for k='+ str(k))
    plt.savefig('error_percentages_k' + str(k) + '.png')
    plt.close()
