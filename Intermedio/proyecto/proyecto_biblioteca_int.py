from tkinter import * 
from tkinter import ttk
from tkinter import Label

from modelo import mostrar_prestados
from modelo import guardar
from modelo import borrar
from modelo import prestamo
from modelo import mostrar_tabla
from modelo import devolucion
from modelo import crear_tabla

crear_tabla()

master = Tk()

var_titulo = StringVar()
var_editorial = StringVar()
var_nombre = StringVar()

lbl_regreso = Label(master, text="")
lbl_regreso.config(text="El libro se regreso con exito.")
lbl_guardar = Label(master, text="")
lbl_guardar.config(text="El libro se ha agregado correctamente.")
lbl_borrar = Label(master, text="")
lbl_borrar.config(text="El libro se ha borrado correctamente.")
lbl_prestamo = Label(master, text="")
lbl_prestamo.config(text="El prestamo se ha realizado correctamente.")

tree = ttk.Treeview(master)
tree["columns"] = ("col1", "col2", "col3","col4", "col5", "col6")
tree.column("#0", width= 30, minwidth=50, anchor=W)
tree.column("col1", width= 80, minwidth=80, anchor=W)
tree.column("col2", width= 80, minwidth=80, anchor=W)
tree.column("col3", width= 100, minwidth=100, anchor=W)
tree.column("col4", width= 100, minwidth=100, anchor=W)
tree.column("col5", width= 100, minwidth=100, anchor=W)
tree.column("col6", width= 100, minwidth=100, anchor=W)

tree.heading("col1", text="ID")
tree.heading("col2", text="Titulo")
tree.heading("col3", text="Editorial")
tree.heading("col4", text="Estado") 
tree.heading("col5", text="Nombre")
tree.heading("col6", text="Fecha")
tree.grid(column=0, row=6, columnspan=6)

boton_guardar = Button(master, text="Guardar", command= lambda: guardar(var_titulo, var_editorial, lbl_guardar, tree)) 
boton_guardar.grid(row=0, column=0)
boton_borrar = Button(master, text="Borrar", command= lambda: borrar(tree, lbl_borrar)) 
boton_borrar.grid(row=1, column=0)
boton_prestamo = Button(master, text="Prestamo", command =lambda: prestamo(tree, var_nombre, lbl_prestamo)) 
boton_prestamo.grid(row=0, column=2) 
boton_devolucion = Button(master, text="Devolucion", command=lambda: devolucion(tree, lbl_regreso)) 
boton_devolucion.grid(row=1, column=2) 
boton_libros_prestados = Button(master, text="Libros prestados", command= lambda: mostrar_prestados(tree)) 
boton_libros_prestados.grid(row=0, column=4) 
boton_libros_totales = Button(master, text="Mostrar todo", command= lambda: mostrar_tabla(tree)) 
boton_libros_totales.grid(row=1, column=4) 
mostrar_tabla(tree)

titulo = Label(master, text = "Titulo ")
titulo.grid(row=2, column= 0, sticky= W)
editorial = Label(master, text = "Editorial", )
editorial.grid(row=3, column= 0, sticky= W) 

entry_titulo = Entry(master, textvariable= var_titulo, width= 30) 
entry_titulo.grid(row=2, column= 1)
entry_editorial = Entry(master, textvariable= var_editorial, width= 30)
entry_editorial.grid(row=3, column= 1)

nombre = Label(master, text = "Nombre ")
nombre.grid(row=2, column= 2, sticky=W)

entry_nombre = Entry(master, textvariable= var_nombre, width= 30) 
entry_nombre.grid(row=2, column=3)

master.mainloop()