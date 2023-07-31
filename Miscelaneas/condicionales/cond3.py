# Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número exceda los límites emita un mensaje y finalice el programa

def contCifras():
    num = int(input("Ingrese un numero mayor que 0 y menor que 9999: "))

    if num < 0 or num > 9999:
        print("El número excede los límites.")
    else:
        cifras = len(str(num))
        print("El número tiene", cifras, "cifras.")

contCifras()