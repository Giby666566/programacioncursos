import os
os.system("cls")
#El for itera sobre objetos iterables
#como por ejemplo los elementos de una list
#elementos de una tuple
#caracteres de un string
#todos estos elementos tienen posiciones
#accedemos a las posiciones con los bracket [posicion]
cadena="Este es mi programa"
for caracter in cadena:
    print(caracter, end=" ")

print()
#range(0,len(cadena))==0,1,2,3,4,5,...,len(cadena)
#OJO, los limites del range van desde posicion inicial hasta posicion final-1
for i in range(0,len(cadena)):
    print(cadena[i], end=",")

i=0
while i<len(cadena):
    print(cadena[i],end=".")
    i=i+1

print()
#ENUMERATE
celulares=["iphone x", "huawei p30", "galaxy s21", "xiaomi p20", "nokia"]
for i, celular in enumerate(celulares):
    print(i, celular)
    #print(celulares[i])

#[(0,"iphone x"),(1,"huawei p30"),("2,galaxy s21"),...]
a=enumerate(celulares)
print(f"El enumerate es {a}")