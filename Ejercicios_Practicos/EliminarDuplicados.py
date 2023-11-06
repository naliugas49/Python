#Crea una función que tome una lista y elimine los elementos duplicados, manteniendo el orden original de la lista.
lista = ["juan","pedro","pedro","juan","pepe"]

lista2=[]

for i in lista:
    if i not in lista2:
        lista2.append(i)
print(lista2)    