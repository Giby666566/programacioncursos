#Pedimos los limites de nuestra integral a y b
a=int(input("Dame el limite inferior de la integral\n"))
b=int(input("Dame el limite superior de la integral\n"))
#Calculamos b-a porque es la evaluacion de x de la integral definida de un polinomio de grado n
grado=0
integral=0
coeficiente=0
#Hacemos un ciclo mientras el input que me den sea diferente de un espacio
while coeficiente!=" ":
    coeficiente=input(f"Dame el coeficiente de x a la {grado}\n")
    if coeficiente!=" ":
        grado=grado+1
        integral=integral+(float(coeficiente)*(b**grado-a**grado))/grado
print(f"El resultado de la integral es {integral}")