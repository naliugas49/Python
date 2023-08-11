class Persona:
    def __init__(self,nombre,sexo,edad):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
    def info(self):
        print( f'su nombre es {self.nombre} de sexo {self.sexo} y edad {self.edad}\n' )
        
class Deportista(Persona):           ### dentro del parentesis se pone la clase padre
    def __init__(self,nombre,sexo,edad,rendimiento):  ## es necesario cargar todos los atributos de la clase padre ademas de los nuevos del hijo
        super().__init__(nombre,sexo,edad) ## aqui se define como el contructor de la clase padre dentro del contructor del hijo (super para hacer referencia qe los coja del padre)
        self.rendimiento = rendimiento 
    
class Futbolista(Persona):
    def __init__(self, nombre, sexo, edad, goles, asistencias):
        Persona.__init__(self,nombre, sexo, edad) ## esta es otra manera de definir el constructor haciendo referencia por el hombre especifico de la clase,  
        self.goles = goles                       ## OJO en este caso hay que poner como parametro el atributo self 
        self.asistencias = asistencias           ## Regularmente se usa cuando se va a trabajar con herencia multiple
        
##################### Herencia multiple ###############
class Fut_Depor(Futbolista,Deportista):
    def __init__(self, nombre, sexo, edad, goles, asistencias,rendimiento):
        Futbolista.__init__(self,nombre, sexo, edad, goles, asistencias)      
        Deportista.__init__(self,nombre,sexo,edad,rendimiento)

########## Instancias de las clases #########
Messi = Futbolista("Leonel Andres","masculino","35","807","325") 
dairon =Fut_Depor("Dairon Aguila","masculino","28","800","25","alto")


print(Messi.goles)
Messi.info()          ## aqui estamos utilizando el metodo info() que a pesar de no estar definida dentro de la clase Futbolista que es a la que hacemos 
                 ## referencia, hereda el metodo(la funcion) de su clase padre Persona
print (f'elrendimiento de {dairon.nombre} es {dairon.rendimiento}')

## Metodo de prueba para saber si una clase hereda de la otra y para saber si un objeto es instancia de una clase.

herencia = issubclass (Futbolista,Persona)
print(herencia)   # devuelve True o False 
instancia = isinstance(Messi,Futbolista)
print(instancia) # devuelve True o False