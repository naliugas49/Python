import re

msg = '''No introdujo la mascara en ninguno de los 2 formatos correctos (xxx.xxx.xxx.xxx o yy).
Vuelva a intentarlo:\n> '''
numbers = ('0','128','192','224','240','248','252','254')
# Patron para comparar si es una mascara valida en formato 255.255.255.0
patron = r"^(((255\.){3}(255|254|252|248|240|224|192|128|0+))|((255\.){2}(255|254|252|248|240|224|192|128|0+)\.0)|((255\.)(255|254|252|248|240|224|192|128|0+)(\.0+){2})|((255|254|252|248|240|224|192|128|0+)(\.0+){3}))$"
# Patron para comparar si una mascara es valida en formato CIDR
patronCIDR = r"^([0-9]|[1-2][0-9]|3[0-2])$"


#----------------------------------------
### FUNCIONES ###
#----------------------------------------
def CIDR_to_Mask(parameter):
    valor = int(parameter)    
    if valor >= 24:
        value = valor - 24
        result = numbers[value]            
        return f"255.255.255.{result}"
    elif 24 > valor >= 16:
        value = valor - 16
        result = numbers[value]            
        return f"255.255.{result}.0"
    elif 16 > valor >= 8:
        value = valor - 8
        result = numbers[value]            
        return f"255.{result}.0.0"
    elif 8 > valor >= 0:
        value = valor - 8
        result = numbers[value]            
        return f"{result}.0.0.0"
def Mask_to_CIDR (parameter):
    number_list = parameter.split(".")
    octeto = 0
    for valor in number_list:    
        if valor == "255":
            octeto += 8       
        elif valor == "0":
            return octeto             
        else:        
            octeto_number = numbers.index(valor)
            #print(octeto_number)
            return octeto + int(octeto_number)
def Network_subred(parameter):
    IP, Mask = parameter.split("/")[0],parameter.split("/")[1]
    IP_l = IP.split(".")
    Mask_decimal = CIDR_to_Mask(Mask).split(".")

    subred = ""
    for i,ii in zip(IP_l,Mask_decimal):
        result = int(i) & int(ii)
        #result = int((bin(int(i)) and bin(int(ii))),2)
        subred = f"{subred}{str(result)}."
    subred = subred[:-1]+ f"/{Mask}"    
    return subred  

def Host (parameter):
    n = int(parameter)
    host = 2**(32-n)-2
    return host

#------------------------------------------
### PROGRAMA PRINCIPAL ####
#------------------------------------------
answer = input(''' 
Bienvenido a su Calculadora de red, seleccione la operacion a realizar:
1- Convertir de CIDR a mask y viseversa.
2- Saber cuantos hosts tendra disponibles en la subred.
3- Averiguar a que red pertenece la IP especifica.
 > ''')

while answer not in ('1','2','3'):
    answer = input("Opcion no valida intentelo de nuevo.\n > ")

if answer == '1':
    mask = input('Ingrese la mascara que desea convertir: ')
    
    if re.match (patronCIDR,mask):
        print(CIDR_to_Mask(mask))
    elif re.match (patron,mask):
        print(Mask_to_CIDR(mask))
    else:
        mask = input(msg)

elif answer == '2':
    subnet = input('introduzca la mascara de subred: ')
    if re.match (patronCIDR,subnet):
        print(f"Esta subred tiene disponibilidad para {Host(subnet)} hosts")
    elif re.match (patron,subnet):
        d = Mask_to_CIDR(subnet)
        print(f"Esta subred tiene disponibilidad para {Host(Mask_to_CIDR(subnet))} hosts")
    else:
        mask = input(msg) 
else:
    subnet = input ("""Ingrese la IP con la mascara a la cual para saber a la subred a la que pertenece: 
siga este formato Ej. 10.0.0.25/18 
> """)
    print(f"La subred a la que pertenece dicha IP es {Network_subred(subnet)}")
