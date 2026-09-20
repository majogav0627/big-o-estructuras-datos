class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def buscar(self, carnet):
        actual = self.cabeza
        while actual:
            if actual.dato["carnet"] == carnet:
                return actual.dato
            actual = actual.siguiente
        return None