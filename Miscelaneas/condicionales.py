# El ejercicio 1 consta de un codigo que haga un bucle del 1 al 10 y haga la suma de todos los numeros pares y por
# aparte la suma de todos los numeros impares 


inicio=0
fin=0
lista=(inicio,fin)
def sumaPares(inicio,fin):
    sumPares=0
    for a in range(inicio,fin+1):
        if a%2==0:
            print(a)
            sumPares+=a
    print(f'la suma de los numeros pares es: {sumPares}')
def sumaImpares(inicio,fin):
    sumImpares=0
    for a in range(inicio,fin+1):
        if a%2==1:
            print(a)
            sumImpares+=a
    print(f'la suma de los numeros impares es: {sumImpares}')
sumaPares(1,10)
sumaImpares(1,10)

#----------------------------------------------------------------
# El ejercicio 2 constara de un codigo donde el usuario pueda ingresar la hora, los minutos
# y los segundos actuales, el sistema le mostrara que horas son un segundo despues de la 
# hora que inserto 

hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

def hora():
    hora = int(input("Ingrese la hora: "))
    if hora == 24 and segundos == 59:
        hora = 0
    elif hora < 24 and segundos == 59 and minutos == 59:
        hora = hora + 1

def minutos():
    if minutos == 59 and segundos == 59:
        minutos = 1
    elif minutos < 59 and segundos == 59:
        minutos = minutos + 1

def segundos():
    if segundos == 59:
        segundos = 0
    elif segundos < 59:
        segundos = segundos + 1

print ('Son las :', (hora) , 'horas con ',(minutos) ,'minutos y ' ,(segundos) ,':')