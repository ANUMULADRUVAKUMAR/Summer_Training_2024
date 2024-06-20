class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=1
class AVL:
    def __init__(self):
        self.root=None
    
    def height(self,node):
        if node is None:
            return 0
        return node.height
    
    def balance(self,node):
        if node is None:
            return 0
        return self.height(node.left)-self.height(node.right)
    
    def insert(self,root,value):
        if root is None:
            return Node(value)
        if value>root.value:
            root.right=self.insert(root.right,value)
        else:
            root.left=self.insert(root.left,value)
            
        root.height=1+max(self.height(root.right), self.height(root.left))
        balance=self.balance(root)
        
        if balance>1 and value<root.left.value:
            return self.rightrotation(root)
        elif balance<-1 and value>root.right.value:
            return self.leftrotation(root)
        elif balance>1 and value>root.left.value:
            root.left=self.leftrotation(root.left)
            return self.rightrotation(root)
        elif balance<-1 and value<root.right.value:
            root.right=self.rightrotation(root.right)
            return self.leftrotation(root)
        return root
        
    def leftrotation(self,z):
        y=z.right
        t3=y.left
        
        y.left=z
        z.right=t3
        
        z.height=1+max(self.height(z.right),self.height(z.left))
        y.height=1+max(self.height(y.right),self.height(y.left))
        
        return y
    def rightrotation(self,z):
        y=z.left
        t2=y.right
        
        y.right=z
        z.left=t2
        
        z.height=1+max(self.height(z.right),self.height(z.left))
        y.height=1+max(self.height(y.right),self.height(y.left))
        
        return y
    def deletion(self,root,value):
        if root is None:
            return None
        if value>root.value:
            root.right=self.deletion(root.right,value)
        elif value<root.value:
            root.left=self.deletion(root.left,value)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            root.value=self.minv(root.right)
            root.right=self.deletion(root.right,root.value)
            
        root.height=1+max(self.height(root.right), self.height(root.left))
        balance=self.balance(root)
        
        if balance>1 and value<root.left.value:
            return self.rightrotation(root)
        elif balance<-1 and value>root.right.value:
            return self.leftrotation(root)
        elif balance>1 and value>root.left.value:
            root.left=self.leftrotation(root.left)
            return self.rightrotation(root)
        elif balance<-1 and value<root.right.value:
            root.right=self.rightrotation(root.right)
            return self.leftrotation(root)
        return root
    def minv(selef,root):
        m=root.value
        while(root.left):
            m=root.left.value
            root=root.left
        return m
        
    def inorder(self,root):
        if root.left:
            self.inorder(root.left)
        print(root.value)
        if root.right:
            self.inorder(root.right)
    def insert_value(self, value):
        self.root = self.insert(self.root, value)
    def delete_value(self, d):
        self.root = self.deletion(self.root, d)
tree=AVL()
tree.insert_value(14)
tree.insert_value(17)
tree.insert_value(11)
tree.insert_value(7)
tree.insert_value(53)
tree.insert_value(4)
tree.insert_value(13)
tree.insert_value(12)
tree.insert_value(8)
tree.insert_value(60)
tree.insert_value(19)
tree.insert_value(16)
tree.insert_value(20)
tree.inorder(tree.root)
print("after deletion")
tree.delete_value(8)
tree.inorder(tree.root)
print("after deletion")
tree.delete_value(7)
tree.inorder(tree.root)
print("after deletion")
tree.delete_value(11)
tree.inorder(tree.root)
print("after deletion")
tree.delete_value(14)
tree.inorder(tree.root)
print("after deletion")
tree.delete_value(17)
tree.inorder(tree.root)