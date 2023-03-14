import numpy as np
import pandas as pd

data = [
    50, 50, 47, 97, 49, 3, 53, 42, 26, 74, 82, 62, 37, 15, 70, 27, 36, 35, 48,
    52, 63, 64
]
# Creando un objeto numpy.array
grades = np.array(data)
# print(data)
# print(grades)

#* Diferencia entre una lista y un numpy.array(lista) -> La diferencia principal es que una lista no se puede operar por si sola mientras que un array puede ser operado entre arrays y escalares EJemplo:
#? Si imprimimos una lista por 2 duplica el numero de componentes
# print(type(data), " x 2 : ", data * 2)
#? Si imprimimos un array por dos, devuelve cada uno de los indices por el escalar
# print(type(grades), " x 2 : ", grades * 2)

#? Para poder vcisualizar la dimension de la matriz podemos usar el metodo shape sin argumentos
# Dimension del Array (22,) -> Una sola fila de 22 elementos
# print(grades.shape)

#Operando con metodos de numpy.array.mean() - PROMEDIO
promedio = grades.mean()
print('Promedio: {:.2f}'.format(promedio))

#Para poder visualizar cada elemento dentro del array podemos hacerlo igual
# que en una lista #array[posicion] De una dimension
print("Imprimiento la pos[0]", grades[0])

#Para agregar mas dimensiones o valores a nuestro array
#! Importante que las dimensiones de los arrays sean iguales
study_hours = [
    10.0, 11.5, 9.0, 16.0, 9.25, 1.0, 11.5, 9.0, 8.5, 14.5, 15.5, 13.75, 9.0,
    8.0, 15.5, 8.0, 9.0, 6.0, 10.0, 12.0, 12.5, 12.0
]
student_data = np.array([study_hours, grades])
# print(student_data)
# print(student_data.shape)

# Ahora nuestra matriz es de 2 x 22 o dos arrays de 2 filas de 22 elementos, para poder visualizar los datos ahora tenemos que especificar la posicion en dos dimensiones (Fila y columna)
fila = 1
columna = 2
#print(f"Imprimiendo el elemento en Fila: {fila}, Columna: {columna} -> {student_data[fila][columna]}")

# Operaciones en matrices
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()
print("Promedios por filas", "Promedio horas de estudio: ", avg_study,
      "Promedio calificaciones: ", avg_grade)

#! numpy tiene varios metodos mas que debemos ir explorando

#* UTILIAZNDO PANDAS COMO VISUALIZADOR DE DATOS

#? Creamos un DataFrame con pandas.
df_students = pd.DataFrame({
    'Name': [
        'Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic',
        'Jimmie', 'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana',
        'Kian', 'Jenny', 'Jakeem', 'Helena', 'Ismat', 'Anila', 'Skye',
        'Daniel', 'Aisha'
    ],
    'StudyHours':
    student_data[0],
    'Grade':
    student_data[1]
})
#? Para imprimir la tabla.
#print(df_students)

#? Para imprimir solo una cantidad podemos usar el metodo loc o iloc
# Podemos usar loc para imprimir una fila
# print(df_students.loc[5])
# loc imprime una 0,1,2,3,4,y 5 (6 elementos) en un rango
# print("_______loc________")
# print(df_students.loc[0:5])
# iloc imprime 0,1,2,3 y 4  (5 elementos) en un rango
# print("_______iloc________")
# print(df_students.iloc[0:5])

#? Para imprimir una cantidad determinada de columnas podemos especificar
#--> Elemento 1 muestra columna 1 y 2
print("_____df_stundents.iloc[1,[1,2]]____")
print(df_students.iloc[1, [0, 1, 2]])

#? Tambien podemos especificar que valor de la columna a mostrar por el nombre
print("____df_students.loc[0,'Grade']______")
print(df_students.loc[0, 'Grade'])

#? Esta es otra forma o truco de encontrar datos por una expresion para filtrar
print("____df_students.loc[df_students['Name']=='Aisha']____")
print(df_students.loc[df_students['Name'] == 'Aisha'])

#! no es necesario colocar el metodo loc, se lo puede omitir
print("____df_students[df_students['Name']=='Aisha']____")
print(df_students[df_students['Name'] == 'Aisha'])

#? Tambien podemos hacer uso de el metodo query que ofrece panda
print("_______df_students.query('Name==\"Aisha\"')____")
print(df_students.query('Name=="Aisha"'))

#Podemos cargar Dataframes desde algun archivo csv
df_students = pd.read_csv('grades.csv', delimiter=',', header='infer')
print("__________df_stundents.head()_____________")
print(df_students.head())

# Podemos ver que elementos son null con el metodo .isnull()
print("______df_studenst.isnull()_____")
print(df_students.isnull())

# Podemos contar la cantidad de valores null
print("________df_students.isnull().sum()___")
print(df_students.isnull().sum())

# Una de las formas de corregir un valor null es reemplazandolo por un promedio
print("___df_students.StudyHours.fillna(df_students.Studyours.mean())___")
print(df_students.StudyHours.fillna(df_students.StudyHours.mean()))

# Otra forma es eliminando si no tenemos un valor que pueda ser absolutamente correcto
print("ELIMINANDO FILAS SIN ELEMENTOS")
print("_____df_students = df_students.dropna(axis=0, how='any')______")
df_students = df_students.dropna(axis=0, how='any')
print(df_students)

#! podemos realizar operaciones de diferentes formas llamando a la columna por nombre o como propiedad
mean_study = df_students['StudyHours'].mean()
mean_grade = df_students.Grade.mean()
print('Promedio de horas estudiadas {:.2f} y promedio de notas {:.2f}'.format(
    mean_study, mean_grade))

print("Imprimir tablas filtradas")
print(df_students[df_students.StudyHours > mean_study])

print("Operando sobre dataFrame obtenido ")
print(df_students[df_students.StudyHours > mean_study][1, 2])
