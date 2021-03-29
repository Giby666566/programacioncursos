
def foo():
    global x
    x="juanito"
    print(f"El valor de x es {x}")


x=5
print(x)
foo()
print(x)




