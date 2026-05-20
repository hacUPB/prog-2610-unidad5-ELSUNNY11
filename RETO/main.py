import os
import matplotlib.pyplot as plt

# Cambiar el directorio de trabajo a donde está main.py (HECHO CON IA)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Registro global de archivos explorados
archivos_registrados = {}


#   TEXTO (.txt)

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

def es_fecha(palabra):
    palabra = palabra.strip(".,;:!?\"'()")
    for sep in ["/", "-"]:
        if sep in palabra:
            partes = separar_por(palabra, sep)
            if len(partes) == 3:
                dia, mes, año = partes[0], partes[1], partes[2]
                if dia.isdigit() and mes.isdigit() and año.isdigit():
                    if len(año) == 4 and 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12:
                        return True
    return False

def leer_txt(nombre):
    archivo = open(nombre, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    texto = ""
    for linea in lineas:
        texto += linea

    palabras     = separar_palabras(texto)
    sin_espacios = ""
    for c in texto:
        if c not in " \n":
            sin_espacios += c

    conteo = {}
    for p in palabras:
        p = p.lower().strip(".,;:!?\"'()")
        if p != "":
            if p in conteo: conteo[p] += 1
            else: conteo[p] = 1

    claves = list(conteo.keys())
    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):
            if conteo[claves[j]] > conteo[claves[i]]:
                claves[i], claves[j] = claves[j], claves[i]

    print(f"\n  Total líneas             : {len(lineas)}")
    print(f"  Total palabras           : {len(palabras)}")
    print(f"  Caracteres con espacios  : {len(texto)}")
    print(f"  Caracteres sin espacios  : {len(sin_espacios)}")
    print("  Top 5 palabras frecuentes:")
    for i in range(min(5, len(claves))):
        print(f"    {i+1}. '{claves[i]}' — {conteo[claves[i]]} veces")

def contar_palabras_txt(nombre):
    archivo = open(nombre, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    texto = ""
    for linea in lineas:
        texto += linea

    palabras = separar_palabras(texto)
    print(f"Palabras: {len(palabras)}  |  Líneas: {len(lineas)}")

def buscar_palabra_txt(nombre):
    archivo = open(nombre, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    errores, c404, fechas = [], [], []
    for i in range(len(lineas)):
        linea = lineas[i].rstrip()
        if "ERROR" in lineas[i].upper(): errores.append((i + 1, linea))
        if "404" in lineas[i]: c404.append((i + 1, linea))
        for palabra in separar_palabras(lineas[i]):
            if es_fecha(palabra): fechas.append((i + 1, palabra, linea))

    print(f"\n  Coincidencias 'ERROR' : {len(errores)}")
    for num, linea in errores: print(f"    Línea {num}: {linea}")
    print(f"\n  Coincidencias '404'   : {len(c404)}")
    for num, linea in c404: print(f"    Línea {num}: {linea}")
    print(f"\n  Fechas encontradas    : {len(fechas)}")
    for num, fecha, linea in fechas: print(f"    Línea {num}: {fecha} → {linea}")


def pedir_archivo(extension):
    global archivos_registrados
    disponibles = {k: v for k, v in archivos_registrados.items() if v.endswith(extension)}
    if disponibles:
        print(f"  Archivos {extension} disponibles:")
        for num, ruta in disponibles.items():
            print(f"    [{num}] {os.path.basename(ruta)}")
        entrada = input(f"  Número o ruta del archivo {extension}: ").strip()
    else:
        print(f"  (Directorio actual: {os.getcwd()})")
        entrada = input(f"  Ruta del archivo {extension}: ").strip()

    if entrada.isdigit() and int(entrada) in archivos_registrados:
        nombre = archivos_registrados[int(entrada)]
    else:
        nombre = entrada

    if not os.path.exists(nombre):
        print(f"  Error: '{nombre}' no encontrado.")
        return None
    print(f"  Archivo cargado: {os.path.basename(nombre)}")
    return nombre

def submenu_txt():
    nombre = pedir_archivo(".txt")
    if nombre is None: return
    while True:
        print("\n-- Submenú TXT --\n1. Leer\n2. Contar palabras\n3. Buscar patrones\n4. Gráfico top 10 palabras\n5. Gráfico longitud de líneas\n6. Volver")
        opcion = input("Opción: ").strip()
        if   opcion == "1": leer_txt(nombre)
        elif opcion == "2": contar_palabras_txt(nombre)
        elif opcion == "3": buscar_palabra_txt(nombre)
        elif opcion == "4": grafico_top_palabras(nombre)
        elif opcion == "5": grafico_longitud_lineas(nombre)
        elif opcion == "6": break
        else: print("Opción no válida.")

#   CSV

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

def leer_csv(nombre):
    archivo = open(nombre, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()
    filas = []
    for linea in lineas:
        filas.append(separar_por(linea.rstrip("\n"), ","))
    return filas

def ver_primeras_ultimas(nombre):
    if not os.path.exists(nombre):
        print("Error: archivo no encontrado.")
        return
    datos = leer_csv(nombre)
    total = len(datos)
    print("\n  Primeras 10 filas ")
    limite = 11 if total >= 11 else total
    for fila in datos[:limite]: print("  " + " | ".join(fila))
    print("\n  Últimas 5 filas ")
    inicio = total - 5 if total > 5 else 1
    for fila in datos[inicio:]: print("  " + " | ".join(fila))

def estadisticas_columna(nombre):
    datos = leer_csv(nombre)
    encabezados = datos[0]
    print("\n  Columnas disponibles:")
    for i in range(len(encabezados)): print(f"    [{i}] {encabezados[i]}")

    col = input("  Número de columna: ").strip()
    if not col.isdigit() or int(col) >= len(encabezados):
        print("  Columna no válida."); return
    col = int(col)

    valores = []
    for fila in datos[1:]:
        if col < len(fila):
            celda = fila[col].strip().strip('"')
            if celda != "" and celda != "None" and celda != "null":
                try: valores.append(float(celda))
                except ValueError: pass

    if len(valores) == 0: print("  No se encontraron valores numéricos."); return

    total = len(valores)
    suma = 0
    for v in valores: suma += v
    promedio = suma / total

    maximo = valores[0]
    minimo = valores[0]
    for v in valores:
        if v > maximo: maximo = v
        if v < minimo: minimo = v

    copia = list(valores)
    for i in range(len(copia)):
        for j in range(i + 1, len(copia)):
            if copia[j] < copia[i]: copia[i], copia[j] = copia[j], copia[i]
    mitad = len(copia) // 2
    mediana = (copia[mitad - 1] + copia[mitad]) / 2 if len(copia) % 2 == 0 else copia[mitad]

    print(f"\n  Columna          : {encabezados[col]}")
    print(f"  Total válidos    : {total}")
    print(f"  Promedio         : {promedio:.2f}")
    print(f"  Mediana          : {mediana:.2f}")
    print(f"  Máximo           : {maximo:.2f}")
    print(f"  Mínimo           : {minimo:.2f}")

def submenu_csv():
    nombre = pedir_archivo(".csv")
    if nombre is None: return
    while True:
        print("\n Submenú CSV \n1. Primeras 10 y últimas 5\n2. Estadísticas de columna\n3. Gráfico de líneas\n4. Gráfico de pastel\n5. Gráfico scatter\n6. Volver")
        op = input("Opción: ").strip()
        try:
            if op == "1": ver_primeras_ultimas(nombre)
            elif op == "2": estadisticas_columna(nombre)
            elif op == "3": grafico_lineas_csv(nombre)
            elif op == "4": grafico_pastel_csv(nombre)
            elif op == "5": grafico_scatter_csv(nombre)
            elif op == "6": break
            else: print("Opción no válida.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

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

# MENÚ PRINCIPAL
# EXPLORA DIRECTORIO
def explorar_directorio():
    global archivos_registrados
    ruta = input("Ingresa la ruta del directorio: ")
    
    if not os.path.exists(ruta):
        print('Error: "Ruta no válida"')
        return

    archivos_registrados = {}
    numero = 1

    print(f"\nArchivos .txt y .csv en '{ruta}':")
    for archivo in os.listdir(ruta):
        if archivo.endswith(".txt") or archivo.endswith(".csv"):
            ruta_completa = os.path.join(ruta, archivo)
            archivos_registrados[numero] = ruta_completa
            print(f" [{numero}] {archivo}")
            numero += 1

    print("  (Usa el número al ingresar un archivo)")


def main():
    while True:
        print("\n MENÚ PRINCIPAL \n1. Explorar directorio\n2. Procesar textos (.txt)\n3. Analizar datasets (.csv)\n4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            explorar_directorio()
        elif opcion == "2":
            submenu_txt()
        elif opcion == "3":
            submenu_csv()
        elif opcion == "4":
            print("¡Chao Henry!")
            break
        else:
            print("Opción no válida.")


main()
