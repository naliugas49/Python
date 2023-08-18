class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor1"   ## atributo  privado.. se define con _
        self.__atribute_private = "Valor2"  ## atributo muy privado al que no se puede acceder se defne con __
    def __hablar(self):                     ## tambien se pueden hacer los metodos 
        print("hola")
 
objeto1 = MiClase()
print(objeto1._atributo_privado)
#print(objeto1.__atribute_private)

