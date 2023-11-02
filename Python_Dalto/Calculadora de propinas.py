'''
Descripción:
Escribe un programa que calcule el monto total de una cuenta de restaurante, incluyendo la propina. 
El programa debe solicitar al usuario el monto total de la cuenta y el porcentaje de propina que desea dejar. 
Luego, debe calcular el monto de la propina y mostrar el total a pagar.

Requisitos:
- El programa debe validar que los valores ingresados sean numéricos y mostrar un mensaje de error si no lo son.
- El programa debe validar que el porcentaje de propina sea mayor o igual a 0 y menor o igual a 100. Si no cumple esta condición, 
  debe mostrar un mensaje de error.
- El programa debe redondear el monto total a pagar a dos decimales.
- El programa debe permitir al usuario repetir la operación cuantas veces desee.

Puedes utilizar las siguientes funciones para ayudarte:

- input(): Para solicitar al usuario los valores de entrada.
- try-except: Para manejar errores al validar los valores ingresados.
- round(): Para redondear el resultado final.

¡Buena suerte con el ejercicio! Si tienes alguna pregunta, no dudes en hacerla.
'''

check = porcent = 'la tiza'
def all_numeric (num):
  try:
    float(num)
    return True
  except ValueError:
    return False

while True:
  while all_numeric(check) == False:
    check = input("Ingrese el monto total de la cuenta: ")
    if all_numeric(check) == True:
      
      while all_numeric(porcent) == False or int(porcent) > 100 or int(porcent) < 0 : 
        porcent = input ("Ingrese el porciento de propina que desea dejar: ")
        if all_numeric(porcent) == True:
          if 0 <= int(porcent) <= 100 :
            valor_percent = float(check) * float(porcent)/100 
            valor_total = round((float(check)+ valor_percent),2)
            print( f"""EL monto total a pagar es de 
            ${valor_total}\n""")
          else:
            print('''
          <Error>./     El valor de porciento debe estar entre 0 y 100/
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''') 
                
        else: 
          print('''
          <Error>./     Solo se permiten datos numericos/
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')       
    
    else:
      print('''
      <Error>./     Solo se permiten datos numericos/
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')    
  check = porcent = 'la tiza'

   
  










