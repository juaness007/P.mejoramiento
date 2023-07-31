#Llenar lista con la serie de fibonacci, con la cantidad de digitos que el usuario indique al inicio del programa

def fibonacci(x):
    if x == 0:                      
        return 0
    elif x == 1:                    
        return 1                    
    else:                           
        num1 = 0
        num2 = 1

        for i in range(x - 1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3

        return num2

lista = []

num = int(input("Ingrese la cantidad de números de la serie de Fibonacci que desea ver: "))

for i in range(num):
    lista.append(fibonacci(i))

print(lista)