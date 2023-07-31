

def numerodivisores():
        n = int (input("Ingrese un numero: "))
        i=0
        while True:
            i+=1
            if n % i ==0:                                   
                print(f"El numero {i} es divisor de {n}")
        
            if n==i:
                break

numerodivisores()            