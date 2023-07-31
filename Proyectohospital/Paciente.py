from citas import *
class Paciente():
    citasAgenda=[]
    # comprobante={}

    def __init__(self,nombrePaciente, tipoDocumento, documento, fecha, hora, consultorio, nombreDoctor, motivo):
        super().__init__(nombrePaciente, tipoDocumento, documento, fecha, hora, consultorio, nombreDoctor, motivo)
        self.__nombrePaciente=nombrePaciente
        self.__tipoDocumento=tipoDocumento
        self.__documento=documento
        self.__nombreDoctor=nombreDoctor

        Paciente.citasAgenda=[]
        # Paciente.comprobante={}

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

        Paciente.comprobante={"Nombre del paciente: " : nombrePaciente,
                              "Tipo de documento: " : tipoDocumento,
                              "Documento: ": documento,
                              "Motivo de  la consulta: ":motivo,
                              "Nombre del doctor: ":nombreDoctor,
                              "Fecha:  ":fecha,
                              "Hora: ":hora,
                              "Consultorio: ":consultorio}
        
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
        print("Inicio del metodo")
        for k in citas.citasGeneral:
            print(f"""
            {k.getcitas()}
                  
            """)
        # for Paciente.comprobante in Paciente.citasAgenda:
        #     consulta= input("Ingrese el nombre del paciente con el cual registró la cita: ")
        #     if Paciente.comprobante["nombrePaciente"] == consulta:
        #         print(" Usted tiene una cita")
        #         print('Nombre doctor:',Paciente.comprobante['nombreDoctor'])
        #         print('Nombre del consultorio:',Paciente.comprobante['consultorio'])
        #         print('Fecha de la cita:',Paciente.comprobante['fecha'])
        #         print('Hora',Paciente.comprobante['hora'])
        #     else:
        #         print('Usted no tiene ninguna cita agendada')

    def getpaciente (self):
        return f'{self.__tipoDocumento},{self.__documento}'