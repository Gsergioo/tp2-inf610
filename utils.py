class Item:

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

class Node:

    def __init__(self, x: Item) -> None:
        self.item = x
        self.next_node = None