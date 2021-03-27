import os
print("BIENVENIDO AL MANDADO DE MI CASA")
with open("mandado.txt","a") as f:
    texto=input("DAME ALGO PARA METERSELO AL MANDADO, ESCRIBE SALIR PARA SALIR\n")
    while texto.upper()!="SALIR":
        f.write(texto)
        f.write("\n")
        texto=input("DAME ALGO PARA METERSELO AL MANDADO\n")

eleccion=input("Quieres abrir tu archivo con los nuevos datos?\n1. si, 2. no")
#El usuario me puede meter si, sI, Si, SI
if eleccion.upper()=="SI":
    os.system("mandado.txt")

os.system("V3.xlsx")