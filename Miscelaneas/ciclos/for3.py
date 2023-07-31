#Determinar cuales son los multiplos de 5 comprendidos entre 1 y n

def multiplos():
    n=int(input('Introduzca un numero: '))
    for i in range(11):
        if i%5==0:
            print(f'{i} es multiplo de 5')
        else:
            print(i)
multiplos()