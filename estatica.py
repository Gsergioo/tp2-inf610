from utils import Node, Item

class LinearStaticList:

    MAX = 10000

    def __init__(self) -> None:
        self.list = [None for i in range(self.MAX)]
        self.tamanho = 0

    def insert(self, x: Item, pos):
        counter = 1 
        if self.tamanho == self.MAX:
            return "Não foi possivel inserir, cheia"
        if pos == self.tamanho:
            self.list[self.tamanho] = x
            return counter
        else: 
            for i in range(self.tamanho, pos, -1):
                counter += 1
                self.list[i] = self.list[i - 1]

        self.tamanho += 1
        counter += 1
        self.list[pos] = x 

        return counter

    def remove(self, pos):
        counter = 1
        if pos == self.tamanho:
            self.tamanho -= 1
            return counter
        
        item = self.list[pos]
        for i in range(pos, self.tamanho):
            counter += 1
            self.list[i] = self.list[i + 1]
        
        self.tamanho -= 1
        return item, counter
    
    def locate(self, pos):
        return self.list[pos]

    def show(self):
        for i in range(0, self.tamanho):
            print(self.list[i].value)