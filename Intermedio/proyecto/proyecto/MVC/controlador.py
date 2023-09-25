from tkinter import messagebox
import re
from datetime import datetime


from MVC.modelo import Modelo


class Controlador:
    def __init__(self, modelo: Modelo) -> None:
        """Constructor de la clase Controlador.

        :param Modelo modelo: se le pasa un objeto de la clase Modelo
        """        
        self.modelo = modelo

    def crear_tabla(self):
        self.modelo.crear_tabla

    def guardar(self, var_titulo, var_editorial, lbl_guardar, tree):
        """Método que contiene la lógica para guardar libros en la base de datos.

        :param Stringvar var_titulo: contiene el titulo del libro.
        :param Stringvar var_editorial: contiene el nombre de la editorial. 
        :param Label lbl_guardar: botón de guardado
        :param ttk.Treeview tree: treeview
        """        
        if var_titulo.get() == "" or var_editorial.get() == "":
            messagebox.showinfo(
                "Complete datos",
                "Para realizar un ingreso debe completar titulo y editorial",
            )
        else:
            self.modelo.insert(var_titulo, var_editorial)

            var_editorial.set("")
            var_titulo.set("")
            self.oculta_mensaje_guardar(lbl_guardar)
            self.mostrar_tabla(tree)

    def oculta_mensaje_guardar(self, lbl_guardar):
        lbl_guardar.grid_forget()
        lbl_guardar.grid(column=1)

    def borrar(self, tree, lbl_borrar):
        """Método que contiene la lógica para borrar libros.

        :param Treeview tree: treeview
        :param Label lbl_borrar: botón de borrado.
        """        
        items = tree.focus()
        values = tree.item(items, "values")
        if len(values) == 0:
            messagebox.showinfo(
                "Debe seleccionar",
                "Para hacer una devolución debe seleccionar un libro.",
            )
        else:
            self.modelo.delete(id=values[0])
            self.oculta_mensaje_borrar(lbl_borrar)
            lbl_borrar.grid(column=1)
            self.mostrar_tabla(tree)

    def oculta_mensaje_borrar(self, lbl_borrar):
        lbl_borrar.grid_forget()

    def prestamo(self, tree, var_nombre, lbl_prestamo):
        """Método que contiene la lógica para dar en préstamo un libro.

        :param Treeview tree: treeview.
        :param Stringvar var_nombre: contiene el nombre del libro.
        :param Label lbl_prestamo: botón de préstamo.
        """        
        items = tree.focus()
        values = tree.item(items, "values")

        var_fecha = datetime.now()

        if not re.match(r"^[a-zA-Z\s]+$", var_nombre.get()):
            messagebox.showinfo(
                "Nombre inválido",
                "El nombre no puede estar vació y debe contener solo letras mayúsculas, minúsculas o espacios.",
            )

        elif len(values) == 0:
            messagebox.showinfo(
                "Debe seleccionar",
                "Para hacer una devolución debe seleccionar un libro.",
            )
        else:
            id = values[0]
            estado = values[3]
            if estado == "Prestado":
                messagebox.showinfo(
                    "Ya se encuentra prestado",
                    "Para realizar un préstamo no debe estar prestado previamente.",
                )
            else:
                self.modelo.update_prestamo(var_nombre.get(), var_fecha, id)
                self.oculta_mensaje_prestamo(lbl_prestamo)
                lbl_prestamo.grid(column=1)
                self.mostrar_tabla(tree)
                var_nombre.set("")

    def oculta_mensaje_prestamo(self, lbl_prestamo):
        lbl_prestamo.grid_forget()

    def devolucion(self, tree, lbl_regreso):
        """Método que contiene la lógica para la devolución de un libro.

        :param Treeview tree: treeview
        :param Label lbl_regreso: botón de regreso
        """        
        items = tree.focus()
        values = tree.item(items, "values")

        if len(values) == 0:
            messagebox.showinfo(
                "Debe seleccionar",
                "Para hacer una devolución debe seleccionar un libro.",
            )
        else:
            id = values[0]
            estado = values[3]
            fecha = values[5]
            if estado == "Sin prestamo":
                messagebox.showinfo("Mensaje", "El libro no ha sido prestado")
            else:
                fecha = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S.%f")
                fecha_actual = datetime.now()
                lapso = fecha_actual - fecha
                dias = lapso.days
                if dias > 7:
                    messagebox.showinfo(
                        "Demora", f"El libro tiene una demora de {dias} días"
                    )
                    self.modelo.update_devolucion(id)
                    self.mostrar_tabla(tree)
                else:
                    messagebox.showinfo(
                        "Correcto", "Muchas gracias por devolver el libro en término."
                    )
                    self.modelo.update_devolucion(id)
                    self.oculta_mensaje_regreso(lbl_regreso)
                    lbl_regreso.grid(column=1)
                    self.mostrar_tabla(tree)

    def oculta_mensaje_regreso(self, lbl_regreso):
        lbl_regreso.grid_forget()

    def obtener_datos(self):
        """Método que retorna listado con todos los libros.

        :return list: listado con todos los libros.
        """        
        return self.modelo.show_all()

    def mostrar_tabla(self, tree):
        """Método para mostrar todos los libros.

        
        """        
        datos = self.obtener_datos()
        tree.delete(*tree.get_children())
        for fila in datos:
            tree.insert("", "end", values=fila)

    def libros_prestados(self):
        """Método que retorna todos los libros prestados.

        """        
        return self.modelo.show_prestados()

    def mostrar_prestados(self, tree):
        """Método que muestra todos los libros prestados.

        """        
        datos = self.libros_prestados()
        tree.delete(*tree.get_children())
        for fila in datos:
            tree.insert("", "end", values=fila)
