# Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
# información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo 
# electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato 
# debe imprimirse el contenido del diccionario.

dicctionary = {}
lis = ['nombre', 'edad', 'sexo', 'telefono','correo electronico'] 
for d in lis:
    data = input(f"escriba su {d}: ")
    dicctionary[d] = data
    print(dicctionary)
    
