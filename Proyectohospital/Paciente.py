from citas import *
class Paciente(citas):
    citasAgenda=[]
    comprobante={}

    def __init__(self, nombrePaciente, tipoDocumento, documento, fecha, hora, consultorio, nombreDoctor, motivo):
        super().__init__(nombrePaciente, tipoDocumento, documento, fecha, hora, consultorio, nombreDoctor, motivo)
        self.__nombrePaciente=nombrePaciente
        self.__tipoDocumento=tipoDocumento
        self.__documento=documento
        self.__nombreDoctor=nombreDoctor

        Paciente.citasAgenda=[]
        Paciente.comprobante={}

    def registrarCitas(citasAgenda):
        print("""
            Registro de citas """)   
        nombrePaciente=input("Ingrese el nombre del paciente: ")
        tipoDocumento=input("Ingrese el tipo de documento: ")
        documento=int(input("Ingrese el numero de  documento: ")) 
        motivo=input("Ingrese el motivo de la cita:  ")
        nombreDoctor=input("Ingrese el nombre del doctor: ")
        fecha=input("Ingrese la fecha en el siguiente orden DD/MM/AAAA: ")
        hora=input("Ingrese la hora de la cita: ")
        consultorio=int(input("Ingrese el numero de consultorio: "))

        Paciente.comprobante={"Nombre del paciente: " : nombrePaciente,
                              "Tipo de documento: " : tipoDocumento,
                              "Documento: ": documento,
                              "Motivo de  la consulta: ":motivo,
                              "Nombre del doctor: ":nombreDoctor,
                              "Fecha:  ":fecha,
                              "Hora: ":hora,
                              "Consultorio: ":consultorio}
        
    def eliminarCitas ():
        for Paciente.comprobante in Paciente.citasAgenda:
            eliminarCitas= input('Ingrese el nombre del paciente con el cual registró la cita: ')
            if Paciente.comprobante ['nombrePaciente'] == eliminarCitas:
                Paciente.citasAgenda.remove(Paciente.comprobante)
                print("Su cita ha sido eliminada con exito!")

    def consultarCitas():
        for Paciente.comprobante in Paciente.citasAgenda:
            consulta= input("Ingrese el nombre del paciente con el cual registró la cita: ")
            if Paciente.comprobante["nombrePaciente"] == consulta:
                print(" Usted tiene una cita")
                print(Paciente.comprobante)
            else:
                print('Usted no tiene ninguna cita agendada')

    def                     