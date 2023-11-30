from MVC.modelo import Modelo
from MVC.controlador import Controlador
from MVC.vista import Vista


if __name__== "__main__":
    
    modelo = Modelo("database.db")
    modelo.crear_tabla() # Si se lo corre por segunda vez se ejecuta la excepción.
    controlador = Controlador(modelo)
    vista = Vista(controlador)