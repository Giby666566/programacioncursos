#congetura de collatz
numero=int(input('dame un número '))
while numero>=1:
    
    if numero%2==0:
        print(numero)
        numero=numero/2
    elif numero%2==1:
        print(numero)
        numero=(numero*3)+1
    if numero==1: 
        print(numero)
        break



