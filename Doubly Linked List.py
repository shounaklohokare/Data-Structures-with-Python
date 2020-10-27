class Node(object):

    def __init__(self, value):
        self.value=value
        self.nextnode = None
        self.previousnode = None

    
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode=b
b.previousnode = a
b.nextnode=c
c.previousnode=b
c.nextnode=d
d.previousnode=c

