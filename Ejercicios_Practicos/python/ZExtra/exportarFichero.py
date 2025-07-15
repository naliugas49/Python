def productTable(n):
    file1=open("tabla del numero"+str(n)+".txt","w")
    for i in range(1,11):
        pro = n*i
        file1.write(str(n)+"*"+str(i)+"="+str(pro)+'\n')#'\n'+
        print(str(n)+"*"+str(i)+"="+str(pro))
    file1.close() 


number = int(input('\n\n introduce un numero del 1 al 10 \n\n'))

while True:
    if not number:
        break
    if number > 10 or number < 1:
        print('numero inconrrecto intentelo de nuevo')
    else:
        productTable(number)
        break
        