# Escribir un programa que guarde en un diccionario los precios de las frutas de la 
# tabla, pregunte al usuario por una fruta, un número de kilos y muestre por 
# pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el 
# diccionario debe mostrar un mensaje informando de ello.
#
# Fruta 	Precio
# Plátano 	1.35
# Manzana 	0.80
# Pera 	0.85
# Naranja 	0.70


dicc = {
    'platano':'1.35',
    'manzana':'0.80',
    'pera':'0.85',
    'naranja':'0.70'    
}

quiz_fruit = input('Que producto desea comprar: ')
if quiz_fruit in dicc:
    quiz_kg = input('Cuantos kilos: ')
    mult = float(dicc.get(quiz_fruit)) * float(quiz_kg)
    print(f'Debe pagar {mult} por su producto')
else:
    print('No tenemos esa fruta')
    
    
    
#OTRO METODO
frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")