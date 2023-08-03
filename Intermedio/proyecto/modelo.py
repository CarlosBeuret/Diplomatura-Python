import sqlite3
from tkinter import messagebox
import re
from datetime import datetime

database_path = "database.db"
con = sqlite3.connect(database_path)

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

def guardar(var_titulo, var_editorial, lbl_guardar, tree):
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
        oculta_mensaje_guardar(lbl_guardar)        
        
        mostrar_tabla(tree)

def oculta_mensaje_guardar(lbl_guardar):
    lbl_guardar.grid_forget()
    lbl_guardar.grid(column=1)

def borrar(tree, lbl_borrar):
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
        oculta_mensaje_borrar(lbl_borrar)
        lbl_borrar.grid(column=1)
        mostrar_tabla(tree)

def oculta_mensaje_borrar(lbl_borrar):
    lbl_borrar.grid_forget()

def prestamo(tree, var_nombre, lbl_prestamo):
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
            oculta_mensaje_prestamo(lbl_prestamo)
            lbl_prestamo.grid(column=1)
            mostrar_tabla(tree)
            var_nombre.set("")

def oculta_mensaje_prestamo(lbl_prestamo):
      lbl_prestamo.grid_forget()

def devolucion(tree, lbl_regreso):
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
                mostrar_tabla(tree)
            else:
                messagebox.showinfo("Correcto", "Muchas gracias por devolver el libro en término.")
                con = sqlite3.connect(database_path)
                cursor = con.cursor()
                sql = "UPDATE biblioteca SET estado=?, nombre=?, fecha=? WHERE id=?"
                cursor.execute(sql, ("Sin prestamo", "", "Null", id))
                con.commit()
                con.close()
                oculta_mensaje_regreso(lbl_regreso)
                lbl_regreso.grid(column=1)
                mostrar_tabla(tree)

def oculta_mensaje_regreso(lbl_regreso):
    lbl_regreso.grid_forget()

def obtener_datos():
    con = sqlite3.connect(database_path)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM biblioteca")
    datos = cursor.fetchall()
    con.close()
    return datos

def mostrar_tabla(tree):
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

def mostrar_prestados(tree):
    datos = libros_prestados()
    tree.delete(*tree.get_children())
    for fila in datos:
        tree.insert("", "end", values=fila)