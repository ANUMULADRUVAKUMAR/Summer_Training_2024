class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def addbeg(self,data):
        current=node(data)
        current.next=self.head
        self.head=current
    def addback(self,data):
        if self.head is None:
            self.head=node(data)
        else:
            current_node=self.head
            while(current_node.next):
                current_node=current_node.next
            current_node.next=node(data)
    def printf(self):
        current_node=self.head
        while(current_node):
            print(current_node.data,end="->")
            current_node=current_node.next
        print()
    def linear_search(self,data):
        current_node = self.head
        while(current_node):
            if(current_node.data==data):
                return "Found"
            current_node=current_node.next
        return "NotFound"
    def middle(self):
        fast = self.head
        slow= self.head
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
        print(slow.data)
    def even_odd(self):
        fast=self.head
        slow=self.head
        k=0
        while(True):
            fast=fast.next.next
            slow=slow.next
            k+=1
            if(fast==None):
                return 'even'
            elif(fast.next==None):
                return 'odd'
    def balanced_parenthesis(self):
        d={')':'(','}':'{',']':'['}
        l1=[]
        current=self.head
        k=0
        while(current):
            if(current.data not in d):
                k+=1
                l1.append(current.data)
                current=current.next
            else:
                if d[current.data]==l1[len(l1)-1]:
                    k+=1
                    l1.pop()
                else:
                    return k+1
                current=current.next
        if(len(l1)==0):
            return -1
        else:
            return k
l1=sll()
l1.addback('[')
l1.addback('{')
l1.addback('(')
l1.addback(']')
l1.addback(']')
l1.addback(')')
l1.printf()
'''
print()
print(l1.linear_search(30))
l1.middle()
print(l1.even_odd())
'''
print(l1.balanced_parenthesis())