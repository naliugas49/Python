# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene 
# <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

lis = ['nombre','edad','direcion','telefono']
dicc = {}
for d in lis:
    quiz = input(f'introduzca su {d}: ')
    dicc[d] = quiz
    
print(f'{dicc[lis[0]]} tiene {dicc[lis[1]]} años, vive en {dicc[lis[2]]} y su número de teléfono es {dicc[lis[3]]}')


#OTRO METODO
nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])