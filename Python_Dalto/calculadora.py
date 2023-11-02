print("""Bienvenidos a la calculadora
Para salir escribe Salir 
Las operaciones son suma, multi, div y resta""")


numero1 = ""
while numero1 == "" or numero1.isnumeric() == False:
    numero1 = input("Ingrese un numero: ")
    if numero1.lower() == "salir":
        exit()

while True:
    operacion = ""
    while operacion == "" or operacion.lower() not in ["suma", "div", "multi", "resta"]:
        operacion = input("Ingresa operacion: ")
        if operacion.lower() == "salir":
            exit()

    numero2 = ""
    while numero2 == "" or numero2.isnumeric() == False:
        numero2 = input("Ingresa siguiente numero: ")
        if numero2.lower() == "salir":
            exit()

    if operacion == "suma":
        numero1 = int(numero1) + int(numero2)
    elif operacion == "resta":
        numero1 = int(numero1) - int(numero2)
    elif operacion == "multi":
        numero1 = int(numero1) * int(numero2)
    else:
        numero1 = int(numero1) // int(numero2)
    print(f"El resultado es {numero1}.")
