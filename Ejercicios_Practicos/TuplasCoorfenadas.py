#Crea una lista de tuplas que representen coordenadas (x, y). Luego, implementa una función que encuentre la tupla con la coordenada más cercana
#al origen(0, 0).

l = [(4,5),(3,1),(0,1),(4,98),(0,0)]

def Near (lista):
    near_distance = (lista[0][0]**2 + lista[0][1]**2)**1/2
    for i in lista:
        distance = (i[0]**2 + i[1]**2)**1/2
        if  distance < near_distance:
            near_point = i
    return near_point
    
print(Near(l))
    
