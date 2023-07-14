class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def print_ll(self):
        if self.head is None:
            print("stuck empty")
        
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
                
LL1=Linkedlist()
LL1.print_ll()

         
    