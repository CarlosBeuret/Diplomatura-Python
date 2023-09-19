import sqlite3
from tkinter.messagebox import showerror


class Modelo:
    def __init__(self, database_path):
        self.database_path = database_path
        self.con = sqlite3.connect(self.database_path)
        self.cursor = self.con.cursor()

    def crear_tabla(self):
        try:
            sql = """CREATE TABLE biblioteca (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                titulo TEXT,
                                editorial TEXT,
                                estado TEXT,
                                nombre TEXT,
                                fecha DATE
                            );"""
            self.cursor.execute(sql)
            self.con.commit()
        except:
            showerror("ERROR", "La base de datos ya ha sido creada.")

    def insert(self, titulo, editorial):
        data = (titulo.get(), editorial.get(), "Sin préstamo", "", "Null")
        sql = "INSERT INTO biblioteca(titulo, editorial, estado, nombre, fecha ) VALUES(?, ?, ?, ?, ?);"
        self.cursor.execute(sql, data)
        self.con.commit()
       
    def delete(self, id):
        sql = "DELETE FROM biblioteca WHERE id = ?;"
        self.cursor.execute(sql, id)
        self.con.commit()

    def update_prestamo(self, nombre, fecha, id):
        sql = "UPDATE biblioteca SET estado=?, nombre=?, fecha=? WHERE id=?"
        self.cursor.execute(sql, ("Prestado", nombre, fecha, id))
        self.con.commit()

    def update_devolucion(self, id):
        sql = "UPDATE biblioteca SET estado=?, nombre=?, fecha=? WHERE id=?"
        self.cursor.execute(sql, ("Sin préstamo", "", "Null", id))
        self.con.commit()

    def show_all(self):
        self.cursor.execute("SELECT * FROM biblioteca")
        datos = self.cursor.fetchall()

        return datos

    def show_prestados(self):
        self.cursor.execute("SELECT * FROM biblioteca WHERE estado = 'Prestado'")
        datos = self.cursor.fetchall()

        return datos
