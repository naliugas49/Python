# #print(dir(dic))
# print(dic['pepe'])
# print(dic.get('juan'))
# print(dic.setdefault('e',5))

from operator import getitem

def wen():
    dic = {}
    while True:
        entrada = input('escribe un nombre \n')
        if not entrada:
            break
        dic[entrada] += 1 if entrada in dic.keys() else 1
        
def dac():
    dic={}
    while True:
        x = input('escribe un nombre \n')
        if not x:
            break            
        if x in dic.keys():
            dic[x] +=1
        else:
           dic[x]=1
    Max(dic)
        
def Max(dicc):
    for key, value in dicc.items():
        x =  max(dicc.values())
        if value == x:
            t = key, x
            print ( t) 
            
print (dac())    

     
# dicc = {'dairon': 2, 'pepe': 2, 'juan': 1}
# for key, value in  dicc.items():
#     if value == max(dicc.values()):
#         print (key,max(dicc.values())) 
    

