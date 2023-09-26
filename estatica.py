from tp2 import Item

class LinearStaticList:

    MAX = 1000

    def __init__(self) -> None:
        self.list = [None for i in range(self.MAX)]
        self.tamanho = 0

    def insert(self, x: Item, pos): 
        if self.tamanho == self.MAX:
            return "Não foi possivel inserir, cheia"
        if pos == self.tamanho:
            self.list[self.tamanho] = x
        else: 
            for i in range(self.tamanho, pos, -1):
                self.list[i] = self.list[i - 1]

        self.tamanho += 1
        self.list[pos] = x 

    def remove(self, pos):
        if pos == self.tamanho:
            self.tamanho -= 1
            return 0
        
        for i in range(pos, self.tamanho):
            self.list[i] = self.list[i + 1]
        
        self.tamanho -= 1
        return 0
    
    def locate(self, pos):
        return self.list[pos]

    def show(self):
        for i in range(0, self.tamanho):
            print(self.list[i].value)