import sqlite3
from tkinter.messagebox import showerror


class Modelo:
    def __init__(self, database_path):
        self.database_path = database_path
        self.con = sqlite3.connect(self.database_path)
        self.cursor = self.con.cursor()
        
    def crear_tabla(self):
        """ Método utilizado para crear la tabla de la base de datos.
        """                        
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
        """Método utilizado para insertar valores en la base de datos.

        :param StringVar titulo: corresponde al título del libro.
        :param StringVar editorial: corresponde a la editorial del libro.
        """        
        data = (titulo.get(), editorial.get(), "Sin préstamo", "", "Null")
        sql = "INSERT INTO biblioteca(titulo, editorial, estado, nombre, fecha ) VALUES(?, ?, ?, ?, ?);"
        self.cursor.execute(sql, data)
        self.con.commit()
       
    def delete(self, id):
        """Método utilizado para borrar un valor de la base de datos.

        :param int id: Corresponde al id del libro.
        """        
        sql = "DELETE FROM biblioteca WHERE id = ?;"
        self.cursor.execute(sql, id)
        self.con.commit()

    def update_prestamo(self, nombre, fecha, id):
        """Método utilizado para actualizar un libro como prestado.

        :param str nombre: nombre de la persona que solicita el libro.
        :param datetime fecha: fecha y hora del préstamo.
        :param int id: identificador del libro.
        """        
        sql = "UPDATE biblioteca SET estado=?, nombre=?, fecha=? WHERE id=?"
        self.cursor.execute(sql, ("Prestado", nombre, fecha, id))
        self.con.commit()

    def update_devolucion(self, id):
        """Método utilizado para actualizar un libro como devuelto.

        :param int id: identificador del libro.
        """        
        sql = "UPDATE biblioteca SET estado=?, nombre=?, fecha=? WHERE id=?"
        self.cursor.execute(sql, ("Sin préstamo", "", "Null", id))
        self.con.commit()

    def show_all(self):
        """Método que devuelve todos los libros.

        :return list : listado de libros.
        """        
        self.cursor.execute("SELECT * FROM biblioteca")
        datos = self.cursor.fetchall()

        return datos

    def show_prestados(self):
        """Método que devuelve el listado de libros prestado.

        :return list: lista con los libros prestados.
        """        
        self.cursor.execute("SELECT * FROM biblioteca WHERE estado = 'Prestado'")
        datos = self.cursor.fetchall()

        return datos
