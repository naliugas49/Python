# Escribe una función que determine si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa). Utiliza métodos de cadenas
# como replace y reverse.

text = input("ingrese palabra:\n")
if text == text[::-1]:
    print("El texto es palindromo")
else:
    print("El texto no es palindromo")


