class Tema:
    
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)


class TemaConcreto(Tema):
    def __init__(self):
        self.estado = None

    def set_estado(self, value):
        self.estado = value
        self.notificar()

    def get_estado(self):
        return self.estado


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserver(Observador):
    def __init__(self, obj):
        self.observador = obj
        self.observador.agregar(self)

    def update(self, *args):
        
        print(f"El libro fue {args[0]}.")
        

