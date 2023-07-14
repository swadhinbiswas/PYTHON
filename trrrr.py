class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.previous = None
        
class Double_Link_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
         
    def __repr__(self):
        string = ""
         
        if(self.head == None):
            string += "Doubly Linked List Empty"
            return string
         
        string += f"Doubly Linked List:\n{self.head.data}"       
        start = self.head.next
        while(start != None):
            string += f" -> {start.data}"
            start = start.next
        return string
         
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.count += 1
            return
         
        self.tail.next = Node(data)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        self.count += 1
         
    def insert(self, data, index):
        if (index > self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
             
        if(index == self.count):
            self.append(data)
            return
             
        if(index == 0):
            self.head.previous = Node(data)
            self.head.previous.next = self.head
            self.head = self.head.previous
            self.count += 1
            return
         
        start = self.head
        for _ in range(index):
            start = start.next
        start.previous.next = Node(data)
        start.previous.next.previous = start.previous
        start.previous.next.next = start
        start.previous = start.previous.next
        self.count += 1
        return
     
    def remove(self, index):
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
         
        if index == 0:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
            return
             
        if index == (self.count - 1):
            self.tail = self.tail.previous
            self.tail.next = None
            self.count -= 1
            return
         
        start = self.head
        for i in range(index):
            start = start.next
        start.previous.next, start.next.previous = start.next, start.previous
        self.count -= 1
        return
     
    def index(self, data):
        start = self.head
        for i in range(self.count):
            if(start.data == data):
                return i
            start = start.next
        return None
     
    def size(self):
        return self.count
     
    def display(self):
        print(self)
        
        
d = Double_Link_list()
d.append(1)
d.append(3)
d.display()
d.insert(2, 1)
d.display()
