# Crea un diccionario de contactos donde cada contacto tiene un nombre y un número de teléfono. Luego, implementa funciones para agregar, buscar
# y eliminar contactos del diccionario.

dic_Contacts = {
    "Messi": "7452173",
    "CR7": "8567402",
    "Neymar": "888956"
}

################
## Funciones ###
####################################
#agregar
def agregar(name,number):
    dic_Contacts[name]=number

#buscar
def search(name):
    return dic_Contacts.get(name)


#eliminar
def delete(name):
    return dic_Contacts.pop(name)
#####################################

while True:
    option = "la tiza"
    while option.isnumeric() == False or option not in ("1,2,3,4,5"):
        option = input('''\n################################################################
################################################################                
        Seleccione una de las siguientes opciones a realizar:
        1. Agregar un contacto
        2. Buscar un contacto
        3. Borrar un contacto
        4. Ver su lista de contactos
        5. Salir                              
    > ''')
        
    if option == "1":
        add_name = input("Escriba el nombre del contacto: \n")
        add_number = input ("Escriba el numero del contacto:\n")
        agregar(add_name,add_number)
    elif option == "2":
        search_name = input("Ingrese el nombre del contacto a buscar su numero:\n")
        print(f"\n{search(search_name)}")
    elif option == "3":
        del_name = input("Ingrese el nombre del contacto a borrar:\n")
        delete(del_name)
    elif option == "4":
        print (f"\n{dic_Contacts}\n")
    else: 
        exit()
    
    
    












