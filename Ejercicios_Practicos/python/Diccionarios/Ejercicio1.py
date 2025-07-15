# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de #
# aviso si la divisa no está en el diccionario.


dicc = {
    'Euro':'€', 
    'Dollar':'$',
    'Yen':'¥'
}
money = input('escriba una divisa: ')

if money in dicc.keys():
    print(dicc[money])
else:
    print('La divisa no esta disponible')
 
#Otro metodo   
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))