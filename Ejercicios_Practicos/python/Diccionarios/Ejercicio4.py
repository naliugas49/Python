# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre 
# por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el 
# nombre del mes.

months = {
    '1':'Enero','01':'Enero',
    '2':'Febrero','02':'Febrero',
    '3':'Marzo','03':'Marzo',
    '4':'Abril','04':'Abril',
    '5':'Mayo','05':'Mayo',
    '6':'Junio','06':'Junio',
    '7':'Julio','07':'Julio',
    '8':'Agosto','08':'Agosto',
    '9':'Septiembre','9':'Septiembre',
    '10':'Octubre',
    '11':'Noviembre',
    '12':'Diciembre'       
}

date = input('Escriba una fecha siguiendo el formato (dd/mm/aaaa): '  )

print(f" {date[:date.find('/')]} de {months.get(date.split('/')[1])} de {date.split('/')[2]}")

#OTRO METODO
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])
