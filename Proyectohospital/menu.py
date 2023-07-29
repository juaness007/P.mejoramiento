#from citas import *
#from doctor import *

def ingresar_al_sistema(self):
        while True:
            a=str(input('--> '))
            print("""
---------------
seleccione
1. Doctor
2. Paciente
---------------
""") 
            a=str(input('--> '))
            if a == "1" or a == "Doctor": 
                print(''' 
---------------
1. Consultar citas agendadas 
2. Salir 
---------------                     
''')
        