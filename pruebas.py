from paciente import *
from menu import *
class doctor(menu):
    def __init__(self):
        super().__init__()
    def especialidad(self):
        while True:
            a=str(input('--> '))
            if a=='1' or a=='Doctor':
                print('''Bienvenido al menú, seleccione su especialidad:
1.Odontologia
2.Medicina general 
3.Pediatria''')
                while True:
                    a=str(input('--> '))
                    if a=='1' or a=='Odontologia':
                        print("""Que acción quiere realizar
1.Consultar citas Odontologia           
2.Salir """)
                        while True:
                            a=str(input('--> '))
                            if a == '1' or a=='Cosultar citas Odontologia':
                                


                        break
                    elif a== '2' or a== 'Medicina  general':
                        print("""Que acción quiere realizar
1.Consultar citas Medicina general 
2.Salir """)
                        break
                    elif a==3 or a== 'Pediatria':
                        print("""Que acción quiere realizar
1.Consultar citas Pediatria 
2.Salir """)
                        break
                    else: print('error\n')    
            
            elif a=='2' or a=='Paciente':
                print('''Bienvenido al menú, que acción desea realizar: 
1. Regitrar citas 
2. Consultar citas
3. Eliminar citas ''')
                while True:
                    a=str(input('--> '))
                    if a=='1' or a=='Registrar citas':
                        print(""" Seleccione la especialidad de la cita  
1.Odontologia 
2.Medicina general
3.Pediatria""")
                        break
                    elif a=='2' or a== 'Consultar citas':
                        print(""" Seleccione la especialidad de la cita  
1.Odontologia 
2.Medicina general                         
3.Pediatria""")
                        break
                    elif a=='3' or a== 'Eliminar citas':
                        print(""" Seleccione la especialidad de la cita  
1.Odontologia 
2.Medicina general                         
3.Pediatria""")                                                                                           
                        break
                    else: print('error\n')
c1=doctor()
c1.ingresar_al_sistema()   
c1.especialidad()