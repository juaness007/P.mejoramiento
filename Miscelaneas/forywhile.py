n=int(input('introduzca un numero:'))
sumaDivisores=0
for a in  range (1,n):
    if a % n == 0:
          print(f"{a} es primo de {n} ")
    else:print(f" {a} no es primo de {n} ")
      
for b in range (1,n//2+1):
    if n%b ==0:
        print(f'{b} es perfecto')
    else:print(f'{b} no es perfecto')
sumaDivisores+=b       
if sumaDivisores == n:
     True
else:
     False        
        
           