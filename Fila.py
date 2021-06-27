from Node import Node
from Apartamento import Apartamento

class Fila:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    # inserir na fila
    def push(self, torreid, name, adress, apartamentoid, number, vaga):
        node = Apartamento(torreid, name, adress, apartamentoid, number, vaga)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    # remover da fila
    def pop(self):
        if self._size > 0:
            elem = self.first.apartamentoid
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._size = self._size - 1
            return elem
        raise IndexError("A fila está vazia")

    # ver fila
    def peek(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.apartamentoid) + " "
                pointer = pointer.next
            return r
        raise IndexError("A fila está vazia")


    def __len__(self):
        return self._size


    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.apartamentoid) + " "
                pointer = pointer.next
            return r
        return "A fila está vazia"

    def __str__(self):
        return self.__repr__()