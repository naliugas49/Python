def suma(*numeros):    # al argumento se le pone asterisco para hacer referencia de que los argumentos van a ser iterables
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)


def get_product(**datos):  # los 2 asteriscos en este caso a parte de representar que los argumentos 
    print(datos)            # seran iterables ademas obliga a introducirlos con un indetificador (key)


get_product(id=" 23")

