from tkinter import * 
from tkinter import ttk
from tkinter import Label
from tkinter import messagebox
from datetime import datetime
import sqlite3
import re


master = Tk()

database_path = "database.db"
con = sqlite3.connect(database_path)


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


def crear_tabla():
    con = sqlite3.connect(database_path)
    cursor = con.cursor()
    sql =  """CREATE TABLE IF NOT EXISTS biblioteca (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT,
                        editorial TEXT,
                        estado TEXT,
                        nombre TEXT,
                        fecha DATE
                    );"""
    cursor.execute(sql)
    con.commit()
    con.close()


def obtener_datos():
    con = sqlite3.connect(database_path)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM biblioteca")
    datos = cursor.fetchall()
    con.close()
    return datos


def mostrar_tabla():
    datos = obtener_datos()
    tree.delete(*tree.get_children())
    for fila in datos:
        tree.insert("", "end", values=fila)

def libros_prestados():
    con = sqlite3.connect(database_path)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM biblioteca WHERE estado = 'Prestado'")
    datos = cursor.fetchall()
    con.close()
    return datos

def mostrar_prestados():
    datos = libros_prestados()
    tree.delete(*tree.get_children())
    for fila in datos:
        tree.insert("", "end", values=fila)

def guardar():
    if var_titulo.get() == "" or var_editorial.get() == "" :
        messagebox.showinfo("Complete datos", "Para realizar un ingreso debe completar titulo y editorial")
    else:
        con = sqlite3.connect(database_path)
        cursor = con.cursor()
        data = (var_titulo.get(),var_editorial.get(), "Sin prestamo", "", "Null" )
        sql = ("INSERT INTO biblioteca(titulo, editorial, estado, nombre, fecha ) VALUES(?, ?, ?, ?, ?);")
        cursor.execute(sql, data)
        con.commit()
        con.close()
        var_editorial.set("")
        var_titulo.set("")
        oculta_mensaje()        
        lbl_guardar.grid(column=1)
        mostrar_tabla()

def borrar():
    items = tree.focus()
    values = tree.item(items, "values")
    if len(values)== 0:
        messagebox.showinfo("Debe seleccionar", "Para hacer una devolucion debe seleccionar un libro.")
    else: 
        id = values[0]
        con = sqlite3.connect(database_path)
        cursor = con.cursor()
        sql = ("DELETE FROM biblioteca WHERE id = ?;")
        cursor.execute(sql, (id,))
        con.commit()
        con.close()
        oculta_mensaje()
        lbl_borrar.grid(column=1)
        mostrar_tabla()
   
def prestamo():
    items = tree.focus()
    values = tree.item(items, "values")
    
    var_fecha = datetime.now()
    
    if not re.match(r'^[a-zA-Z\s]+$', var_nombre.get()):
        messagebox.showinfo("Nombre inválido", "El nombre no puede estar vacio y debe contener solo letras mayúsculas, minúsculas y espacios.")

    elif len(values)== 0:
        messagebox.showinfo("Debe seleccionar", "Para hacer una devolucion debe seleccionar un libro.")
    else:    
        id = values[0]
        estado = values[3] 
        if estado == "Prestado":
            messagebox.showinfo("Ya se encuentra prestado", "Para realizar un prestamo no debe estar prestado previamente.")
        else:
            con = sqlite3.connect(database_path)
            cursor = con.cursor()
            sql = "UPDATE biblioteca SET estado=?, nombre=?, fecha=? WHERE id=?"
            cursor.execute(sql, ("Prestado", var_nombre.get(), var_fecha, id))
            con.commit()
            con.close()
            oculta_mensaje()
            lbl_prestamo.grid(column=1)
            mostrar_tabla()
            var_nombre.set("")
    

def devolucion():
    items = tree.focus()
    values = tree.item(items, "values")
   
    if len(values)== 0:
        messagebox.showinfo("Debe seleccionar", "Para hacer una devolucion debe seleccionar un libro.")
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
                messagebox.showinfo("Demora", f"El libro tiene una demora de {dias} dias")
                con = sqlite3.connect(database_path)
                cursor = con.cursor()
                sql = "UPDATE biblioteca SET estado=?, nombre=?, fecha=? WHERE id=?"
                cursor.execute(sql, ("Sin prestamo", "", "Null", id))
                con.commit()
                con.close()
                mostrar_tabla()
            else:
                messagebox.showinfo("Correcto", "Muchas gracias por devolver el libro en término.")
                con = sqlite3.connect(database_path)
                cursor = con.cursor()
                sql = "UPDATE biblioteca SET estado=?, nombre=?, fecha=? WHERE id=?"
                cursor.execute(sql, ("Sin prestamo", "", "Null", id))
                con.commit()
                con.close()
                oculta_mensaje()
                lbl_regreso.grid(column=1)
                mostrar_tabla()
  
def oculta_mensaje():
    lbl_regreso.grid_forget()
    lbl_prestamo.grid_forget()
    lbl_borrar.grid_forget()
    lbl_guardar.grid_forget()

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

boton_guardar = Button(master, text="Guardar", command= guardar) 
boton_guardar.grid(row=0, column=0)


boton_borrar = Button(master, text="Borrar", command= borrar) 
boton_borrar.grid(row=1, column=0)

boton_prestamo = Button(master, text="Prestamo", command= prestamo) 
boton_prestamo.grid(row=0, column=2) 

boton_devolucion = Button(master, text="Devolucion", command= devolucion) 
boton_devolucion.grid(row=1, column=2) 

boton_libros_prestados = Button(master, text="Libros prestados", command= mostrar_prestados) 
boton_libros_prestados.grid(row=0, column=4) 

boton_libros_totales = Button(master, text="Mostrar todo", command= mostrar_tabla) 
boton_libros_totales.grid(row=1, column=4) 
mostrar_tabla()


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