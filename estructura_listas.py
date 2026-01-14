def lista_online(stream):
    """
    Procesamiento online usando estructura lineal (lista)
    Inserción secuencial + búsqueda
    """
    estructura = []

    for x, y in stream:
        # Inserción online
        estructura.append(x)

        # Acceso / búsqueda
        _ = x in estructura
