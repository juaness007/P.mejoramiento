#Solicite la hora en formato horas, minutos y  segundos. Imprima en pantalla la hora que será dentro 1 segundo

def hora(horas, minutos, segundos):
    segundos += 1

    if segundos >= 60:
        segundos = 0
        minutos += 1

        if minutos >= 60:
            minutos = 0
            horas += 1

            if horas >= 24:
                horas = 0

    return horas, minutos, segundos


horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))


nuevas_horas, nuevos_minutos, nuevos_segundos = hora(horas, minutos, segundos)


print(f"La hora dentro de 1 segundo será: {nuevas_horas}:{nuevos_minutos}:{nuevos_segundos}")
