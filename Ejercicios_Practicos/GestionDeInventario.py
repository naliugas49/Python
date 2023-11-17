# Crea un programa que permita gestionar un inventario. Debes utilizar un diccionario para representar los elementos del inventario, donde las
# claves son los nombres de los productos y los valores son las cantidades disponibles. Implementa funciones para agregar, actualizar, eliminar y
# mostrar elementos del inventario. También permite que los usuarios realicen compras y actualicen el inventario en consecuencia.

inventario = {
    "toallas":4,
    "jabon":10,
    "detergente":2
}

question = input('''Que desea saber de su inventario??
Elija una de las siguientes opciones: 
1. Muestra todos los elementos
2. Muestra la cantidad de un elemnto                 
3. Agregar algun producto
4. Rebajar algun producto del inventario
5. Salir
> ''')

def Valid_Product (monto):   
    while not monto.isnumeric():      
        print("No introdujo una cantidad correcta!")
        monto = input("intente con otra cantidad: ")
    return monto  
        

while True:
    if question == "5":
        exit()
    elif question == "1":        
        for key in inventario:
            print(f"{key}  {inventario[key]}")
    
    elif question == "2":
        element = input('''Indique el elemento a mostrar su cantidad
    > ''').lower()
        while True :           
            if element in inventario:
                print (f"La cantidad de {element} es: {inventario[element]}")
                break
            else:
                element = input("""Elemento no encontrado intentelo de nuevo
    > """)
    
    elif question == "3":
        product = input( "que producto desea agregar?:  ")        
        amount = input ("que cantidad: ")
        if product in inventario:            
            inventario[product] = inventario [product] + int(Valid_Product(amount))
        else:
            inventario[product] = int(amount)
    
    elif question == "4":
        product = input("que producto desea rebajar?: ") 
        while True:                       
            if product in inventario:
                amount = input ('que cantidad: ')
                inventario[product] = inventario [product] - int(Valid_Product(amount))
                if inventario[product] < 0:
                    print(">>>ERROR<<< Intenta rebajar una cantidad mayor que la que tiene en inventario")
                elif inventario[product] == 0:
                    del inventario[product]
                    break
                else:
                    break
            else:
                product = input("""Elemento no encontrado intentelo de nuevo
    > """)
    else:
        print("Por favor introduzca solo alguna de las opciones que se muestran")        

    question = input("\n> ")



