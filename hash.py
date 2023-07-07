import matplotlib.pyplot as plt
import random
import csv
import numpy as np
import pandas as pd

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

