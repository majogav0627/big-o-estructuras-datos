class NodoBST:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.carnet = estudiante["carnet"]
        self.izquierdo = None
        self.derecho = None

class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, estudiante):
        if not self.raiz:
            self.raiz = NodoBST(estudiante)
        else:
            self._insertar_recursivo(self.raiz, estudiante)

    def _insertar_recursivo(self, actual, estudiante):
        if estudiante["carnet"] < actual.carnet:
            if not actual.izquierdo:
                actual.izquierdo = NodoBST(estudiante)
            else:
                self._insertar_recursivo(actual.izquierdo, estudiante)
        else:
            if not actual.derecho:
                actual.derecho = NodoBST(estudiante)
            else:
                self._insertar_recursivo(actual.derecho, estudiante)

    def buscar(self, carnet):
        return self._buscar_recursivo(self.raiz, carnet)

    def _buscar_recursivo(self, actual, carnet):
        if not actual or actual.carnet == carnet:
            return actual.estudiante if actual else None
        if carnet < actual.carnet:
            return self._buscar_recursivo(actual.izquierdo, carnet)
        return self._buscar_recursivo(actual.derecho, carnet)