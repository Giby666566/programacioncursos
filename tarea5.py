import os
os.system('cls')
temperatura=float(input("dame la temperatura"))
temp=bool(input('¿la temperatura está en grados Celcius?'))
if temp==True:
    farenheit=(temperatura*1.8)+32
    print(f'la temperatura en grados Fahrenheit es:{farenheit}')
elif temp==False:
    celsius=(temperatura-32)/1.8
    print(f'la temperatura en grados celsius es:{celsius}')

#programa2
n=int(input('dame un numero\n'))
for numero in range(0,n):
    if n%2==0:
        print("es par",end="\n")
        print(n)
        n=n-1
        
    else:
        print(f'no es par\n{n}')
        n=n-1
print("\n")
num=0
for num in range (0,14,1):
    if num==8 or num==10:
        continue
    else:
        print(num)
        num=num+1