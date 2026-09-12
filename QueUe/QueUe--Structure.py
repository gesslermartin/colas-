from collections import deque


class Queue:

    def __init__(self):
        self._items = deque()

    def enqueue(self, elemento):
        self._items.append(elemento)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.popleft()

    def front(self):
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def mostrar(self):
        return list(self._items)

    def eliminar_fondo(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def eliminar_frente(self):
        if self.is_empty():
            return None
        return self._items.popleft()

    def vaciar(self):
        self._items.clear()
        
    def colocar_al_frente(self, elemento):
       self._items.appendleft(elemento)

    def mover_primer_negativo_al_fondo(self):
        for elemento in list(self._items):
            if elemento < 0:
                self._items.remove(elemento)
                self._items.append(elemento)
                return elemento
        return None

    def mover_mayor_a_la_cima(self):
        if self.is_empty():
            return None

        mayor = max(self._items)
        self._items.remove(mayor)
        self._items.appendleft(mayor)

        return mayor
    
