#Crea un juego de adivinanza en el que el programa genera un número aleatorio y el usuario 
#debe adivinarlo. Proporciona pistas como "Demasiado alto" o "Demasiado bajo". 
#Utiliza bucles y condicionales para guiar al usuario hasta la respuesta correcta.

import random

number =  str(random.randint(1,10000))

userNumber = input("Adivina un numero del 1 al 10000 ")
while True:
    
    if userNumber > number:
        print ("El numero es menor")
    elif userNumber < number: 
        print( "El numero es mayor")
    else:
        print("Respuesta correcta. Felicidades!!!")
    userNumber = input("Intentelo de nuevo: ")

