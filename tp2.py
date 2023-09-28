import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns


from estatica import LinearStaticList
from dynamicV1 import LinkedListV1
from dynamicV2 import LinkedListV2
from dynamicV3 import LinkedListV3
from dynamicV4 import LinkedListV4
from utils import Item


class Fila: 

    def __init__(self, type) -> None:
        self.items = self._get_data_structure(type)
        self.size = 0

    def _get_data_structure(self, type):   
        tads = {
            "LinearStatic": LinearStaticList(),
            "DynamicV1": LinkedListV1(),
            "DynamicV2": LinkedListV2(),
            "DynamicV3": LinkedListV3(),
            "DynamicV4": LinkedListV4()
        }
        return tads[type]
    
    def queue(self, x: Item):
        counter = self.items.insert(x, self.size)
        self.size += 1
        return counter

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
        counter = 0
        for i in range(self.queue.size):
            if self.queue.get_first().key == key:
                return self.queue.get_first(), counter
            else:
                item, counter_aux = self.queue.dequeue()
                counter += counter_aux
                counter_aux = self.queue.queue(item)
                counter += counter_aux

        return None, counter
    
    def insert(self, item):
        self.queue.queue(item)
        self.size += 1

if __name__ == "__main__":
    vv = []
    for i in range(10, 1000, 100):
        print(i)
        keys = np.random.choice(range(i), i, replace=False)
        values = np.random.choice(range(i), i, replace=False)
        items = [Item(item[0], item[1]) for item in zip(keys, values)]

        v = []
        for list_type in ["LinearStatic", "DynamicV1", "DynamicV2", "DynamicV3", "DynamicV4"]:
            dicionario = Dicionario(list_type)
            for item in items:
                dicionario.insert(item)

            a, counter = dicionario.search(keys[-1]) 
            v.append(counter) 
        vv.append(v)    

    x = [x for x in range(10, 1000, 100)]

    for i in range(5):
        y = [a[i] for a in vv]
        print("AAA")
        print(len(x))
        print(len(y))
        sns.lineplot(x=x, y=y)

    plt.show()

     