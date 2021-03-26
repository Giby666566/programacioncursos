#ejercicio 1
numero1=int(input("dame un número "))
numero2=int(input("dame otro número "))
numero3=int(input("dame otro número "))

if numero1>numero2 and numero1>numero3:
    print(f'{numero1}',' es mayor')
elif numero2>numero1 and numero2>numero3:
    print(f'{numero2}',"es mayor")
else: 
    print(f'{numero3}','es mayor')
#ejercicio 2 
lado1=int(input('dame lado 1 '))
lado2=int(input('dame lado 2 '))
lado3=int(input('dame lado 3 '))
lado4=int(input('dame lado 4 '))
if lado1==lado2 and lado2==lado3 and lado3==lado4 and lado4==lado1:
    print('es un cuadrado')
else:
    print('es un rectángulo')
#ejercicio 3 
cosas=int(input("¿cuantas cosas compró?\n"))
if cosas>10:
    print("sin descuento pagaría ",cosas*20)
    print("el descuento fue de ",(cosas*20)*0.10)
    print("el precio final con descuento es:",(cosas*20)*0.90 )
#ejercicio 4 
calif=int(input('¿cual es la calificación?\n'))
if calif>90:
    print("es A")
elif calif>80 and calif<=90:
    print("es B")
elif calif>70 and calif<=80:
    print("es C")
elif calif>60 and calif<=70:
    print("es D")
else:
    print("reprobado")
#programa reto
numero=int(input('dame un numero de 4 digitos'))
if numero>=1000 and numero<=9999:
    numero=list(numero)
    numero.sort()
    print (numero)
else:
    print("el numero no corresponde al pedido")

