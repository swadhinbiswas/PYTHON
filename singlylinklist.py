#creat class
class Node :
    def __init__(self,data):
        self.data=data
        self.ref=None
        

#creat Link_list

class Link_list:
     def __init__(self):
         self.head=None
#traversal
     def traversal(self):
         if self.head == None:
             print("emty")
         else:
             value=self.head
             while value != None:
                 print(value.data,end="=>")
                 value=value.ref
    #insertion Node Beginaing
     def insert_begin(self,data):
         begin=Node(data)
         begin.ref=self.head
         self.head=begin
       #insert last  
         
     def insert_last(self,data):
         last=Node(data)
         temp=self.head
         while temp.ref != None:
             temp=temp.ref
         temp.ref=last
     #insert specif
     def insert_any(self,position,data):
         any=Node(data)
         anywhere=self.head
         for i in range(1,position-1):
             anywhere=anywhere.ref
         any.ref=anywhere.ref
         anywhere.ref=any
     #delete from begining
     def delete_beginning(self):
         begin=self.head
         self.head=begin.ref
         begin.ref=None
    
    #delete from last
     def delete_last(self):
         temp=self.head
         delete=self.head.ref
         while delete.ref != None:
             delete=delete.ref
             temp=temp.ref
         temp.ref=None
    #delete from any where
     def delete_anywhere(self,position):
         temp=self.head
         delete=self.head.ref
         for i in range(1,position-1):
             delete=delete.ref
             temp=temp.ref
         temp.ref=delete.ref
         delete.ref=None
        
#test Node
n1=Node(5)
Link=Link_list()
Link.head=n1
n2=Node(10)
n1.ref=n2

Link.traversal()
print("\n")

Link.insert_begin(2)

Link.traversal()
Link.insert_last(11)
print("\n")
Link.traversal()
print("\n")
Link.insert_any(4,5)
Link.traversal()
Link.delete_beginning()
print("\n")
Link.traversal()
print("\n")
Link.delete_last()
Link.traversal()
print("\n")
Link.delete_anywhere(2)
Link.traversal()
