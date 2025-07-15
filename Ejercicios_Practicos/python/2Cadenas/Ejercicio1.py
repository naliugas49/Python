#####################################################################################################################
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
#imprima por pantalla en líneas distintas el nombre del usuario tantas veces como 
#el número introducido.
#####################################################################################################################

name = input('escriba su nombre\n')
number = int(input('escriba un numero al azar\n'))
for i in range(number):
    print(name)
    
    
#variante de la solucion    
nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))
