# Escribir un programa que almacene el diccionario con los créditos de las #asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después #muestre por pantalla los créditos de cada asignatura en el formato <asignatura> #tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas #del curso, y <créditos> son sus créditos. Al final debe mostrar también el #número total de créditos del curso.


dicc = {'Matemáticas': 6, 
        'Física': 4,
        'Química': 5
}
all_credit = 0
for subjet, credit in dicc.items():
        print(subjet, 'tiene', credit,'creditos')
        all_credit += credit
  
print('\nEl curso tiene',all_credit,'creditos')