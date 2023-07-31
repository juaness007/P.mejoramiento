#pedir una nota de 0 a 10 y mostrarla de la forma: insuficiente, Suficiente ,bien
def obtener_calificacion(nota):
    if 0 <= nota < 5:
        return "Insuficiente"
    elif 5 <= nota < 7:
        return "Suficiente"
    elif 7 <= nota <= 10:
        return "Bien"
    else:
        return "Nota inválida"

try:
    nota = float(input("Introduce la nota (0-10): "))
    calificacion = obtener_calificacion(nota)
    print(f"La calificación es: {calificacion}")
except ValueError:
    print("Entrada inválida. Debes introducir un número válido.")

