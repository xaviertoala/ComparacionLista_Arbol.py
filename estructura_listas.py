import csv
import numpy as np
import time
from sklearn.linear_model import SGDRegressor  # reemplaza PassiveAggressiveRegressor

# Ruta a tu CSV
ruta_csv = 'dataStudents.csv'

# Función para cargar dataset en listas
def cargar_dataset_en_listas():
    X_list = []
    y_list = []
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
            X_list.append(features)
            y_list.append(float(row["GPA"]))
    return X_list, y_list

# Escenarios: número de ejecuciones
escenarios = [20, 50, 75, 100, 150]

for N in escenarios:
    tiempos_ejecuciones = []

    for ejec in range(N):
        start_time = time.time()

        # Cargar dataset en listas
        X_list, y_list = cargar_dataset_en_listas()

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

        # Entrenamiento incremental
        for i in range(len(X_list)):
            xi = np.array(X_list[i]).reshape(1, -1)
            yi = np.array([y_list[i]])
            model.partial_fit(xi, yi)

        end_time = time.time()
        tiempos_ejecuciones.append(end_time - start_time)

    promedio_tiempo = sum(tiempos_ejecuciones) / len(tiempos_ejecuciones)
    print(f"Escenario {N} ejecuciones: promedio de tiempo por ejecución = {promedio_tiempo:.6f} s")
