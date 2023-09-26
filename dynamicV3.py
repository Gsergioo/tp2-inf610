from tp2 import Node, Item

class LinkedListV3:
    
    def __init__(self) -> None:
        self.head = Node(None)
        self.last = None
        self.size = 0

    def insert(self, x: Item, pos): 
        node = Node(x)
        if pos == self.size:
            self.last.next_node = node
            self.last = self.last.next_node

        pointer = self.head.next_node
        while pos - 1:
            pointer = pointer.next_node
            pos -= 1

        next_node = pointer.next_node
        pointer.next_node = node
        node.next_node = next_node
        if pointer == self.last:
            self.last = node
        self.size += 1

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
        if not self.node:
            print("A lista está vazia. Não é possível remover.")
            return -1

        anterior = self.head
        atual = self.head.next_node
        contador = 0

        while atual:
            if contador == pos:
                anterior.proximo = atual.proximo
                return atual
            anterior = atual
            atual = atual.proximo
            contador += 1

        return None