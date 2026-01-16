import csv
import numpy as np
import time
from sklearn.linear_model import SGDRegressor  # modelo online estilo Passive-Aggressive

# -----------------------------
# Definir la estructura del árbol
# -----------------------------
class Nodo:
    def __init__(self, features, gpa):
        self.features = features
        self.gpa = gpa
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    # Insertar por valor de GPA como criterio (solo ejemplo)
    def insertar(self, features, gpa):
        nuevo_nodo = Nodo(features, gpa)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_rec(self.raiz, nuevo_nodo)

    def _insertar_rec(self, actual, nuevo_nodo):
        if nuevo_nodo.gpa < actual.gpa:
            if actual.izquierda is None:
                actual.izquierda = nuevo_nodo
            else:
                self._insertar_rec(actual.izquierda, nuevo_nodo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo_nodo
            else:
                self._insertar_rec(actual.derecha, nuevo_nodo)

    # Recorrido inorder para obtener datos en orden
    def recorrido_inorder(self):
        datos = []
        def _inorder(nodo):
            if nodo:
                _inorder(nodo.izquierda)
                datos.append((nodo.features, nodo.gpa))
                _inorder(nodo.derecha)
        _inorder(self.raiz)
        return datos

# -----------------------------
# Función para cargar CSV en el árbol
# -----------------------------
ruta_csv = 'dataStudents.csv'
def cargar_dataset_en_arbol(ruta_csv):
    arbol = Arbol()
    with open(ruta_csv, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            features = [
                float(row["Age"]),
                float(row["Gender"]),
                float(row["Ethnicity"]),
                float(row["ParentalEducation"]),
                float(row["StudyTimeWeekly"]),
                float(row["Absences"]),
                float(row["Tutoring"]),
                float(row["ParentalSupport"]),
                float(row["Extracurricular"]),
                float(row["Sports"]),
                float(row["Music"]),
                float(row["Volunteering"])
            ]
            gpa = float(row["GPA"])
            arbol.insertar(features, gpa)
    return arbol

# -----------------------------
# Escenarios de ejecuciones
# -----------------------------
escenarios = [50, 100, 200]  # número de ejecuciones
ruta_csv = 'dataStudents.csv'

for N in escenarios:
    tiempos_ejecuciones = []

    for ejec in range(N):
        start_time = time.time()

        # Cargar dataset en árbol
        arbol = cargar_dataset_en_arbol(ruta_csv)
        datos = arbol.recorrido_inorder()  # obtener features y gpa en orden

        # Crear modelo SGDRegressor estilo Passive-Aggressive
        model = SGDRegressor(
            loss='epsilon_insensitive',
            penalty=None,
            learning_rate='pa1',
            eta0=1.0,
            max_iter=1,
            warm_start=True,
            random_state=42
        )

        # Entrenamiento incremental recorriendo el árbol
        for features, gpa in datos:
            xi = np.array(features).reshape(1, -1)
            yi = np.array([gpa])
            model.partial_fit(xi, yi)

        end_time = time.time()
        tiempos_ejecuciones.append(end_time - start_time)

    promedio_tiempo = sum(tiempos_ejecuciones) / len(tiempos_ejecuciones)
    print(f"Escenario {N} ejecuciones: promedio de tiempo por ejecución = {promedio_tiempo:.6f} s")
