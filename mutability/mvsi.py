#UN OBJETO ES INMUTABLE
cadena="Anahuac"
print(id(cadena))
#cadena[0]="R" NO ME VA A DEJAR PORQUE ES INMUTABLE
#NO ME PUEDE CAMBIAR SU ESTADO
cadena="IPN"
print(id(cadena))
cadena="Rnahuac"
print(id(cadena))

#UN OBJETO ES MUTABLE
lista=[1,2,3,4]
print(lista)
lista[0]=6
print(lista)

lista2=list(lista)
print(lista is lista2)
print(lista)
print(lista2)
print(id(lista),id(lista2))

