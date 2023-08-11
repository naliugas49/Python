################################################################################################################################
## MRO (Method Resolution Order): consiste en dar prioridad si existe una clase que hereda de otras 2 las cuales estas 2 padres poseen 
## algun (atributo o metodo) o algunos que sean iguales como saber cual elegir.
###############################################################################

## ejemplo con clases sin atributos solo metodos

# como funciona si no encuentra el metodo ejemplo: Pyrghon lo hace por ramas donde si la clase en  cuestion no tuviera el metodo lo busca
# en la primera clase padre de izquierda a derecha si no lo encuentra ahi 

    #    ##clase en cuestion D tiene el metodo?## ----> SI ---> lo ejecuta
    #                        |               
    #                       NO
    #                        |
    #  ##busca el metodo en la primera clase padre## ---> SI --> lo ejecuta
    #          ##de izquierda a derecha B ##
    #                        |
    #                        NO
    #                        |
    # ##la primera clase padre B hereda de alguien## ---> SI --> ##si la clase padre B hereda       --> SI --->  ##se busca el metodo en esa otra clase## 
    #                        |                                 ##de una clase distinta a la otra clase C#         ## la clase padre del padre##
    #                        NO                                                      |
    #                        |                                                       NO
    #   ##pues busca en otra clase padre C##                                         |
    #                                                            ## si heredan de la misma  salta para 
    #                                                               la otra clase padre y luego a la padre principal 
    #                                                                       padre de las otras 2#

class A:
    def ejemplo(self):
        print("Clase A")
class B:
    def ejemplo(self):
        print("Clase B")
class C(A):
    def ejemplo(self):
        print("Clase C")
class D(B,C):
    def ejemplo(super):
        print("Clase D")        

d = D()
d.ejemplo()

print(D.mro()) ##### con esta funcion te dice toda la ruta del mro


### si quiero ejecutar el metodo especifico de una clase en particular
A.ejemplo(d)  #estoy ejecuatando el metodo superior(A) con la clase que lo hereda todo y ademas pudiera tener sus propios atributos