from utils import Item, Node

class LinkedListV1:
    
    def __init__(self) -> None:
        self.node = None

    def insert(self, x: Item, pos): 
        node = Node(x)
        if pos == 0 and self.node != None:   
            node.next_node = self.node
            self.node = node
            return 
        elif pos == 0:
            self.node = node
            return
        
        pointer = self.node
        while pos - 1:
            pointer = pointer.next_node
            pos -= 1
        
        next_node = pointer.next_node
        pointer.next_node = node
        node.next_node = next_node

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
        if not self.node:
            print("A lista está vazia. Não é possível remover.")
            return -1

        if pos == 0:
            node = self.node
            self.node = self.node.next_node
            return node

        anterior = None
        atual = self.node
        contador = 0

        while atual:
            if contador == pos:
                anterior.proximo = atual.proximo
                return atual
            anterior = atual
            atual = atual.proximo
            contador += 1

    def show(self):
        node = self.node
        while node != None:
            print(node.item.value)
            node = node.next_node