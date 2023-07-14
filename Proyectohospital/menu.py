class menu:
    def __init__(self):
        pass
    def ingresar_al_sistema(self):
        print("""seleccione
1. Doctor
2. Paciente""") 
        while True:
            a=str(input('--> '))
            if a=='1' or a=='Doctor':
                print('ingreso al sistema')
                break
            elif a=='2' or a=='Paciente':
                print('ingreso al sistema')
                break
            else: print('error\n')
c1=menu()
c1.ingresar_al_sistema()