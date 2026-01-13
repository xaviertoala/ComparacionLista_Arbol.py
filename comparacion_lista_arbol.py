import csv
import pandas as pd
import time

# ==============================
# 1. Cargar el dataset
# ==============================
df = pd.read_csv("dataStudents.csv")

# ==============================
# 2. Crear LISTA (estructura lineal)
# ==============================
lista_estudiantes = []

for _, fila in df.iterrows():
    lista_estudiantes.append(
        (fila["StudentID"], fila["GPA"])
    )

# Verificación rápida
print("Primeros 5 en la lista:")
print(lista_estudiantes[:5])


# ==============================
# 3. Definir NODO del árbol
# ==============================
class Nodo:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.izq = None
        self.der = None


# ==============================
# 4. Árbol binario de búsqueda
# ==============================
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, key, value):
        self.raiz = self._insertar(self.raiz, key, value)

    def _insertar(self, nodo, key, value):
        if nodo is None:
            return Nodo(key, value)

        if key < nodo.key:
            nodo.izq = self._insertar(nodo.izq, key, value)
        else:
            nodo.der = self._insertar(nodo.der, key, value)

        return nodo

    def buscar(self, key):
        return self._buscar(self.raiz, key)

    def _buscar(self, nodo, key):
        if nodo is None:
            return None

        if nodo.key == key:
            return nodo.value

        if key < nodo.key:
            return self._buscar(nodo.izq, key)

        return self._buscar(nodo.der, key)


# ==============================
# 5. Crear el árbol con el dataset
# ==============================
df = df.sample(frac=1).reset_index(drop=True)

arbol = ArbolBinario()

for _, fila in df.iterrows():
    arbol.insertar(fila["StudentID"], fila["GPA"])

print("\nRaíz del árbol:")
print(arbol.raiz.key, arbol.raiz.value)


# ==============================
# 6. Búsqueda en LISTA
# ==============================
def buscar_en_lista(lista, key):
    for estudiante in lista:
        if estudiante[0] == key:
            return estudiante[1]
    return None


# ==============================
# 7. Comparación de búsqueda
# ==============================
id_prueba = df.iloc[0]["StudentID"]

print("\nBuscando StudentID:", id_prueba)
print("GPA desde lista:", buscar_en_lista(lista_estudiantes, id_prueba))
print("GPA desde árbol:", arbol.buscar(id_prueba))


# ==============================
# 8. Medición de tiempos
# ==============================
repeticiones = 10000
tiempo_lista = 0
tiempo_arbol = 0

for _ in range(repeticiones):
    inicio = time.perf_counter()
    buscar_en_lista(lista_estudiantes, id_prueba)
    tiempo_lista += time.perf_counter() - inicio

    inicio = time.perf_counter()
    arbol.buscar(id_prueba)
    tiempo_arbol += time.perf_counter() - inicio

print("\nRESULTADOS DE TIEMPO")
print("Tiempo promedio lista:", tiempo_lista / repeticiones)
print("Tiempo promedio árbol:", tiempo_arbol / repeticiones)
