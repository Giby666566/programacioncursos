nombre=input("Dame el nombre de un archivo para copiarlo\n")
nuevo=input("Dame el nombre de la copia\n")
with open(nombre,"rb") as f:
    with open(nuevo,"wb") as f1:
        for linea in f:
            f1.write(linea)
