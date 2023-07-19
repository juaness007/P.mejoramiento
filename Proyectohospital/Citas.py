class citas:
    def __init__(self,nombrePaciente,tipoDocumento,documento,fecha,hora,consultorio,nombreDoctor,motivo):
        self.__nombrePaciente=nombrePaciente
        self.__tipoDocumento=tipoDocumento
        self.__documento=documento
        self.__fecha=fecha
        self.__hora=hora
        self.__consultorio=consultorio
        self.__nombreDoctor=nombreDoctor
        self.__motivo=motivo
        

    def getcitas(self):
            return f'{self.__nombreDoctor},{self.__fecha / self.__hora},{self.__motivo},{self.__consultorio},'
