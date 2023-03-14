import numpy as np
import pandas as pd

data = [
    50, 50, 47, 97, 49, 3, 53, 42, 26, 74, 82, 62, 37, 15, 70, 27, 36, 35, 48,
    52, 63, 64
]
grades = np.array(data)
# print(data)
# print(grades)

# Diferencia entre una lista y un numpy.array(lista)
# print(type(data), " x 2 : ", data * 2)
# print(type(grades), " x 2 : ", grades * 2)

# Dimension del Array (22,) -> Una sola fila de 22 elementos
# print(grades.shape)

#Promedio de valores
promedio = grades.mean()
print('Promedio: {:.2f}'.format(promedio))
