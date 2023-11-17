# Crea un sistema simple de reservas de hoteles. Utiliza diccionarios para representar habitaciones  
# disponibles y reservadas en un hotel. Permite a los usuarios realizar reservas, cancelar reservas y ver la 
# disponibilidad de habitaciones en función de las fechas de entrada y salida.
from datetime import datetime

disponibilidad = {
    "101":[('2023-10-01','2023-10-05')],
    "102":[],
    "103":[('2023-10-03','2023-10-10')]
}

#################
### FUNCIONES ###
#################
def Fechas():
    entrada_date = input("Ingrese Fecha de entrada bajo este formato(YYYY-MM-DD): ")
    while not ValidarFecha(entrada_date):
        entrada_date = input("Ingrese Fecha de entrada bajo este formato(YYYY-MM-DD): ")
    salida_date = input("Ingrese Fecha de salida bajo este formato(YYYY-MM-DD): ")
    while not ValidarFecha(salida_date) or salida_date < entrada_date:
        salida_date = input("Ingrese Fecha de salida bajo este formato(YYYY-MM-DD) y posterior a fecha de entrada: ")    
    return entrada_date,salida_date
def VerificarDisponibilidad (in_,out_):
    l=[]
    for clave, valor in disponibilidad.items():
        if valor == []:
            l.append(clave)
        else:    
            for i in valor:                
                if (valor == 0) or (in_ <= i[0]  and  out_ < i[0]) or (in_ > i[1]):
                    l.append(clave) 
                else:
                    break
    return l
def ValidarFecha(cadena):
    formato_esperado = '%Y-%m-%d'
    try:
        fecha = datetime.strptime(cadena, formato_esperado)
        return True
    except ValueError:
        return False
def AgregarReserva (inside,outside):
    l = disponibilidad[hab_disp[0]]
    if disponibilidad[hab_disp[0]] == [] : 
        l.append((inside,outside))
    else:
        for i in range(0,len(disponibilidad[hab_disp[0]])):            
            if disponibilidad[hab_disp[0]][i] >= (inside,outside):
                break
            l.insert(i+1,(inside,outside))
                
    return l 
def Cancelar (hab,inside,outside):
    if (inside,outside) in disponibilidad[hab]:
        disponibilidad[hab].remove((inside,outside))
        print("Su reserva fue cancelada con exito")
    else:
        print(f"No hay reserva para la habitacion {hab} en el periodo de {inside} hasta {outside}")
    
##########################################    

accion = input('''
Se lecciona la operacion a realizar:
1. Realizar Reservas
2. Cancelar Reservas
3. Ver Disponibilidad
''')   

######## Programa Principal ##############
if accion == "1":       
    entrada_date,salida_date = Fechas()
    hab_disp = VerificarDisponibilidad(entrada_date,salida_date)
    
    if hab_disp == []:
        print("No tenemos habitaciones disponibles en este momento: ")
    else:
        disponibilidad[hab_disp[0]] = AgregarReserva(entrada_date,salida_date)
        print(f"Tiene la habitacion {hab_disp[0]} disponible para el periodo desde {entrada_date} hasta {salida_date}") 
elif accion == "2":
    habitacion = input("numero de la habitacion: ")
    entrada_date,salida_date = Fechas()
    Cancelar(habitacion,entrada_date,salida_date)
elif accion == "3":
    print("Para saber la disponibilidad en un periodo de tiempo ingreselos a continiacion. ")
    entrada_date,salida_date = Fechas()
    print( f"Tiene disponible todas estas habitaciones: {VerificarDisponibilidad(entrada_date,salida_date)}")
    






    

    
    








