from utils import Item, Node

class LinkedListV2:
    
    def __init__(self) -> None:
        self.node = None
        self.last = None
        self.size = 0

    def insert(self, x: Item, pos): 
        counter = 1
        node = Node(x)
        if pos == 0 and self.node != None:
            node.next_node = self.node
            self.node = node
            return counter
        elif pos == 0:
            self.node = Node(x)
            self.last = self.node
            return counter
        elif pos == self.size:
            self.last.next_node = Node(x)
            self.last = self.last.next_node
            return counter

        pointer = self.node
        while pos - 1:
            counter += 1
            pointer = pointer.next_node
            pos -= 1

        next_node = pointer.next_node
        pointer.next_node = node
        node.next_node = next_node
        if pointer == self.last:
            self.last = node
        self.size += 1

        return counter

    def locate(self, pos):
        if not self.node:
            return -1
        
        node = self.node
        while pos:
            node = node.next_node
            if node == None:
                return node
            pos -= 1
        return node.item  

    def remove(self, pos):
        counter = 1
        if not self.node:
            print("A lista está vazia. Não é possível remover.")
            return counter
        if pos == 0:
            item = self.node.item
            self.node = self.node.next_node
            return item, counter

        anterior = None
        atual = self.node
        contador = 0

        while atual:
            counter += 1
            if contador == pos:
                anterior.proximo = atual.proximo
                self.size -= 1
                return counter, atual.item
            anterior = atual
            atual = atual.proximo
            contador += 1