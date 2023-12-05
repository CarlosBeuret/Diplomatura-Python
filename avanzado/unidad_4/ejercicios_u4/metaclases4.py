class ControlMotor(type):
    encendido=False

class Material: 
    material='plastico'

class Auto(Material, metaclass=ControlMotor):
    marca="renault"

    def __init__(self, color):
        self.color=color
    
    def retornar_color(self, valor):
        return self.color+str(valor)

objeto=Auto("azul")
print(objeto.material)
print(Auto.__dict__)
print(Auto.__dict__['marca'])
print(Auto.encendido)
try:
    print(objeto.encendido)
except:
    print("La instancias de una clase no puede acceder a la metaclase")