class Deque(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        self.items == []
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        self.items.pop()
    def removeRear(self):
        self.items.pop(0)
    def size(self):
        return len(self.items)
    
d = Deque()
d.addFront("hello")
d.addRear("world")
d.addFront("You")
