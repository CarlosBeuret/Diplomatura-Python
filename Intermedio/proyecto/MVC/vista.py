from tkinter import ttk
from tkinter import Tk
from tkinter import Label
from tkinter import StringVar
from tkinter import Button
from tkinter import Entry

from controlador import Controlador


class Vista:
    def __init__(self, controlador: Controlador):
        self.controlador = controlador

        self.master = Tk()

        self.var_titulo = StringVar()
        self.var_editorial = StringVar()
        self.var_nombre = StringVar()

        self.lbl_regreso = Label(self.master, text="")
        self.lbl_regreso.config(text="El libro se regreso con exito.")
        self.lbl_guardar = Label(self.master, text="")
        self.lbl_guardar.config(text="El libro se ha agregado correctamente.")
        self.lbl_borrar = Label(self.master, text="")
        self.lbl_borrar.config(text="El libro se ha borrado correctamente.")
        self.lbl_prestamo = Label(self.master, text="")
        self.lbl_prestamo.config(text="El prestamo se ha realizado correctamente.")

        self.tree = ttk.Treeview(self.master)
        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
        self.tree.column("#0", width=30, minwidth=50, anchor="w")
        self.tree.column("col1", width=80, minwidth=80, anchor="w")
        self.tree.column("col2", width=80, minwidth=80, anchor="w")
        self.tree.column("col3", width=100, minwidth=100, anchor="w")
        self.tree.column("col4", width=100, minwidth=100, anchor="w")
        self.tree.column("col5", width=100, minwidth=100, anchor="w")
        self.tree.column("col6", width=100, minwidth=100, anchor="w")

        self.tree.heading("col1", text="ID")
        self.tree.heading("col2", text="Titulo")
        self.tree.heading("col3", text="Editorial")
        self.tree.heading("col4", text="Estado")
        self.tree.heading("col5", text="Nombre")
        self.tree.heading("col6", text="Fecha")
        self.tree.grid(column=0, row=6, columnspan=6)

        self.boton_guardar = Button(
            self.master,
            text="Guardar",
            command=lambda: self.controlador.guardar(
                self.var_titulo, self.var_editorial, self.lbl_guardar, self.tree
            ),
        )
        self.boton_guardar.grid(row=0, column=0)
        self.boton_borrar = Button(
            self.master,
            text="Borrar",
            command=lambda: self.controlador.borrar(self.tree, self.lbl_borrar),
        )
        self.boton_borrar.grid(row=1, column=0)
        self.boton_prestamo = Button(
            self.master,
            text="Préstamo",
            command=lambda: self.controlador.prestamo(
                self.tree, self.var_nombre, self.lbl_prestamo
            ),
        )
        self.boton_prestamo.grid(row=0, column=2)
        self.boton_devolucion = Button(
            self.master,
            text="Devolución",
            command=lambda: self.controlador.devolucion(self.tree, self.lbl_regreso),
        )
        self.boton_devolucion.grid(row=1, column=2)
        self.boton_libros_prestados = Button(
            self.master,
            text="Libros prestados",
            command=lambda: self.controlador.mostrar_prestados(self.tree),
        )
        self.boton_libros_prestados.grid(row=0, column=4)
        self.boton_libros_totales = Button(
            self.master,
            text="Mostrar todo",
            command=lambda: self.controlador.mostrar_tabla(self.tree),
        )
        self.boton_libros_totales.grid(row=1, column=4)
        self.controlador.mostrar_tabla(self.tree)

        self.titulo = Label(self.master, text="Titulo ")
        self.titulo.grid(row=2, column=0, sticky="w")
        self.editorial = Label(
            self.master,
            text="Editorial",
        )
        self.editorial.grid(row=3, column=0, sticky="w")

        self.entry_titulo = Entry(self.master, textvariable=self.var_titulo, width=30)
        self.entry_titulo.grid(row=2, column=1)
        self.entry_editorial = Entry(
            self.master, textvariable=self.var_editorial, width=30
        )
        self.entry_editorial.grid(row=3, column=1)

        self.nombre = Label(self.master, text="Nombre ")
        self.nombre.grid(row=2, column=2, sticky="w")

        self.entry_nombre = Entry(self.master, textvariable=self.var_nombre, width=30)
        self.entry_nombre.grid(row=2, column=3)

        self.master.mainloop()
