#Hacer un programa que lea un archivo de textos y que te quite las vocales de ese archivo
import os
nombre=input("Dame la direccion del archivo")
with open(nombre,"r") as f:
    with open("temporal.txt","w") as nuevo:
        for linea in f:
            for caracter in linea:
                if caracter=="a" or caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u":
                    continue
                else:
                    nuevo.write(caracter)
os.remove(nombre)
os.rename("temporal.txt",nombre)

