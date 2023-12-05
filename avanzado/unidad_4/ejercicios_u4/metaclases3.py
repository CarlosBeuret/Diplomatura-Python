class MiMetaclase(type):
    def __new__(meta, nombre_de_clase, superclase, diccionario_de_clase):
        print('En __new__ de metaclase: ', meta, nombre_de_clase, superclase, diccionario_de_clase, sep='\n...')
        return type.__new__(meta, nombre_de_clase, superclase, diccionario_de_clase)

    def __init__(Clase, nombre_de_clase, superclase, diccionario_de_clase):
        print('En __init__ de metaclase: ', nombre_de_clase, superclase, diccionario_de_clase, sep='\n...')
        print('... init objeto de clase', list(Clase.__dict__.keys()))

class MiSuperclase: pass

class MiClase(MiSuperclase, metaclass=MiMetaclase):
    atributo1=1
    def metodo1(self, arg):
        return self.atributo1+3*arg

print("Creando una instancia")
x=MiClase()
print('atributo1: ', x.atributo1, x.metodo1(7)) 