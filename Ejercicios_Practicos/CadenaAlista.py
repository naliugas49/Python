# Escribe una función que convierta una cadena en una lista de palabras (utilizando split) y otra función 
# que haga lo contrario (convierta una lista de palabras en una cadena).

cadena = ("dairon aguila cardenas")
listaDePAlabras = cadena.split(" ")
print(listaDePAlabras)

cadenaDeLista = ""
for i in listaDePAlabras:
    cadenaDeLista = cadenaDeLista + " " + i
print(cadenaDeLista)


