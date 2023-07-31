#Calcular el maximo de numeros positivos introducidos por teclado 
#sabiendo que metemos numeros hasta que introduzcamos uno negativo

def maximoPositivo():
    maximo = -1  
    suma = 0    

    while True:
        numero = int(input("Introduce un número: "))
        
        if numero < 0:
            break

        suma += numero  

        if numero > maximo:
            maximo = numero  

    if maximo == -1:
        print("No se introdujeron números positivos.")
    else:
        print("El máximo de los números positivos es:", maximo)

    print("La suma de los números positivos es:", suma)

maximoPositivo()
