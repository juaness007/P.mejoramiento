#1. Determinar los divisores de un número introducido por teclado
#2. Determinar si un numero es o no es primo
#3. Determinar si un número es o no es perfecto. Un numero es
#perfecto si la suma de sus divisores sin incluir el propio
#número es igual a este
#4. Determinar cuales y cuantos números perfectos hay entre 1 y
#1000?
#5. ¿Cuáles y cuántos son los números primos comprendidos
#entre 1 y 1000?
#6. Calcular el máximo de números positivos introducidos por
#teclado, sabiendo que metemos números hasta que
#introduzcamos uno negativo. El negativo no cuenta.#

import random 
lista = []
def primos (lista):
    lista2 = []
    cont = 0
    contPrimos = 0
    tam = random.randrange (5,15)
    for i in range (tam):
        numero = random.randrange(0,1000)
        lista.append(numero)
    print (lista)

    for q in lista:
        cont = 0
        for w in range (1,q + 1):
            if q % w == 0:
                cont = cont + 1
            else:
                continue 
    
        if cont == 2:
            contPrimos = contPrimos + 1
            lista2.append(q)
    return f"La cantidad de numero primos es {contPrimos} y los numeros son: {lista2}"
print (primos(lista))