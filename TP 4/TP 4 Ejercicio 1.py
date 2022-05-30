class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getPrecio(self):
        return self.precio

    def View(self):
        print(
            "\nTitulo: " + (self.getTitulo()) + "\nAutor: " + (self.getAutor() + "\nPrecio: " + str(self.getPrecio())))


class Cliente:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getDireccion(self):
        return self.direccion

    def View(self):
        print("\nNombre: " + (self.getNombre()) + "\nEdad: " + (self.getEdad() + "\nDireccion: "
                                                                + str(self.getDireccion())))


titulo = input("Ingresar el TITULO del libro: ")
autor = input("Ingresar el AUTOR del libro: ")
precio = input("Ingresar el PRECIO del libro: ")

nombre = input("Ingresar el NOMBRE del cliente: ")
edad = input("Ingresar EDAD del cliente: ")
direccion = input("Ingresar la DIRECCION del cliente: ")

libro = Libro(titulo, autor, precio)
libro.View()
cliente = Cliente(nombre, edad, direccion)
cliente.View()

ListaLibros = []
ListaClientes = []


def ShowBooks():
    print(ListaLibros)


def ShowClients():
    print(ListaClientes)


def Assign():
    pass
