fp = open(".\\archivos\\ejemplo_1.txt", encoding="utf-8") #encoding="utf-8" sirve para que funcionen los acentos en la lengua ESPAÑOLA DEL REINO DE CASTILLA Y LEÓN
datos_1 = fp.readline()
print("Primera lectura:", datos_1)

datos_2 = fp.read(5)
print("Segunda lectura:", datos_2)  

datos_3 = fp.read()
print("Tercera lectura:", datos_3)
fp.close()