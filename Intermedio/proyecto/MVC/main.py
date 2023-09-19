from vista import Vista
from modelo import Modelo
from controlador import Controlador



if __name__== "__main__":
    
    modelo = Modelo("database.db")
    modelo.crear_tabla() # Si se lo corre por segunda vez se ejecuta la excepción.
    controlador = Controlador(modelo)
    vista = Vista(controlador)