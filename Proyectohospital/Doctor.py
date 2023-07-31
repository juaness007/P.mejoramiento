from paciente import *
from citas import *
class doctor ():
    especialidad=[]
    dic={}
    def __init__(self, nombrePaciente, tipoDocumento, documento, fecha, hora, consultorio, nombreDoctor, motivo):
        nombrePaciente=nombrePaciente
        tipoDocumento=tipoDocumento
        documento=documento
        fecha=fecha
        hora=hora
        consultorio=consultorio
        nombreDoctor=nombreDoctor
        motivo=motivo
        doctor.especialidad=[]
        doctor.dic={}

    def consultarCitas():
        print("Su cita es: ")
        for k in citas.citasGeneral:
            print(f"""
            {k.getcitas()}""")
            if k not in citas.citasGeneral:
                print('Usted no tiene ninguna cita agendada')   

    def getdoctor(self):
        return f'{self.__consultorio},{self.especialidad}'

      