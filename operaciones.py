def max(a,b):
    if a>b:
        return a
    else:
        return b

def sum(juan,pepe):
    return juan+pepe

def nombre_completo(nombre,appat,apmat):
    print(f"El nombre completo es {nombre} {appat} {apmat}")

print("Dame dos numeros")
x=int(input())
y=int(input())

mi_maximo=max(x,y)

sumita=sum(x,y)
print(f"La suma es {sumita}")

print(f"El maximo es {mi_maximo}")

nombre_completo("Juan","Perez","Martinez")