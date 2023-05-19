"""
Ejercicio8
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada

"""
 
compra=[]
total=0
# VISTA
def menu():
    print("\n Elija una opción:")
    print("(a) Agregar producto:")
    print("(e) Eliminar producto:")
    print("(l) Listar producto:")
    print("(m) Modificar producto:")
    print("ó cualquier otra tecla para salir:")
    global valor
    global eleccion
    eleccion=input()
    if eleccion=="a" or eleccion=="e" or eleccion=="l" or eleccion=="m":
        valor=True
    else:
        valor=False
menu()

# MODELO
def alta(): print("Estoy en alta")
def borrar(): print("Estoy en borrar")
def listar(): print("Estoy en listar")
def modificar(): print("Estoy en modificar")

# CONTROLADOR
while valor==True:
    print("elección: ", eleccion)

    if eleccion=="a":
        alta()
    elif eleccion=="e":
        borrar()
    elif eleccion=="l":
        listar()       
    elif eleccion=="m":
        modificar()
    else:
        break
    menu()
 