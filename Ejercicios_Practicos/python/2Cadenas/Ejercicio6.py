##############################################################################################################################################################
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
##############################################################################################################################################

phrase = input('introduzca una frase\n')
vowel = input('ingrese una vocal\n')
print(phrase.replace(vowel, vowel.upper()))