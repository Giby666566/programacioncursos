import os
#Le decimos al cmd que escriba lo que hay dentro de system
#os.system("python hola_mundo.py")

#Me dice el directorio actual en el que estoy trabajando
print(f"Mi direccion es {os.getcwd()}")

#Me cambia el directorio actual del programa
os.chdir("C:/Users/Pedro Velez/Documents/6to semestre")

print(f"Mi direccion es {os.getcwd()}")

directorios=os.listdir()
print(directorios)


