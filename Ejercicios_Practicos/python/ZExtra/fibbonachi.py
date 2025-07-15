#0 1 1 2 3 5 8 12
number=int(input('escribe un numero \n'))
n=1
c=0
if number == 1:
    print('0')
elif number ==2:
    print('1')
else:
    for i in range(0,number-2):
        n=n+c
        c=n-c
        print(n)