import sqlite3

database_path = "database.db"


valores = [
    ("Quijote", "Atlantida", "Sin prestamo", "", "Null"),
    ("Martin Fierro", "Billiken", "Prestado", "Carlos", "2023-06-06 19:34:10.123456"),
    ("El Hobbit", "Alba", "Sin prestamo", "", "Null"),
    ("Rayuela", "Planeta", "Sin prestamo", "", "Null"),
    ("El señor de los granillos", "Estrada", "Prestado", "Juan", "2023-06-26 19:34:10.123456"),
    ("Matrix", "AZ", "Sin prestamo", "", "Null")
]


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

def insertar_valores():
    con = sqlite3.connect(database_path)
    cursor = con.cursor()
    for dato in valores:
        cursor.execute("INSERT INTO biblioteca (titulo, editorial, estado, nombre, fecha) VALUES (?, ?, ?, ?, ?)", dato)


    con.commit()
    con.close()
    
crear_tabla()

insertar_valores()
