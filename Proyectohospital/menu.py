class menú:
    def __init__(self):
        pass

    def ingreso(self):
        print("""
    Bienvenido al menú, seleccione una opción 
    1 Doctor 
    2 Paciente    """)
    
    while True:
        a=input("-->")
        if a == "1":
            print("Hola Doctor /n que  accion quiere realizar")
        break    
D1=menú()
print(D1.ingreso())   