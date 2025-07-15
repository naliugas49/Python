# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#     Ingredientes vegetarianos: Pimiento y tofu.
#     Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que
# elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
# vegetariana o no y todos los ingredientes que lleva.
###############################################################################################################################################################################
question = input ('Quiere una pizza vegetariana o no vegetariana \n')
both = ('\n- mozzarella\n- tomate') 
if question == 'vegetariana':
    veg =input('Escoja uno de los siguientes ingredientes para su pizza \n 1- pimiento \n 2- tofu \n')
    print('la pizza que eligio es Vegetariana y los ingredientes son: \n ',both,'\n-',veg)
elif question == 'no vegetariana':
    noveg =input('Escoja uno de los siguientes ingredientes para su pizza \n 1- peperoni \n 2- Jamon \n 3- Salmon \n')
    print('la pizza que eligio es No Vegetariana y los ingredientes son:\n',both,'\n-',noveg)
else:
    print('se ha equivocado al elegir')
    
#Metodo 2
 # Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    