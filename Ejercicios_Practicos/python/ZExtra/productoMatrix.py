# array = [ [2,4,6], [8,10,12], [14,16,18,20] ]
# print([c for f in array for c in f])


# list = [["Rohan", 60], ["Aviral", 21],  
#         ["Harsh", 30], ["Rahul", 40], 
#         ["Raj", 20]] 

# for names in list: 
#     print(names[0], "is", names[1], 
#           "years old.") 

#####################################################################################################################
# Escribir un programa que almacene las matrices
# en una lista y muestre por pantalla su producto.
############ Nota ####: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
#####################################################################################################################

from array import array


A = [ [1,2,3],
      [4,5,6],
      [1,2,3]] 

B = [ [-1,0,3],
      [ 0,1,4],
      [ 1,1,4]]


#     size = (len(A[0]))


pro = 0
l = [] 
l1 = []
for j in range(len(A)):
    for k in range(len(B[0])):
        for i in  range(len(B)):
            pro += A[j][i]*B[i][k]
        print(pro)
        l1.append(pro) 
        pro =0
    l.extend([l1])
    l1=[]
print(l)       
        


