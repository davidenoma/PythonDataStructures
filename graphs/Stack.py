class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
         return self.items == []
    def len(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.isEmpty():
            raise Exception("Your stack is empty")
        return self.items.pop()
    def top(self):
        if self.isEmpty():
            raise Exception("Your stack is empty")
        return self.items[-1]
    

