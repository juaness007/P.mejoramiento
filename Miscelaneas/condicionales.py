i = 0
par = 0
impar = 0
lista=[1,2,3,4,5,6,7,8,9,10]

def sumaPares(lista):
   for i in range (lista):
    i = i + 1
    resultado = i % 2
    if resultado == 0:
     par = par + i 

def sumaImpares():
   for i in range (0,10):
    i = i + 1
    resultado = i % 2
    if resultado != 0:
     impar = impar + i 

print('la suma de los pares es:', (sumaPares(lista)))       
  




    #elif resultado != 0:
      # impar = impar + i

