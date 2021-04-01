numero=int(input("Dame un numero"))
suma=0
for i in range(0,numero+1):
    for j in range(1,i+1):
        suma=suma+j
print(suma)