fp = open(".\\archivos\\ejemplo_2.txt", encoding="utf-8") #encoding="utf-8" sirve para que funcionen los acentos en la lengua ESPAÑOLA DEL REINO DE CASTILLA Y LEÓN
datos_1 = fp.readlines()
print("Primera lectura:", datos_1)

datos_2 = fp.read[]