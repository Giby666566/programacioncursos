texto=input("Dame un texto que quieras meter al archivo ")
nombre_archivo=input("Dame un nombre de un archivo ")

with open(nombre_archivo,"a") as miarchivo:
    miarchivo.write(texto)