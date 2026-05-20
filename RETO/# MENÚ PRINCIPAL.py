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