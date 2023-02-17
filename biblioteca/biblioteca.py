from datetime import datetime

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []

    def alta_usuario(self, usuario):
        self.usuarios.append(usuario)
        print("Usuario agregado.")
        print("\n")

    def alta_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado.")
        print("\n")

    def baja_usuario(self, dni):
        usuario = self.buscar_usuario(dni)
        if usuario:
            self.usuarios.remove(usuario)
            print("Usuario eliminado.")
            print("\n")
            return True
        return False

    def baja_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro:
            self.libros.remove(libro)
            print("Libro eliminado.")
            print("\n")
            return True
        return False

    def prestar_libro(self, isbn, dni):
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(dni)

        if libro and usuario:
            libro.usuario = usuario
            libro.fecha_prestamo = datetime.now().date()
            print("Libro prestado.")
            print("\n")
            return True
        return False

    def devolver_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro:
            libro.usuario = None
            libro.fecha_prestamo = None
            print("Libro devuelto.")
            print("\n")
            return True
        return False

    def consultar_libros(self):
        for libro in self.libros:
            print(f"{libro.titulo} · {libro.autor} · {libro.isbn}")
            print("\n")

    def consultar_usuarios(self):
        for usuario in self.usuarios:
            print(f"{usuario.nombre} + {usuario.dni}")
            print("\n")

    def consultar_prestamos(self):
        for libro in self.libros:
            if libro.usuario:
                print(f"{libro.titulo} · {libro.usuario.nombre} · {libro.fecha_prestamo}")
                print("\n")

    def buscar_usuario(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario
        return None

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None