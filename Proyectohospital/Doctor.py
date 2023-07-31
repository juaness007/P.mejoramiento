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
        for Paciente.comprobante in Paciente.citasAgenda:
            consulta= input ('Ingrese el nombre del paciente: ')
            if Paciente.comprobante["nombrePaciente"] == consulta:
                print(""" Usted tiene una cita
                      Nombre del paciente : """ , Paciente.comprobante ["nombrePaciente"])
                print("Documento", Paciente.comprobante ["documento"])
                print("Fecha", Paciente.comprobante ["fecha"])
                print("Hora",Paciente.comprobante["hora"])
                print("Motivo" , Paciente.comprobante["motivo"])
                print("Nombre doctor", Paciente.comprobante["nombreDoctor"])
                print("Consultorio", Paciente.comprobante["consultorio"])
            else:
                print('Usted no tiene citas:(')  

    def getdoctor(self):
        return f'{self.__consultorio},{self.especialidad}'

      