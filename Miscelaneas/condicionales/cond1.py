#Pedir 3 numeros e indicar cual es el numero del medio Ej. 11,2,1000 ,el del medio es el 11
def numMedio():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    numero3 = int(input("Ingrese el tercer numero: "))

    if numero1 < numero2 < numero3 or numero3 < numero2 < numero1:
        print ("El numero medio es ", numero2)

    elif numero2 < numero1 < numero3 or numero3 < numero1 < numero2:
        print ("El numero medio es ", numero1)

    else:
        print ("E numero medio es ", numero3)

numMedio()    