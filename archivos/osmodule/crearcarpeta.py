import os
nombre=input("Dame el nombre de una carpeta para crearla \n")
os.mkdir(nombre)


#Quiero crear un archivo y guardarlo en la nueva carpeta que me dijeron
archivo=input("Dame el nombre del archivo txt para crearlo dentro de tu carpeta nueva\n")
with open(nombre+"/"+archivo,"w") as f:


os.chdir(nombre)
with open(archivo,"w") as f:
