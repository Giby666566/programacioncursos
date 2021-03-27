
#Leemos un archivo con formato "r"
#guardamos su contenido en una variable llamada texto
with open("carros.txt","r") as archivo:
    #Obteniendolo todo
    texto=archivo.read()
    print(texto)
    #Linea por linea
    #for linea in archivo:
     #   print(linea, end="")

lista=["a","b","c"]
print()
for elemento in lista:
    print(elemento)
