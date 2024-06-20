class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insert(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            new_node=Node(value)
            current_node=self.head
            while(current_node.next):
                current_node=current_node.next
            current_node.next=new_node
            new_node.prev=current_node
    def insert_at_beg(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            new_node=Node(value)
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def insert_at_pos(self,value,pos):
        new_node=Node(value)
        current_node=self.head
        k=0
        while(current_node.next):
            k+=1
            if(k==pos-1):
                new_node.next=current_node.next
                current_node.next.prev=new_node
                current_node.next=new_node
                new_node.prev=current_node
            current_node=current_node.next
    def prints(self):
        current_node=self.head
        while(current_node.next):
            print(current_node.value)
            current_node=current_node.next
        print(current_node.value)
        while(current_node):
            print(current_node.value)
            current_node=current_node.prev
    def del_at_beg(self):
        self.head.next.prev=None
        self.head=self.head.next
    def del_at_end(self):
        current_node=self.head
        while(current_node.next.next):
            current_node=current_node.next
        current_node.next=None
    def del_at_pos(self,pos):
        current_node=self.head
        a=0
        while(current_node.next):
            a+=1
            if(a==pos-1):
                s=current_node.next.next
                current_node.next=s
                s.prev=current_node
            current_node=current_node.next
l=dll()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(50)
l.prints()
l.insert_at_beg(5)
print("after inserting at beg")
l.prints()
l.insert_at_pos(15,3)
print("after inserting at pos")
l.prints()
l.del_at_beg()
print("after del at beg")
l.prints()
l.del_at_end()
print("after del at end")
l.prints()
l.del_at_pos(2)
print("after del at end")
l.prints()