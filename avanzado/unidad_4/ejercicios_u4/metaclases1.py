def extender_clase(self, arg):
    print(arg)



class MiClase1: pass

MiClase1.extender_clase=extender_clase

objeto=MiClase1()
objeto.extender_clase("Este método se ha agregado a la clase")