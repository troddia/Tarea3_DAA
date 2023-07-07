import matplotlib.pyplot as plt
import os
# Archivos de texto
archivos = ["resultados_m_k_n=4500/error/resultados_k5.txt", "resultados_m_k_n=6000/error/resultados_k5.txt", "resultados_m_k_n=12000/resultados_k5.txt"]

# Listas de listas para almacenar los valores de m y error por archivo
m_values_list = []
error_values_list = []
print("Directorio actual:", os.getcwd())
# Leer los archivos de texto
for archivo in archivos:
    # Listas para almacenar los valores de m y error
    m_values = []
    error_values = []
    
    with open(archivo, 'r') as file:
        # Iterar sobre cada línea del archivo
        count = 0
        for line in file:
            if count % 7 == 0:
                # Separar los valores por espacio en blanco
                values = line.split()
                m = float(values[4])
                # Agregar los valores a la lista de m_values
                m_values.append(m)
            elif count % 7 == 5:
                values = line.split()
                error = float(values[2].strip("%"))
                # Agregar los valores a la lista de error_values
                error_values.append(error)
            count += 1

    # Agregar las listas de m_values y error_values a las listas de listas
    m_values_list.append(m_values)
    error_values_list.append(error_values)

# Graficar el error según el eje "m" para cada archivo
nombres = ["N = 4500", "N = 6000", "N = 12000"]
for i in range(len(archivos)):
    plt.plot(m_values_list[i], error_values_list[i], label=nombres[i])

plt.xlabel('m')
plt.ylabel('Porcentaje de error')
plt.title('Porcentaje de error según m')
plt.legend()
plt.grid(True)
plt.savefig('Test_3N.png')
