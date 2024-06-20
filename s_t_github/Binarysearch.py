class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,value):
        if root is None:
            return Node(value)
        if value>root.value:
            root.right=self.insert(root.right,value)
        elif value<=root.value:
            root.left=self.insert(root.left,value)
        return root
    def inorder(self,root):
        if root.left:
            self.inorder(root.left)
        print(root.value)
        if root.right:
            self.inorder(root.right)
    def delete(self,root,d):
        if root is None:
            return root
        if d>root.value:
            root.right=self.delete(root.right,d)
        elif d<root.value:
            root.left=self.delete(root.left,d)
        else:
            if root.left==None:
                return root.right
            if root.right==None:
                return root.left
            root.value=self.minm(root.right)
            root.right=self.delete(root.right,root.value)
        return root
    def minm(self,root):
        m=root.value
        while(root.left):
            m=root.left.value
            root=root.left
        return m
  
tree=BST()
tree.root=tree.insert(tree.root,11)
tree.insert(tree.root,6)
tree.insert(tree.root,8)
tree.insert(tree.root,19)
tree.insert(tree.root,4)
tree.insert(tree.root,10)
tree.insert(tree.root,5)
tree.insert(tree.root,17)
tree.insert(tree.root,43)
tree.insert(tree.root,49)
tree.insert(tree.root,31)
tree.inorder(tree.root)
tree.delete(tree.root,31)
print("after deletion")
tree.inorder(tree.root)