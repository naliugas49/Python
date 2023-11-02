# lista = [1,"dairon",True]
# tupla = enumerate(lista)

usuarios = [
    ['popelle', 1],
    ['pluto', 4],
    ['donald', 20]
]
#################################
##### Listas de comprension #####
#################################
# map
# creamos una lista nueva solo con el primer elemento
nombres_map = [usuario[0] for usuario in usuarios]
print(usuarios[0][0])

# filter
nombres_filter = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres_filter)

# map and filter
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

###################################
## Otra via con funciones lambda ##
###################################

nombres_lambdaMap = list(map(lambda usuario: usuario[0], usuarios))

nombres_lambdaFilter = list(filter(lambda usuario: usuario[1] > 2, usuarios))
