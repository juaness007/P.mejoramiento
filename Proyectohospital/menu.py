from citas import *
from doctor import *

while True:
    print("""
---------------
seleccione
1. Doctor
2. Paciente
---------------""")
    a=str(input('--> '))
    if a == "1" or a == "Doctor": 
        print(''' 
---------------
1. Consultar citas agendadas 
2. Registrar Citas
3. Salir 
---------------                     ''')
        a=str(input('--> '))
        if a == '1' or a == 'Consultar citas agendadas':      
            doctor.consultarCitas()
        elif a == '3' or a == 'Salir':
            break
        else:
            print('La opcion que ingreso no es valida intente de nuevo')
        a=str(input('--> '))
    if a == '2' or a == 'Paciente':
            print(''' 
---------------
1.Registrar citas
2.Consultar citas
3.Eliminar citas
---------------                   ''')
            b=str(input('--> '))        
            if b == '1' or b == 'Registar citas':
                Paciente.registrarCitas(Paciente.citasAgenda)
            if b == '2' or b =='Consultar citas':
                Paciente.consultarCitas()
            elif b == '3' or b == 'Eliminar citas':
                Paciente.eliminarCitas()
            elif b == '0' or b =='Salir':    
               break            
            else:
                print('La opcion que ingreso no es valida intente de nuevo ')
