#ME VAN A DAR UNA LISTA DE NUMEROS
#TODOS LOS NUMEROS SE VAN A REPETIR EN 1 OCASION MENOS UNO
#YO TENGO QUE IMPRIMIR EL NUMERO QUE NO SE REPITA

numeros=[]
entrada=int()
entrada=int(input("Dame un numero o escribe -1 para salir"))
while entrada!=-1:
    numeros.append(entrada)
    entrada=int(input("Dame un numero o escribe -1 para salir"))
    

print(numeros)
numeros.sort()
print(numeros)
i=0
while i<len(numeros):
    if (i==len(numeros)-1):
        print(numeros[i])
        break
    if (numeros[i]!=numeros[i+1]):
        print(numeros[i])
        break
    if (numeros[i]==numeros[i+1]):
        #se esta repitiendo
        i=i+2
        continue

print()