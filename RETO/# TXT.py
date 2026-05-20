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