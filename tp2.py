import numpy as np

from estatica import LinearStaticList
from dynamicV1 import LinkedListV1
from dynamicV2 import LinkedListV2
from dynamicV3 import LinkedListV3


class Item:

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

class Node:

    def __init__(self, x: Item) -> None:
        self.item = x
        self.next_node = None

class Fila: 

    def __init__(self, type) -> None:
        self.items = self._get_data_structure(type)
        self.size = 0

    def _get_data_structure(self, type):   
        tads = {
            "LinearStatic": LinearStaticList(),
            "DynamicV1": LinkedListV1(),
            "DynamicV2": LinkedListV2(),
            "DynamicV3": LinkedListV3()
        }
        return tads[type]
    
    def queue(self, x: Item):
        self.items.insert(x, self.size)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.items.remove(0)

    
    def get_first(self):
        return self.items.locate(0)

class Dicionario():

    def __init__(self, type) -> None:
        self.queue = Fila(type)
        self.size = 0
    
    def search(self, key):
        for i in range(self.queue.size):
            if self.queue.get_first().key == key:
                return self.queue.get_first()
            else:
                item = self.queue.dequeue()
                self.queue.queue(item)
        
        return None
    
    def insert(self, item):
        self.queue.queue(item)
        self.size += 1
        


if __name__ == "__main__":
    dicionario = Dicionario("DynamicV1")
    keys = np.random.choice(range(10000), 10000, replace=False)
    values = np.random.choice(range(10000), 10000, replace=False)
    items = [Item(item[0], item[1]) for item in zip(keys, values)]
    
    for item in items:
        dicionario.insert(item)

    a = dicionario.search(10) 
    print(a)
