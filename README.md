# Práctica: Proyecto gestión de una biblioteca en Python

Realiza una aplicación en Python que permita realizar la gestión de una biblioteca. Los requisitos son los siguientes:

    La biblioteca tendrá un listado de usuarios de la biblioteca y de libros.
    Datos de los usuario: dni, nombre, correo electrónico, teléfono, domicilio, libros en préstamo.
    Datos de libro: ISBN, título, autor, genero, portada, sinopsis, ejemplares, usuario que ha recibido el libro en préstamo, fecha de préstamo.
    La aplicación funcionará mediante un menú interactivo presentado en una CLI con las siguientes opciones:
        - Alta de socio
        - Baja de socio
        - Alta de libro
        - Baja de libro
        - Prestar libro
        - Devolver libro
        - Consultar libros
        - Consultar usuarios
        - Consultar prestamos
        - Salir

Utiliza POO para realizar el proyecto. Utiliza una estructura similar a esta:

<code>
Biblioteca/

    biblioteca/

    tests/

    doc/

    LICENSE

    README.md

    requirements.txt

    main.py
</code>

Opcionalmente:

    Utiliza una BBDD para almacenar el proyecto (puedes utilizar SQLite3 o una base de datos externa).
    Implementa los test unitarios mediante pytest o unittest.
    Añade un archivo setup.py.
    Realiza una GUI mediante Tk, wxPython o Kivy.

---