#! /bin/python3
# number1 = input("ingrese el primer numero\n")
# number2 = input("ingrese el segundo numero\n")
# number3 = input("ingrese el tercer numero\n")

# promedio = (int(number1) + int(number2) + int(number3)) / 3

# print(f"el promedio de los tres numeros es {promedio}")

# workList = {}
# print ("Gestione su lista de tareas")
# while True:

#     option = input("\nselecciona la opcion a realizar dentro de las siguientes:\n1.Agregar tarea\n2.Eliminar tarea\n3.Listar tareas\n\n")
#     if option == "1":
#         key = input("ingrese una tarea\n")
#         value = input("ingrrese su prioridad\n")
#         workList[key] = value
#     elif option == "2":
#         delete = input("escriba el nombre de la tarea a eliminar\n")
#         del workList[delete]
#     else:
#         print(workList)

# par = set()
# impar =set()

# for d in range(1,21):
#     if d%2 == 0:
#         par.add(d)
#     else:
#         impar.add(d)
# print(f"\nel conjunto de los numeros pares es: {par}\n")
# print(f"el conjunto de los numeros impares es: {impar}\n")

"""##############################################################################################
Ejercicio 4: Suma de números pares
Escribe una función que tome un número entero positivo como argumento y calcule la suma de todos los números pares desde 2 hasta ese número. Utiliza un bucle for para realizar la suma.
###################################################

number = int(input("Escriba un número entero positivo: "))
def suma (n):
    c = 0
    for i in range(n+1):
        if int(i)%2 == 0:
            c += i
    return c

print(suma(number))

##################################################################################################
Ejercicio 5: Contar vocales en una cadena
Crea una función que tome una cadena de texto como argumento y cuente cuántas vocales (a, e, i, o, u) hay en la cadena. Utiliza un bucle for para recorrer la cadena.
######################################################################

string = input("escriba una frase: ")

def vowels_count(str1):
    c = 0
    for i in str1:
        if i == "a" or i =="e" or i =="i" or i =="o" or i =="u":
            c +=1
    print(c)

vowels_count(string)

####################################################################################
Ejercicio 6: Generador de secuencia Fibonacci
Escribe una función que genere los primeros n números de la secuencia Fibonacci, donde n es un número ingresado por el usuario. 
La secuencia Fibonacci comienza con 0 y 1, y cada número subsiguiente es la suma de los dos anteriores. Utiliza un bucle while para generar la secuencia.

n = int(input("ingrese el numero de digitos que desea de la serie de fibonacci: "))
c = 0
valor1 = 0
valor2 = 1
while c < n:
    valor = valor1 + valor2
    valor1= valor2
    valor2=valor
    print(valor)
    c+=1
    
"""
