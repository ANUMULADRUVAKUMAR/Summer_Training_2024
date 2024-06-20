class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert(self,value):
        if self.head==None:
            self.head=Node(value)
            self.head.next=self.head
        else:
            new_node=Node(value)
            current_node=self.head
            while(current_node.next!=self.head):
                current_node=current_node.next
            current_node.next=new_node
            new_node.next=self.head
    def insert_at_beg(self,value):
        if self.head==None:
            self.head=Node(value)
            self.head.next=self.head
        else:
            current_node=self.head
            while(current_node.next!=self.head):
                current_node=current_node.next
            new_node=Node(value)
            new_node.next=self.head
            self.head=new_node
            current_node.next=self.head
    def prints(self):
        if self.head==None:
            print("NO ELements")
        else:
            current_node=self.head
            while(current_node.next!=self.head):
                print(current_node.value)
                current_node=current_node.next
            print(current_node.value)
    def del_at_beg(self):
        current_node=self.head
        while(current_node.next!=self.head):
            current_node=current_node.next
        self.head=self.head.next
        current_node.next=self.head
    def del_at_end(self):
        current_node=self.head
        while(current_node.next.next!=self.head):
            current_node=current_node.next
        current_node.next=self.head
l=sll()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(50)
l.prints()
l.insert_at_beg(5)
print("after inserting at beg")
l.prints()
l.del_at_beg()
print("after del at beg")
l.prints()
l.del_at_end()
print("after del at end")
l.prints()