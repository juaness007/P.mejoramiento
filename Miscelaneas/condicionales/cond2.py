#Escribe un programa que pida tres numeros y que escriba si son los tres iguales , si hay dos iguales, o si los tres son distintos

def comparador():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    num3 = int(input("Ingrese el tercer numero: "))

    if num1 == num2 == num3 :
        print ("Los tres numeros son iguales")

    elif num2 == num1 or num2 == num3  or num1 == num3:
        print ("Hay dos numeros iguales")

    else:
        print ("Los tres numeros son diferentes")

comparador()        