class Celular():
    marca = "Samsung"
    modelo = "S23"
    camara = "48Mpx"
    
celular1 = Celular.marca
print(celular1)
##############################################
### Constructor de una clase ###
class CelularBest:
    def __init__ (self,marca,modelo,camara):
        self.marca = marca             #Se definen los atributos de la clase
        self.modelo = modelo
        self.camar = camara
    ## creamos metodos sencillos
    def llamar (self):
        print(f'estas llamando de un celular modelo{self.modelo}')  
       

celular2 = CelularBest("Apple","iPhone14","12Mpx")
celular3 = CelularBest("Nothing","NothingPhone2","48Mpx")

print(celular2.marca)
celular2.llamar()