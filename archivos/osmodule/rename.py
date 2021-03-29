import os

#OJO, RENAME RECIBE COMO ARGUMENTOS LAS DIRECCIONES DE LOS ARCHIVOS QUE QUIERO CAMBIAR, NO LOS NOMBRES
nombreactual=input("Dame el nombre de un archivo o carpeta para cambiarle el nombre\n")
nuevonombre=input("Dame el nuevo nombre de tu archivo o carpeta")

os.rename(nombreactual,nuevonombre)