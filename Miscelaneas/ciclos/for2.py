#Determinar si un numero es primo o no es primo 


def Primos ():
    for num in range (1,80):
        if num >1:
            for i in range (2, num):
             if (num%i)==0:
                break
            else:
             print (f'{num} Es primo ')
             
Primos ()