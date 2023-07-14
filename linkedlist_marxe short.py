class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class doubly_linked_list:
   def __init__(self):
      self.head = None
   
# Adding data elements		
   def push(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = self.head
      push=self.head
      if push is not None:
         push.prev = NewNode
      self.head = NewNode

# Print the Doubly Linked list		
   def listprint(self, node):
      while (node is not None):
         print(node.data),
         last = node
         node = node.next

def marge_short(doubly_linked_list):
    if doubly_linked_list.size()==1:
        return doubly_linked_list
    elif doubly_linked_list.head==None:
        return doubly_linked_list
    left,right=split(doubly_linked_list)
    left=marge_short(left)
    right=marge_short(right)
    return marge(left,right)

def split(doubly_linked_list):
    if doubly_linked_list==None or doubly_linked_list.head==None:
        left=doubly_linked_list
        right=None
        return left,right
    else:
        size=doubly_linked_list.size()
        mid