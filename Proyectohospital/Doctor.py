from paciente import *

class doctor():
    def __init__(self,especialidad,nombre,noDocumento,consultorio,disponibilidad):
        self.__especialidad=especialidad
        self.__nombre=nombre
        self.__noDocumento=noDocumento
        self.__consultorio=consultorio
        self.__disponibilidad=disponibilidad
    def consultarCitas():
        print("""
        Consulta agenda de citas  """)
    busquedaCitas=input("Ingrese el nombre del paciente: ")
    for citas in Paciente.citasAgenda:
        if busquedaCitas == citas ["Nombre del paciente :"]:
            print("La cita está agendada: ")
            print("Paciente: ", Paciente.comprobante ["Nombre del paciente"] )
            print("Medico: ", Paciente.comprobante["Nombre del doctor: "])
            print("hora: ", Paciente.comprobante ["Hora: "])
            print("consultorio: ", Paciente.comprobante["Consultorio: "])
            print("motivo: ",Paciente.comprobante["Motivo: "])

        else:
            print("No fue posible encontrar la busqueda",busquedaCitas)

def getmedico(self):
        return f'{self.__especialidad},{self.__nombre},{self.__noDocumento},{self.___disponibilidad},{self.__consultorio}'