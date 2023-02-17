from biblioteca.biblioteca import Biblioteca
from models.models import Libro, Usuario


def main():
    biblioteca = Biblioteca()

    while True:
        print("1. Alta de usuario.")
        print("2. Baja de usuario.")
        print("3. Alta de libro.")
        print("4. Baja de libro.")
        print("5. Prestar libro.")
        print("6. Devolver libro.")
        print("7. Consultar libros.")
        print("8. Consultar usuarios.")
        print("9. Consultar prestamos.")
        print("10. Salir.")
        opcion = input("-> Ingrese una opcion: ")

        print("\n")

        if opcion == "1":
            dni = input("Ingrese su DNI: ")
            nombre = input("Ingrese su nombre: ")
            email = input("Ingrese su email: ")
            telefono = input("Ingrese su telefono: ")
            domicilio = input("Ingrese su domicilio: ")

            usuario = Usuario(dni, nombre, email, telefono, domicilio)
            biblioteca.alta_usuario(usuario)

        elif opcion == "2":
            dni = input("Ingrese el DNI del usuario a eliminar: ")
            biblioteca.baja_usuario(dni)

        elif opcion == "3":
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            genero = input("Ingrese el genero del libro: ")
            portada = input("Ingrese la portada del libro: ")
            sinopsis = input("Ingrese la sinopsis del libro: ")
            ejemplares = int(input("Ingrese la cantidad de ejemplares: "))

            libro = Libro(isbn, titulo, autor, genero, portada, sinopsis, ejemplares)
            biblioteca.alta_libro(libro)

        elif opcion == "4":
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.baja_libro(isbn)

        elif opcion == "5":
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            dni = input("Ingrese el DNI del usuario que presta el libro: ")
            biblioteca.prestar_libro(isbn, dni)

        elif opcion == "6":
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            biblioteca.devolver_libro(isbn)

        elif opcion == "7":
            biblioteca.consultar_libros()

        elif opcion == "8":
            biblioteca.consultar_usuarios()

        elif opcion == "9":
            biblioteca.consultar_prestamos()

        elif opcion == "10":
            break

        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    main()