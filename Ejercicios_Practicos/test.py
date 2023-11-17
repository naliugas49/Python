# disponibilidad = {
#     "101":[('2023-10-01','2023-10-05')],
#     "102":[],
#     "103":[('2023-10-03','2023-10-10')]
# }


# if ('2023-10-01','2023-10-05') in disponibilidad['101']:
#     disponibilidad["101"].remove(('2023-10-01','2023-10-05'))
#     print(disponibilidad)
# else:
#     print("nada")


# hab_disp = ["101","102","103"]
# inside = input ("fecha de entrada: ")
# outside = input("fecha de salida: ")
# l = disponibilidad[hab_disp[0]]
# for i in range(0,len(disponibilidad[hab_disp[0]])):
#             x = disponibilidad[hab_disp[0]][i]
#             if x >= (inside,outside):
#                 l.insert(i,(inside,outside))

# l.insert(0,"34")
# disponibilidad[hab_disp[0]] = l

# print (l)
# print(disponibilidad)

# mi_lista_ordenada = [1, 3, 5, 7, 9]
# elemento_nuevo = 10

# #posicion = 0
# for i in range(0,len(mi_lista_ordenada)):
#     if mi_lista_ordenada[i] >= elemento_nuevo:
        
#     #posicion += 1

# mi_lista_ordenada.insert(i, elemento_nuevo)
# print(mi_lista_ordenada)


l = "2023-04-01"
d = '2023-05-01'

t = "mayor" if d > l else "menor"

print(t)