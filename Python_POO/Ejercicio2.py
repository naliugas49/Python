# Herencias Ejercicio 2
# Ejercicio de herencia y uso de super:
# Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales: Persona y Estudiante.
# La clase Persona tendrá los atributos de nombre y edad y un método que imprima el nombre y la edad de la persona.
# La clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional: grado y un método que imprima el grado del
# estudiante.
# Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre(Persona). 
# Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para asegurarte de que todo 
# funciona correctamente

class Persona:
    def __init__(self,nombre,edad,):
        self.nombre = nombre
        self.edad = edad

    def mostar_datos(self):
        print(f'su nombre es {self.nombre}\nsu edad {self.edad}')

class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def mostar_grado(self):
        print(f'el grado del estudiante es {self.grado}')

estudiante1=Estudiante("Jorge","23","3ro")

estudiante1.mostar_datos()
estudiante1.mostar_grado()