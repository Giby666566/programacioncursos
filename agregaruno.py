ingreso=input("Dame un numero para agregarlo a una lista")
lista=[]
while ingreso!="salir":
    lista.append(int(ingreso))
    ingreso=input("Dame un numero para agregarlo a una lista")

milistaaumentada=[]
print(lista)
for elemento in lista:
    milistaaumentada.append(elemento+1)

print(milistaaumentada)
    