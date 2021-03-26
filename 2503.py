import os
os.system("cls")
def reciproco(numero):
    return 1/numero

def nombrecompleto(nombre,appat,apmat):
    nombcomp=nombre+appat+apmat
    return nombcomp

def sumatoriareciproca(x,cant):
    suma=0
    for i in range(1,cant+1):
        y=1/(x**i)
        suma=suma+y
    return suma
def factorial(n):
    mult=1
    for i in range(n,1,-1):
        mult=mult*i
    return mult

#type()
#id()
#print()
#int()
#range()
#enumerate()
#str()
#list()
#bool()
#...

print(sumatoriareciproca(2,5))
print(factorial(5))
print("Dame un numero")
x=float(input())


y=reciproco(x)
print(f"El reciproco es {y}")

nombre=str(input("Dame el nombre"))
apellidopat=input("Dame el apellido paterno")
apellidomat=input("Dame el apellido materno")

n=nombrecompleto(nombre,apellidopat,apellidomat)
print(n)
