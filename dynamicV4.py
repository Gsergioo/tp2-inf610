from utils import  Item

class NodeDoubleLinked:
    
    def __init__(self, item) -> None:
        self.next = None
        self.previous = None
        self.Item = Item


class LinkedListV3:
    
    def __init__(self) -> None:
        self.head = NodeDoubleLinked(None)
        self.last = None
        self.size = 0

    def insert(self, x: Item, pos): 
        counter = 1
        node = NodeDoubleLinked(x)
        if pos == self.size:
            self.last.next_node = node
            self.last = self.last.next_node

        pointer = self.head.next_node
        while pos - 1:
            counter += 1
            pointer = pointer.next_node
            pos -= 1

        counter += 1
        next_node = pointer.next_node
        pointer.next_node = node
        node.next_node = next_node
        next_node.previous = pointer
        if pointer == self.last:
            self.last = node
        self.size += 1

        return counter

    def locate(self, pos):
        if not self.node:
            return -1
        
        node = self.head.next_node
        while pos:
            node = node.next_node
            if node == None:
                return None
            pos -= 1
        return node.item 

    def remove(self, pos):
        counter += 1
        if not self.node:
            print("A lista está vazia. Não é possível remover.")
            return -1
        if pos == self.size: 
            item = self.last.item
            self.last = self.last.previous
            self.last.next_node = None
            return item, counter

        anterior = self.head
        atual = self.head.next_node
        contador = 0

        while atual:
            counter += 1
            if contador == pos:
                anterior.proximo = atual.proximo
                self.size -= 1
                return atual.item, counter
            anterior = atual
            atual = atual.proximo
            contador += 1

        return None