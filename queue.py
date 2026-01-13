import csv
from collections import deque

cola = deque()

with open("dataStudents.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        cola.append(fila)

print("Dataset cargado en la cola:")
print(cola)

'''
Etnia: La etnia de los estudiantes, codificada de la siguiente manera:
    0: Caucásico
    1: Afroamericano
    2: Asiático
    3: Otros

ParentalEducación: El nivel de educación de los padres, codificado de la siguiente manera:

    0: Ninguno
    1: Escuela Secundaria
    2: Algunos Colegios
    3: Licenciatura
    4: Más alto


    Apoyo a los padres: El nivel de apoyo de los padres, codificado de la siguiente manera:
        0: Ninguno
        1: Bajo
        2: Moderado
        3: Alto
        4: Muy alto
'''