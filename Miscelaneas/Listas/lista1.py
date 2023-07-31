
import random
tam = 10
rango = 20
def llenarLista(tam,rango):
    lista=[]

    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):       
    sum=0                  
    for x in lista:          
        sum+=x               
    return sum

def promedioLista(lista):     
    return sumaLista(lista)/len(lista)  


def mayorLista(lista):        
    maximo = lista[0]                    
    for i in lista:
        if i > maximo:
            maximo=i
    return f"El numero mayor de la lista es: {maximo}"

def menorLista(lista):
    minimo=lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
    return f"El numero menor de la lista es: {minimo}"

def moda(lista):
    max=0
    for i in lista:
        cont=0
        for o in lista:
            if i == o:
                cont+=1
        if cont > max:
            max = cont
            moda1= i
    return f'La moda es: {moda1} ya que se repite {max}'


def ascendente(lista):
    aux=0
    for i in range(len(lista)):             
        for j in range(i+1,len(lista)):     
            if lista[i] > lista[j]:         
                aux = lista[i]              
                lista[i] = lista[j]
                lista[j] = aux
    return f"Lista1 ordenada ascendentemente{lista}"


def mediana(lista):
    if len(lista) %2!=0:                    
        aux = (len(lista)+1)//2           
        return lista[aux-1]
    else:
        aux  = (len(lista) - 1) // 2       
        aux1 = (lista [aux])
        aux2 = (lista[aux + 1])
        aux  = aux1 + aux2                 
        aux  = aux // 2
    return f"La mediana de la lista1 es: {aux}"

def descendente(lista):
    aux=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return f"Lista1 ordenada descendentemente{lista}"


lista1 = llenarLista (tam,rango)
print (lista1)
print ("La lista contiene", len(lista1), "numeros")
print(f"La suma de la lista 1 es:", sumaLista(lista1))
print(f"El promedio de la lista 1 es: ", promedioLista(lista1))
print(mayorLista(lista1))
print(menorLista(lista1))
print(moda(lista1))
print(ascendente(lista1))
print(mediana(lista1))
print(descendente(lista1))