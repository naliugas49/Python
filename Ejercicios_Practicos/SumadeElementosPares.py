#Escribe una función que tome una lista de números y devuelva la suma de los números pares utilizando bucles y condicionales.
number_list = [1,23,4555,6,68,2,200,5000,9]
c = 0
for i in  number_list:
    if int(i)%2 == 0:
        c+=i
print(c)