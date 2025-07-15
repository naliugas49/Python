# Escribir un programa que cree un diccionario simulando una cesta de la compra. El 
# programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista 
# de la compra y el coste total, con el siguiente formato
#################################
# Lista de la compra 	
# Artículo 1 	Precio
# Artículo 2 	Precio
# Artículo 3 	Precio
# … 	…
# Total 	Coste
################################
dicc = {}
valor_all = 0
test = 'Si'

while test == 'Si':
    art = input ('Haga su lista de la compra\nintroduzca el articulo a comprar: ')
    price = input ('ingrese el precio del producto: ')
    dicc [art] = price
    test = input('Para introducir un nuevo articulo escriba Si en caso contrario escriba No: ')

print('\nLista de compra\nArticulo\tPrecio')
for key,valor in dicc.items():
    print(key,'\t\t',valor)
    valor_all += float(valor)
print('Precio total\t',valor_all)    



#Otra Solucion

cesta = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
coste = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)