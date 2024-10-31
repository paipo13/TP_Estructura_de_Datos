import datetime
import random
class Mail:
    def __init__(self):
        self.bandeja= []

class Nodo:
    def __init__(self,valor):
        self.valor=valor
        self.derecho=None
        self.izquierdo=None
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
    
class Arbol :
    def __init__(self,nodo=None):
        self. raiz=None
    def agg(self,nodo):
        if self.raiz==None:
            self.raiz=nodo
        else:
            raiz=self.raiz
            raiz.agregarnodos(nodo)
    def preorder(self,nodo):
        if nodo:
            print(nodo.valor)
            self.preorder(nodo.izquierdo)
            self.preorder(nodo.derecho)

def fecha():
    return datetime.datetime(random.randint(1990,2024),random.randint(1,12), random.randint(1,25), random.randint(0,23), random.randint(0,59))

mails=Arbol(Nodo(['Hola',fecha(),"Leido"]))
mails.agg(Nodo(['Chau',fecha(),"Leido"]))
mails.agg(Nodo(["buenas",fecha(),"Leido"]))

mails.preorder(mails.raiz)

