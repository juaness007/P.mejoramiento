inicio=1
fin=10
lista=(inicio,fin)
def sumaPares():
    sumPares=0
    for a in range(inicio,fin+1):
        if a%2==0:
            print(a)
            sumPares+=a
    print(f'la suma de los numeros pares es: {sumPares}')
def sumaImpares():
    sumImpares=0
    for a in range(inicio,fin+1):
        if a%2==1:
            print(a)
            sumImpares+=a
    print(f'la suma de los numeros impares es: {sumImpares}')
sumaPares()
sumaImpares()