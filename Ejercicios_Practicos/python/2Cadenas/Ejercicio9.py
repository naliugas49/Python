##################################################################################################################################################################
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa 
# anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
################################################################################################################################################################

date=input('escriba la fecha de hoy en formato dd/mm/aaaa \n')
print(f"dia {date[:date.find('/')]} del mes {date.split('/')[1]} del año {date.split('/')[2]}" )