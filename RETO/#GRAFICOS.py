#   GRÁFICOS

def separar_palabras(texto):
    palabras = []
    palabra = ""
    for c in texto:
        if c in " \n\t\r":
            if palabra != "":
                palabras.append(palabra)
                palabra = ""
        else:
            palabra += c
    if palabra != "":
        palabras.append(palabra)
    return palabras

def separar_por(texto, separador):
    partes = []
    actual = ""
    for c in texto:
        if c == separador:
            partes.append(actual)
            actual = ""
        else:
            actual += c
    partes.append(actual)
    return partes

def leer_filas_csv(nombre):
    archivo = open(nombre, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    filas = []
    for linea in lineas:
        linea = linea.strip("\n")
        filas.append(separar_por(linea, ","))
    return filas

def grafico_top_palabras(nombre):
    archivo = open(nombre, "r", encoding="utf-8")
    texto = archivo.read().lower()
    archivo.close()

    stopwords = ["de", "el", "la", "los", "las", "un", "una", "en", "y", "a",
                 "se", "que", "con", "del", "por", "es", "su", "al", "lo", "le"]

    conteo = {}

    for palabra in separar_palabras(texto):
        palabra = palabra.strip(".,;:!?\"'()[]")
        if palabra != "" and palabra not in stopwords:
            if palabra in conteo:
                conteo[palabra] += 1
            else:
                conteo[palabra] = 1

    top_palabras = []
    top_frecuencias = []

    for i in range(10):
        mayor_palabra = ""
        mayor_frecuencia = 0

        for palabra in conteo:
            if conteo[palabra] > mayor_frecuencia and palabra not in top_palabras:
                mayor_palabra = palabra
                mayor_frecuencia = conteo[palabra]

        if mayor_palabra != "":
            top_palabras.append(mayor_palabra)
            top_frecuencias.append(mayor_frecuencia)

    plt.figure(figsize=(10, 6))
    plt.barh(top_palabras, top_frecuencias)
    plt.xlabel("Frecuencia")
    plt.title("Top 10 palabras más frecuentes")
    plt.gca().invert_yaxis()

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    ruta = os.path.join("outputs", "grafico1.png")
    plt.savefig(ruta)
    plt.close()

    print("Gráfico guardado en:", ruta)

def grafico_longitud_lineas(nombre):
    archivo = open(nombre, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    longitudes = []
    for linea in lineas:
        linea = linea.strip("\n")
        longitudes.append(len(linea))

    plt.figure(figsize=(10, 6))
    plt.hist(longitudes, bins=10)
    plt.xlabel("Longitud de línea")
    plt.ylabel("Cantidad de líneas")
    plt.title("Distribución de longitud de líneas")

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    ruta = os.path.join("outputs", "grafico2.png")
    plt.savefig(ruta)
    plt.close()

    print("Gráfico guardado en:", ruta)

def grafico_lineas_csv(nombre):
    datos = leer_filas_csv(nombre)
    encabezados = datos[0]

    print("\nColumnas disponibles:")
    for i in range(len(encabezados)):
        print(i, "-", encabezados[i])

    col_x = int(input("Número de columna X: "))
    col_y = int(input("Número de columna Y: "))

    if col_x >= len(encabezados) or col_y >= len(encabezados):
        print("Columnas no válidas.")
        return

    eje_x = []
    eje_y = []

    for fila in datos[1:]:
        if len(fila) > col_x and len(fila) > col_y:
            x = fila[col_x].strip().strip('"')
            y = fila[col_y].strip().strip('"')

            if x != "" and y != "":
                try:
                    eje_x.append(x)
                    eje_y.append(float(y))
                except:
                    pass

    plt.figure(figsize=(10, 6))
    plt.plot(eje_x, eje_y)
    plt.xlabel(encabezados[col_x])
    plt.ylabel(encabezados[col_y])
    plt.title("Evolución temporal / tendencia")

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    ruta = os.path.join("outputs", "grafico3.png")
    plt.savefig(ruta)
    plt.close()

    print("Gráfico guardado en:", ruta)

def grafico_pastel_csv(nombre):
    datos = leer_filas_csv(nombre)
    encabezados = datos[0]

    print("\nColumnas disponibles:")
    for i in range(len(encabezados)):
        print(i, "-", encabezados[i])

    col = int(input("Número de columna categórica: "))

    if col >= len(encabezados):
        print("Columna no válida.")
        return

    conteo = {}

    for fila in datos[1:]:
        if len(fila) > col:
            categoria = fila[col].strip().strip('"')

            if categoria != "":
                if categoria in conteo:
                    conteo[categoria] += 1
                else:
                    conteo[categoria] = 1

    if len(conteo) == 0:
        print("No hay categorías válidas.")
        return

    etiquetas = list(conteo.keys())
    valores = list(conteo.values())

    plt.figure(figsize=(8, 8))
    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%")
    plt.title("Distribución de " + encabezados[col])

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    ruta = os.path.join("outputs", "grafico4.png")
    plt.savefig(ruta)
    plt.close()

    print("Gráfico guardado en:", ruta)

def grafico_scatter_csv(nombre):
    datos = leer_filas_csv(nombre)
    encabezados = datos[0]

    print("\nColumnas disponibles:")
    for i in range(len(encabezados)):
        print(i, "-", encabezados[i])

    col_x = int(input("Número de columna X: "))
    col_y = int(input("Número de columna Y: "))

    if col_x >= len(encabezados) or col_y >= len(encabezados):
        print("Columnas no válidas.")
        return

    eje_x = []
    eje_y = []

    for fila in datos[1:]:
        if len(fila) > col_x and len(fila) > col_y:
            x = fila[col_x].strip().strip('"')
            y = fila[col_y].strip().strip('"')

            if x != "" and y != "":
                try:
                    eje_x.append(float(x))
                    eje_y.append(float(y))
                except:
                    pass

    if len(eje_x) == 0:
        print("No hay datos numéricos válidos.")
        return

    plt.figure(figsize=(10, 6))
    plt.scatter(eje_x, eje_y)
    plt.xlabel(encabezados[col_x])
    plt.ylabel(encabezados[col_y])
    plt.title("Gráfico de dispersión")

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    ruta = os.path.join("outputs", "grafico5.png")
    plt.savefig(ruta)
    plt.close()

    print("Gráfico guardado en:", ruta)