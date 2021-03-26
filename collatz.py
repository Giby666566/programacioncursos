import os
os.system("cls")
num=int(input("Dame un numero para hacer el jueguito de Collatz\n"))
print("Haremos el jueguito de la conjetura de Collatz")
print(f"Nuestro numero inicial es {num}")
while num!=1:
    if (num%2==0):
        num=num/2
    else:
        num=num*3+1
    print(num)
