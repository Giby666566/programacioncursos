#ejercicio 2
print("¿cual es el precio del producto?")
precio=float(input())
print ("el precio del producto es", end=" ")
print(precio*1.16)
#ejercicio 3 
print("¿cual es tu edad?")
edad=int(input())
print("¿cual es tu sexo?")
sexo=str(input())
print("¿cual es tu altura en metros?")
altura=float(input())
print("tu edad es ",edad,"tu sexo es ",sexo,"tu mides ",altura,"metros")
#ejercicio 4 
print("dame el valor de a")
a=int(input())
print("dame el valor de b")
b=int(input())
print("dame el valor de c")
c=int(input())
x1=-b+(((b**2)-4*a*c))**0.5/2*a
print(x1)