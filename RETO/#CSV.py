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