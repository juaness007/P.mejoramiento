from citas import *
class Paciente():
    citasAgenda=[]
    comprobante={}

    def __init__(self,nombrePaciente, tipoDocumento, documento, fecha, hora, consultorio, nombreDoctor, motivo):
        super().__init__(nombrePaciente, tipoDocumento, documento, fecha, hora, consultorio, nombreDoctor, motivo)
        self.__nombrePaciente=nombrePaciente
        self.__tipoDocumento=tipoDocumento
        self.__documento=documento
        self.__nombreDoctor=nombreDoctor

        Paciente.citasAgenda=[]

    def registrarCitas(citasAgenda):
        print("""
            Registro de citas """)   
        nombrePaciente=input("Ingrese el nombre del paciente: ")
        tipoDocumento=input("Ingrese el tipo de documento: ")
        documento=int(input("Ingrese el numero de  documento: ")) 
        motivo=input("Ingrese el motivo de la cita: ")
        nombreDoctor=input("Ingrese el nombre del doctor: ")
        fecha=input("Ingrese la fecha en el siguiente orden DD/MM/AAAA: ")
        hora=input("Ingrese la hora de la cita: ")
        consultorio=int(input("Ingrese el numero de consultorio: "))
        es = input("Escriba la especialdiad del medico: ")
        print('Su cita ha sido regitrada exitosamente')

        
        nuevaCita = citas(nombrePaciente, tipoDocumento, documento, fecha, hora, consultorio, nombreDoctor, es, motivo)
        
        Paciente.citasAgenda.append(nuevaCita)
        
        
    def eliminarCitas ():
        for l in citas.citasGeneral:
            eliminarCitas= input('Ingrese el nombre del paciente con el cual registró la cita: ')
            if eliminarCitas == l.getNombre():
                Paciente.citasAgenda.remove(l)
                citas.citasGeneral.remove(l)
            print("Su cita ha sido eliminada con exito!")

    def consultarCitas():
        print("Su cita es :")
        for k in citas.citasGeneral:
            print(f"""
            {k.getcitas()}            """)
            if k not in citas.citasGeneral:
                print('Usted no tiene ninguna cita agendada')
    def getpaciente (self):
        return f'{self.__tipoDocumento},{self.__documento}'