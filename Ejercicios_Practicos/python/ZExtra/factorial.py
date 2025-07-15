def factorial(n):
    c=n-1
    while c > 1:
        n=n*c
        c=c-1
    return n

number = ( int ( input('escribe un numero entero \n')))
print (factorial (number))
print(number)

def factorial1(n1):
    for i in range(2,n1):
        n1 = n1*i
    return n1

print ( factorial1 ( int ( input('escribe un numero entero \n'))))

# def factorial2(n2):
#     for (x = 2; x <= n2; x++):
#         n2 = n2*x
#     return n2

# print ( factorial2 ( int ( input('escribe un numero entero \n'))))