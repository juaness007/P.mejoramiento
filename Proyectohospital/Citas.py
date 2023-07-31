class citas:
    citasGeneral = []
    def __init__(self,nombrePaciente,tipoDocumento,documento,fecha,hora,consultorio,       nombreDoctor,       especialidad,motivo):
        self.__nombrePaciente=nombrePaciente
        self.__tipoDocumento=tipoDocumento
        self.__documento=documento
        self.__fecha=fecha
        self.__hora=hora
        self.__consultorio=consultorio
        self.__nombreDoctor=nombreDoctor
        self.__especialidad=especialidad
        self.__motivo=motivo
        
        citas.citasGeneral.append(self)
        

    def getcitas(self):
        return f''' -------------------------------
                Nombre del paciente:{self.__nombrePaciente} 
                Tipo de documento:{self.__tipoDocumento}
                Numero de documento:{self.__documento}
                Fecha de la cita:{self.__fecha}
                Hora de la cita:{self.__hora}
                Numero de consultorio:{self.__consultorio}
                Nombre del doctor:{self.__nombreDoctor}
                Motivo de la cita:{self.__motivo}
                Especialidad de la cita:{self.__especialidad}
            -------------------------------'''
        
    def getNombre(self):
        return self.__nombrePaciente