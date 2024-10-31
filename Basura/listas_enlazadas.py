# Creamos una clase ListaEnlazada que nos permitirá gestionar de manera eficiente los contactos y aplicaciones instaladas. 
# Posteriormente, la utilizaremos en otras funcionalidades del teléfono.

class Nodo():
    """
    Clase Nodo para ser utilizada en la Lista Enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada():
    """
    Implementa una lista enlazada simple.
    """
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        """
        Agrega un nuevo elemento al principio de la lista.
        """
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        """
        Muestra los elementos de la lista.
        """
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
    
    def buscar(self, dato):
        """
        Busca un elemento en la lista y devuelve su posición.
        Si no lo encuentra, devuelve -1.
        """
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1
    
    def eliminar(self, dato):
        """
        Elimina el primer elemento con el dato dado de la lista.
        Si no lo encuentra, no hace nada.
        """
        if self.cabeza and self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return
        
        actual = self.cabeza
        while actual and actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
    
    def invertir(self):
        """
        Invierte la lista.
        """
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente_nodo = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente_nodo
        self.cabeza = anterior
    
    def obtener_tamanio(self):
        """
        Devuelve el tamaño de la lista.
        """
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def buscar_devuelve_True_or_False(self, dato):
        """
        Busca un elemento en la lista y devuelve True si lo encuentra, False si no.
        """
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False