import time
import csv
from estructura_listas import lista_online
from estructura_arboles import arbol_online

# ==========================
# Stream online desde CSV
# ==========================
def dataset_stream_csv(ruta_csv):
    """
    Lee el dataset línea por línea (online)
    """
    with open(ruta_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Variables predictoras (X)
            x = [
                int(row["Age"]),
                int(row["Gender"]),
                int(row["Ethnicity"]),
                int(row["ParentalEducation"]),
                float(row["StudyTimeWeekly"]),
                int(row["Absences"]),
                int(row["Tutoring"]),
                int(row["ParentalSupport"]),
                int(row["Extracurricular"]),
                int(row["Sports"]),
                int(row["Music"]),
                int(row["Volunteering"]),
                float(row["GPA"])
            ]

            # Variable objetivo (y)
            y = float(row["GradeClass"])

            yield x, y

# ==========================
# Medición de tiempo
# ==========================
def medir_tiempo(funcion, ruta_csv, limite=None):
    """
    limite: número máximo de instancias a procesar
    """
    inicio = time.perf_counter()

    stream = dataset_stream_csv(ruta_csv)

    if limite:
        from itertools import islice
        stream = islice(stream, limite)

    funcion(stream)

    fin = time.perf_counter()
    return fin - inicio

# ==========================
# Experimento por cargas
# ==========================
ruta_dataset = "dataStudents.csv"  # <-- TU ARCHIVO
cargas = [100, 500, 1000, 2000, 3392]

print(f"{'Carga':>8} | {'Lista (s)':>12} | {'Árbol (s)':>12}")
print("-" * 40)

for c in cargas:
    t_lista = medir_tiempo(lista_online, ruta_dataset, c)
    t_arbol = medir_tiempo(arbol_online, ruta_dataset, c)

    print(f"{c:>8} | {t_lista:>12.6f} | {t_arbol:>12.6f}")
