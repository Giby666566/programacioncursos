#hacer un programa en donde me dan un string y tengo que regresa otro string que contenga
#las 2 primeras letras del string y las dos ultimas 

#hacer un programa donde me dan un texto y luego me das un caracter y todas las ocurrencias del caracter 
#en el texto las cambia por un #

#programa donde me dan un texto y le tienes que agregar el subfijo "oda", si termina con oda agregar "ar"

#programa donde imprima un string al reves 
import os
os.system("cls")
def sinespacio(palabra):
    textosinesp=str()
    for j in range(0,len(palabra)):
        if palabra[j]!=" ":
            textosinesp=textosinesp+palabra[j]
    return textosinesp

def alreves(palabra):
    reverseado=""
    for i in range(len(palabra)-1,-1,-1):
        reverseado=reverseado+palabra[i]
    return reverseado


palabras=str(input("dame una palabra"))
palabrareverseada=alreves(palabras)
print(palabrareverseada)
textojunto=sinespacio(palabras)
print(textojunto)
#programa donde me dan un texto de palabras separadas por coma e imrimir el mismo texto pero sin las palabras 
#repetidas 

#programa que me quite los espacios

#programa para saber si una palabra es palindroma o no es palindroma (sin espacios) anitalavalatina
