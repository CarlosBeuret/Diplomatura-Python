import sqlite3
import re
 

class Abmc:
    def __init__(self, ): 
        try:
            con = sqlite3.connect("mibase.db")
            cursor = con.cursor()
            sql = """CREATE TABLE productos
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    producto varchar(20) NOT NULL,
                    cantidad real,
                    precio real)
            """
            cursor.execute(sql)
            con.commit()
        except:
            print("Hay un error")


    def conexion(self,):
        con = sqlite3.connect("mibase.db")
        return con

    def alta(self, producto, cantidad, precio, tree):
        cadena = producto.get()
        patron="^[A-Za-záéíóú]*$"  #regex para el campo cadena
        if(re.match(patron, cadena)):
            print(producto.get(), cantidad.get(), precio.get())
            con=self.conexion()
            cursor=con.cursor()
            data=(producto.get(), cantidad.get(), precio.get())
            sql="INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
            cursor.execute(sql, data)
            con.commit()
            print("Estoy en alta todo ok")
            self.actualizar_treeview(tree)
            producto.set('') 
            cantidad.set('') 
            precio.set('')
            return "ACCIÓN COMPLETADA CORRECTAMENTE"
        else:
            print("error en campo producto")
            return "Existio un error"


    def consultar(self, ):
        global compra
        print(compra)

    def borrar(self, tree):
        valor = tree.selection()
        print(valor)   #('I005',)
        item = tree.item(valor)
        print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
        print(item['text'])
        mi_id = item['text']

        con=self.conexion()
        cursor=con.cursor()
        #mi_id = int(mi_id)
        data = (mi_id,)
        sql = "DELETE FROM productos WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(valor)

    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        sql = "SELECT * FROM productos ORDER BY id ASC"
        con=self.conexion()
        cursor=con.cursor()
        datos=cursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))