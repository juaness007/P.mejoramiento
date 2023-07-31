#solicitar 2 numeros por teclado e imprimir el cociente y el residuo del mayor en el menor sin utilizar la division ni el mod

def calcular_cociente_residuo():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    cociente = 0
    residuo = max(num1, num2)

    while residuo >= min(num1, num2):
        residuo -= min(num1, num2)
        cociente += 1

    print("El cociente del mayor en el menor es:", cociente)
    print("El residuo del mayor en el menor es:", residuo)


calcular_cociente_residuo()

