class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
        
#creat Double link list
class Double_Link_list:
    def __init__(self):
        self.head=None
    
    #forword traversal
    def forword_tarversal(self):
        if self.head==None:
            return None
        else:
            forword=self.head
            while forword !=None:
                print(forword.data,end="=>")
                forword=forword.next
    #bsckword traversal
    def back_traversal(self):
        if self.head==None:
            return None
        else:
            a=self.head
            while a.next is not None:
                a=a.next
                while a is not None:
                    print(a.data,end="=>")
                    a=a.prev
    #insertion at begining
    #def insert_at_begining(self,data):
    #test Node
n1=Node(5)
Link=Double_Link_list()
Link.head=n1
n2=Node(10)
n2.prev=n1
n1.next=n2
Link.forword_tarversal()
print()
Link.back_traversal()

        