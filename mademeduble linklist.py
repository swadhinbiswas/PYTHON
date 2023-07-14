class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Double_link_list:
    def __init__(self):
        self.head = None
    def forword_traversal(self):
        if self.head == None:
            return None
        else:
            forword = self.head
            while forword != None:
                print(forword.data, end="=>")
                forword = forword.next
    def backword_traversal(self):
        if self.head == None:
            return None
        else:
            a = self.head
            while a.next is not None:
                a = a.next
            while a is not None:
                print(a.data, end="=>")
                a = a.prev
    