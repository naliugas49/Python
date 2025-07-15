###################################################################################################################################################################
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos 
# en una línea distinta.
####################################################################################################################################################################
from ntpath import join

product = input('eccriba los productos de la lista de la compra separados por coma')

#Metodo 1
print (product.replace(',','\n'))

#Metodo 2
print('\n'.join(product.split(',')))