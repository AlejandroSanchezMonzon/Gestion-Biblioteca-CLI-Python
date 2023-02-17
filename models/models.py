class Usuario:
    def __init__(self, dni, nombre, email, telefono, domicilio):
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.domicilio = domicilio
        self.libros = []

class Libro:
    def __init__(self, isbn, titulo, autor, genero, portada, sinopsis, ejemplares):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.portada = portada
        self.sinopsis = sinopsis
        self.ejemplares = ejemplares
        self.usuario = None
        self.fecha_prestamo = None        