import pandas as pd
import time
import random

# ==============================
# 1. Cargar el dataset
# ==============================
df = pd.read_csv("dataStudents.csv")

# Convertir StudentID a entero para evitar problemas de float
df["StudentID"] = df["StudentID"].astype(int)

# ==============================
# 2. Crear LISTA (estructura lineal)
# ==============================
lista_estudiantes = [(int(fila["StudentID"]), fila["GPA"]) for _, fila in df.iterrows()]

# Verificación rápida
print("Primeros 5 en la lista:")
print(lista_estudiantes[:5])

# ==============================
# 3. Definir NODO del árbol
# ==============================
class Nodo:
    def __init__(self, key, value):
        self.key = key
        self.values = [value]  # lista de GPA para duplicados
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
        elif key > nodo.key:
            nodo.der = self._insertar(nodo.der, key, value)
        else:
            nodo.values.append(value)  # duplicados
        return nodo

    def buscar(self, key):
        nodo = self._buscar(self.raiz, key)
        return nodo.values if nodo is not None else None

    def _buscar(self, nodo, key):
        if nodo is None:
            return None
        if nodo.key == key:
            return nodo
        if key < nodo.key:
            return self._buscar(nodo.izq, key)
        return self._buscar(nodo.der, key)

# ==============================
# 5. Crear el árbol con el dataset
# ==============================
df = df.sample(frac=1).reset_index(drop=True)  # barajar los datos

arbol = ArbolBinario()
for _, fila in df.iterrows():
    arbol.insertar(fila["StudentID"], fila["GPA"])

print("\nRaíz del árbol:")
print(arbol.raiz.key, arbol.raiz.values)

# ==============================
# 6. Búsqueda en LISTA
# ==============================
def buscar_en_lista(lista, key):
    resultados = [gpa for sid, gpa in lista if sid == key]
    return resultados if resultados else None

# ==============================
# 7. Comparación de búsqueda
# ==============================
# Elegir un ID aleatorio del dataset
id_prueba = int(random.choice(lista_estudiantes)[0])

print("\nBuscando StudentID:", id_prueba)
print("GPA desde lista:", buscar_en_lista(lista_estudiantes, id_prueba))
print("GPA desde árbol:", arbol.buscar(id_prueba))

# ==============================
# 8. Medición de tiempos con búsquedas aleatorias
# ==============================
repeticiones = 10000

# Generar IDs aleatorios para cada repetición
ids_aleatorios = [int(random.choice(lista_estudiantes)[0]) for _ in range(repeticiones)]

# Lista
inicio = time.perf_counter()
for id_buscado in ids_aleatorios:
    buscar_en_lista(lista_estudiantes, id_buscado)
tiempo_lista = time.perf_counter() - inicio

# Árbol
inicio = time.perf_counter()
for id_buscado in ids_aleatorios:
    arbol.buscar(id_buscado)
tiempo_arbol = time.perf_counter() - inicio

print("\nRESULTADOS DE TIEMPO")
print("Tiempo promedio lista:", tiempo_lista / repeticiones)
print("Tiempo promedio árbol:", tiempo_arbol / repeticiones)
