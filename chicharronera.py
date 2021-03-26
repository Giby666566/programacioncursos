import math
import os

a=int(input("Dame el valor de a"))
b=int(input("Dame el valor de b"))
c=int(input("Dame el valor de c"))
x1=complex()
x2=complex()

x1=(   -b+math.isqrt(math.pow(b,2)-4*a*c)    )/2*a
x2=(-b-math.isqrt(math.pow(b,2)-4*a*c))/2*a
print(x1,x2)

directorioactual=os.getcwd()
print(f"El directorio actual es {directorioactual}")