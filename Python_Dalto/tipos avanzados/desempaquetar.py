numeros = [1, 2 ,3 ,4]
num1, num2, num3 = numeros

## si solo queremos obtener el primer valor
num1, *otros = numeros  # esto coge el primer valor y los demas los pone en una lista dentro de otros

# si quisiera el primero y el ultimo
num1, *otros, num_ultimo= numeros
