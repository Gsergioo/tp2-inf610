from utils import  Item

class NodeDoubleLinked:
    
    def __init__(self, item) -> None:
        self.next_node = None
        self.previous = None
        self.item = item


class LinkedListV4:
    
    def __init__(self) -> None:
        self.head = NodeDoubleLinked(None)
        self.last = self.head
        self.size = 0

    def insert(self, x: Item, pos): 
        counter = 1
        node = NodeDoubleLinked(x)
        if pos == self.size:
            self.size += 1
            self.last.next_node = node
            self.last = self.last.next_node
            return counter

        pointer = self.head
        while pos - 1:
            counter += 1
            pointer = pointer.next_node
            pos -= 1

        next_node = pointer.next_node
        pointer.next_node = node
        node.next_node = next_node
        next_node.previous = pointer
        if pointer == self.last:
            self.last = node
        self.size += 1

        return counter

    def locate(self, pos):
        if not self.head:
            return -1
        
        node = self.head.next_node
        while pos:
            node = node.next_node
            if node == None:
                return None
            pos -= 1
        return node.item 

    def remove(self, pos):
        counter = 1
        if not self.head.next_node:
            print("A lista está vazia. Não é possível remover.")
            return counter
        if pos == self.size: 
            self.size -= 1
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
                self.size -= 1
                anterior.next_node = atual.next_node
                if pos == self.size:
                    self.last = anterior
                return atual.item, counter
            anterior = atual
            atual = atual.next_node
            contador += 1

        return counter
    

    def show(self):
        node = self.head.next_node
        while node != None:
            print(node.item.value)
            node = node.next_node