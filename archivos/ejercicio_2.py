fp = open(".\\archivos\\ejemplo_2.txt", encoding="utf-8") #encoding="utf-8" sirve para que funcionen los acentos en la lengua ESPAÑOLA DEL REINO DE CASTILLA Y LEÓN
lista = fp.readlines()
fp.close
print(lista)

for linea in lista:
    print(linea[0])