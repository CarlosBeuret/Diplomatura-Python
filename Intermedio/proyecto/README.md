# Proyecto Biblioteca

Este es un proyecto que consiste en la creación de una aplicación para una biblioteca desarrollada en Python con interfaz gráfica de usuario utilizando Tkinter. Permite llevar un stock actulizado de libros, y visualizar si estos estan prestados o no, a quien y cuando. También, permite verificar si la devolución se hizo en tiempo o con retraso.

## Requisitos

Asegúrate de tener instalado Python en tu sistema.

## Instalación

1. Clona o descarga este repositorio en tu máquina local.
2. Ejecuta el archivo main.py para crear la database y agregar algunos libros de ejemplo.


## Uso

1. Ejecuta el archivo `main.py` para iniciar la aplicación. Al ejecutarla se abrirá la interfaz gráfica de usuario.
2. La aplicación te permite realizar las siguientes acciones:
- Agregar un libro (alta): Completa el título y la editorial del libro y presiona el botón "Guardar".
- Borrar un libro (baja): Selecciona un libro de la lista y presiona el botón "Borrar".
- Realizar un préstamo (modificación): Selecciona un libro de la lista, ingresa el nombre de la persona a la que se le presta el libro y presiona el botón "Préstamo". Se ultiliza expresión regular para verificar el nombre ingresado.
- Realizar una devolución (modificación): Selecciona un libro prestado de la lista y presiona el botón "Devolución". La aplicación mostrará si el libro fue devuelto en tiempo o con retraso.
- Mostrar libros prestados (consulta): presiona el boton "Libros Prestados" y se mostrará la lista de libros actualmente prestados.
- Mostrar todos los libros (consulta): presiona el boton "Mostrar Todo" y se mostrara la lista completa de libros en la biblioteca.
3. Los resultados de las acciones se mostrarán en la interfaz de usuario y podrás ver los cambios reflejados en la lista de libros. En la parte inferior se muestran los eventos realizados.


