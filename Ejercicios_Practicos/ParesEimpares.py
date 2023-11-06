# Dada una lista de listas de números, escribe una función que cuente cuántos números pares e impares hay en total.

lis = [1,2,3,4,5,6,7,8,9,9]
def Num_count (lista):
    par = 0
    impar = 0
    for i in lista:
        if int(i)%2 == 0:
            par+=1
        else:
            impar+=1
    return par,impar

print(Num_count(lis))



