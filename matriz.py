matriz=[]

matriz.append([1, 2, 3])
matriz.append([4 ,5 ,6])
matriz.append([7 ,8 ,9])
print(matriz)
for fila in matriz:
    for numero in fila:
        print(numero, end=" ")
    print("\n",end="")
print()

i=0
j=0
while i<=2:
    while j<=2:
        print(matriz[i][j],end=" ")
        j=j+1
    j=0
    i=i+1
    