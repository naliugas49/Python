 ## Crear clase estudiante que tenga los atributos
 # nombre
 # edad
 # grado
 
 #### metodos estudiar()  " el estudiante (nombre) esta estuduando"
#Crear un objeto Estudiante y usar el metodo estudiar()
### se debe interactuar con el usuario y este debe brindar los atributos , luego de esto se instancia la clase  

class Estudiante:
    def __init__(self,nombre,edad,grado) :
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f'el estudiante {self.nombre} esta estudiando')


nombre = input("escriba su nombre: ")
edad = input("Escriba su edad: ")
grado = input ("digame en que grado se encuentra:  ")

estudiante = Estudiante(nombre,edad,grado)   ## instanciar la clase
print(f""" 
      el nombre del estudiante es {estudiante.nombre} \n
      la edad del estudiante es {estudiante.edad} \n
      el grado del estudiante es {estudiante.grado} \n     
      """)
   

estudiante.estudiar()
