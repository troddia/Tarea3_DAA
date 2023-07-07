import matplotlib.pyplot as plt
import random
import csv
import numpy as np
import pandas as pd
import time

class Filter:
    def __init__(self, p, m, k):
        self.p = p
        self.m = m
        self.k = k
        self.M = np.zeros(m)
        self.hash_functions = {}

    # Función para generar k funciones de hash
    def generate_hash_functions(self):
        for i in range(self.k):
            b = random.randint(0, self.p - 1)
            a_values = []
            self.hash_functions[i] = (b, a_values)
 
    # Función que retorna el valor al aplicarle la función h_index al string
    def hash(self, string, function_index):
        b, a_values = self.hash_functions[function_index]
        hash_value = b
        for i, char in enumerate(string):
            if(i < len(a_values)):
                a = a_values[i]
            else:
                a = random.randint(1, self.p - 1) 
                a_values.append(a)

            hash_value += a * ord(char)
        hash_value %= self.p
        hash_value %= self.m
        return hash_value
    
    # Función para rellenar el filtro con los strings dentro del archivo csv_file
    def fill_filter(self, csv_file): 
        csv_file = csv.reader(open(csv_file, "r"), delimiter=",")
        for row in csv_file:
            name = row[0]
            for i in range(self.k):
                hash_value = self.hash(name, i)
                self.M[hash_value] = 1

    # Función que retorna TRUE si una string pasa el filtro, es decir, se encuentran 1s en las posiciones que indican las funciones de hash
    def pass_filter(self, string):
        for j in range(self.k):
            hash_value = self.hash(string, j)
            if (self.M[hash_value] == 0):
                return False

        return True

# TODO: review whats the best prime number
p = 1000000007    
def test(m, k, names):

    hash_family = Filter(p, m, k)

    hash_family.generate_hash_functions()

    csv_file = 'Popular-Baby-Names-Final.csv'

    hash_family.fill_filter(csv_file)

    
    
    #//
    positive = 0
    false_positive = 0
    negative = 0
    
    start_time = time.time()
    for i in range(25000):
        name = names[i]
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
    false_positive_rate = (false_positive / 25000) * 100
    with open('resultados_k'+str(k)+'.txt', 'a') as file:
        file.write("Test for m = " + str(m) + " and k = " + str(k) + "\n")
        file.write("Execution Time: " + str(execution_time) + "\n")
        file.write("Positive: " + str(positive) + "\n")
        file.write("False Positive: " + str(false_positive) + "\n")
        file.write("Negative: " + str(negative) + "\n")
        file.write("Error %: " + str(false_positive_rate) + "%\n")
        file.write("--------------------------------------------------------------" + "%\n")
    return execution_time, error_percentages
    
    #//
    
if __name__ == '__main__':

    data = pd.read_csv('Popular-Baby-Names-Final.csv', header=None) 
    data_2 = pd.read_csv('Film-Names.csv', header=None)

    total_nombres = len(data)
    total_nombres_2 = len(data_2)

    N = 3000

    indices_aleatorios = random.sample(range(total_nombres), 22000)
    indices_aleatorios_2 = random.sample(range(total_nombres_2), N)

    nombres_aleatorios = data.iloc[indices_aleatorios][0].tolist()
    nombres_aleatorios_2 = data_2.iloc[indices_aleatorios_2][0].tolist()

    nombres_combinados = nombres_aleatorios + nombres_aleatorios_2
    random.shuffle(nombres_combinados)

    # Define the range of m values and the step size
    m_values = range(100000, 1000001, 100000)

    # List to store the execution times for each m value
    for k in range(1,2):
        execution_times = []
        error_percentages = []
        for m in m_values:
            t, error = test(m, k, nombres_combinados)
            execution_times.append(t)
            error_percentages.append(error)


        # Plot the execution time vs. m
        plt.plot(m_values, execution_times)
        plt.xlabel('m')
        plt.ylabel('Execution Time')
        plt.title('Execution Time vs. m for k='+ str(k))
        plt.savefig('execution_time_k' + str(k) + '.png')
        plt.close()
