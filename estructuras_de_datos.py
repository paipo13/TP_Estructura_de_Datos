

class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
    
    def agregarnodos(raiz,nodo):
        if raiz.valor[1]<nodo.valor[1]:
            if raiz.derecho==None:
                raiz.derecho=nodo
            else:
                raiz.derecho.agregarnodos(nodo)
        elif raiz.valor[1]>nodo.valor[1]:
            if raiz.izquierdo==None:
                raiz.izquierdo=nodo
            else:
                raiz.izquierdo.agregarnodos(nodo)


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def esta_vacia(self):
        return len(self.items) == 0

class Cola:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def esta_vacia(self):
        return len(self.items) == 0