import bisect

def arbol_online(stream):
    """
    Procesamiento online usando estructura tipo árbol balanceado
    """
    estructura = []

    for x, y in stream:
        # Usamos GPA como clave (puede cambiarse)
        clave = x[-1]

        # Inserción ordenada
        bisect.insort(estructura, clave)

        # Búsqueda logarítmica
        _ = bisect.bisect_left(estructura, clave)
