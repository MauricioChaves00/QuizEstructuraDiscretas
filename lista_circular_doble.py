
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None


class ListaCircularDoble:
    def __init__(self):
        self.cabeza = None
        self.actual = None

    # Agregar una canción al final de la lista
    def insertar(self, cancion):
        nuevo = Nodo(cancion)

        # Caso 1: lista vacía
        if self.cabeza is None:
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo

            self.cabeza = nuevo
            self.actual = nuevo

        # Caso 2: lista con canciones
        else:
            ultimo = self.cabeza.anterior

            nuevo.siguiente = self.cabeza
            nuevo.anterior = ultimo

            ultimo.siguiente = nuevo
            self.cabeza.anterior = nuevo

    # Avanzar a la siguiente canción
    def siguiente(self):
        if self.actual is None:
            return None

        self.actual = self.actual.siguiente
        return self.actual.cancion

    # Retroceder a la canción anterior
    def anterior(self):
        if self.actual is None:
            return None

        self.actual = self.actual.anterior
        return self.actual.cancion