class menú:
    def __init__(self):
        pass

    def ingreso(self):
        print("""
    Bienvenido al menú, seleccione una opción:
    1 Doctor 
    2 Paciente    """)
    
        while True:
            a=input("-->")
            if a == "1":
                print("""Hola Doctor, selecciona tu especialidad: 
                      1 Medicina general 
                      2 Odontología 
                      3 Pediatría  """)
                while True:
                    a=input("-->")
                    if a == "1" or a== 'Medicina general':
                        """"conectar con citas.py"""
                        pass
                        break
                    elif a=='2' or a=='Odontologia':
                        pass
                        break
                    elif a=='3' or a=='Pediatria':
                        pass
                        break
                    else: 'error, elija una opcion disponible'
                                    
                break
            elif a=="2":
                print("""Hola Paciente que acción quiere realizar
1 Registrar cita
2 Eliminar cita
3 Consultar citas""")
                while True:
                    a=input('--> ')
                    if a=='1':
                        pass
                        break
                    elif a=='2':
                        pass
                        break
                    elif a=='3':
                        pass
                        break
                    else:print('opcion no disponible o incorrecta :c')
                break 
                
            else: 
                print("Error, elija una opcion correcta")  
                   
                  


D1=menú()
D1.ingreso()


