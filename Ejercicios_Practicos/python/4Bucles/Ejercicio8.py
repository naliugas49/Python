# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

num = int(input('escribe un numero entero\n'))
print('\n')
d = dd = 1
while d <= num:
    print(str(dd))
    d = d +2
    dd = f'{d} {dd}'
    
#Otro Metodo 
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")