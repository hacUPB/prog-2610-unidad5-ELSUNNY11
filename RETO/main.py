import os
import csv
import re
import matplotlib.pyplot as plt


ruta_base = "D:\\UNIVERSIDAD\\PROGRAMACION\\prog-2610-unidad5-ELSUNNY11\\RETO"


def listar_archivos(ruta):
    """Lista archivos .csv y .txt en la carpeta indicada."""
    if not os.path.exists(ruta):
        print("La ruta no existe. Revisa la variable 'ruta_base'.")
        return []
    archivos = []
    for nombre in os.listdir(ruta):
        if nombre.lower().endswith(".csv") or nombre.lower().endswith(".txt"):
            archivos.append(nombre)
    if len(archivos) == 0:
        print("No se encontraron archivos .csv ni .txt en la carpeta.")
    else:
        print("\nArchivos encontrados:")
        for a in archivos:
            print("-", a)
    return archivos

# FUNCIONES PARA ARCHIVOS .TXT

def contar_palabras_y_caracteres(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo no encontrado.")
        return
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read()
    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres_con = len(texto)
    num_caracteres_sin = len(texto.replace(" ", ""))
    print("\nResultados:")
    print("Número de palabras:", num_palabras)
    print("Caracteres (con espacios):", num_caracteres_con)
    print("Caracteres (sin espacios):", num_caracteres_sin)


def reemplazar_palabra_txt(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo no encontrado.")
        return
    palabra_buscar = input("Palabra a buscar: ")
    palabra_nueva = input("Palabra por la que se reemplazará: ")
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read()
    if palabra_buscar not in texto:
        print("La palabra buscada no está presente en el archivo.")
        return
    texto_nuevo = texto.replace(palabra_buscar, palabra_nueva)
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write(texto_nuevo)
    print("Reemplazo completado y guardado en el archivo.")


def histograma_vocales_txt(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo no encontrado.")
        return
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read().lower()
    vocales = ["a", "e", "i", "o", "u"]
    conteo = []
    for v in vocales:
        conteo.append(texto.count(v))
    print("\nOcurrencias de vocales:")
    for v, c in zip(vocales, conteo):
        print(f"{v}: {c}")
    plt.bar(vocales, conteo, color="skyblue", edgecolor="black")
    plt.title("Histograma de vocales")
    plt.xlabel("Vocal")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()


def submenu_txt():
    archivos = []
    for f in os.listdir(ruta_base):
        if f.lower().endswith(".txt"):
            archivos.append(f)
    if len(archivos) == 0:
        print("No se encontraron archivos .txt en la carpeta.")
        return
    print("\nArchivos .txt disponibles:")
    for i, a in enumerate(archivos, start=1):
        print(f"{i}. {a}")
    sel = input("Selecciona el número del archivo .txt (o escribe el nombre): ")
    if sel.isdigit():
        idx = int(sel) - 1
        if 0 <= idx < len(archivos):
            nombre = archivos[idx]
        else:
            print("Selección inválida.")
            return
    else:
        nombre = sel
        if nombre not in archivos:
            print("Archivo no encontrado.")
            return
    ruta_archivo = os.path.join(ruta_base, nombre)
    while True:
        print("\n--- SUBMENÚ .TXT ---")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar una palabra")
        print("3. Histograma de vocales (gráfico)")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            contar_palabras_y_caracteres(ruta_archivo)
        elif opcion == "2":
            reemplazar_palabra_txt(ruta_archivo)
        elif opcion == "3":
            histograma_vocales_txt(ruta_archivo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")