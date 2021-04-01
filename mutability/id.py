a=10

b=a
print(id(a))
print(type(a))
print(id(b))
print(type(b))
print(a is b)
a=a+1
print(id(a))
print(id(b))
print(a is b)
print(a)
print(b)

x=[1,2,3]
y=x
print(id(x))
print(id(y))
print(x is y)
y.pop()
print(y)
print(x)
x.append("hola")
print(y)
print(x is y)


#CUANDO YO IGUALO DOS OBJETOS INMUTABLES Y CAMBIO UNO, SU IDENTIDAD CAMBIA (id)
#CUANDO YO IGUALO DOS OBJETOS MUTABLES Y CAMBIO UNO, SIGUEN TENIENDO LA MISMA IDENTIDAD (id)