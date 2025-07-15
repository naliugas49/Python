# Escribir un programa que cree un diccionario de traducción español-inglés. El 
# usuario introducirá las palabras en español e inglés separadas por dos puntos, y 
# cada par <palabra>:<traducción> separados por comas. El programa debe crear un 
# diccionario con las palabras y sus traducciones. Después pedirá una frase en 
# español y utilizará el diccionario para traducirla palabra a palabra. Si una 
# palabra no está en el diccionario debe dejarla sin traducir.

import fractions
from typing import Dict
# dicc = {'nombre':'name',
#          'perro':'dog',
#          'alto':'tall',
#          'es':'is',
#        'mi':'my'}i=0

dicc = {}
quiz = input('Introduzca las palabras con sus traducciones en español e inglés'
'separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas\n')

for i in quiz.split(','):
    key,valor = i.split(':')
    dicc[key]=valor

frase = input('escriba una frase para traducirla:  ')

for i in range (len(frase.split())):
    if frase.split()[i] in dicc:
        print(dicc[frase.split()[i]],end =" " )
    else:
        print(frase.split()[i],end =" ")
 
 
#OTRA VIA
diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')
