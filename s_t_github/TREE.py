class Node:
    def __init__(self,data):
        self.value=data
        self.right=None
        self.left=None
class tree:
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
        if root:
            self.inorder(root.left)
            print(root.value,end=' ')
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.value, end=' ')
            self.inorder(root.left)
            self.inorder(root.right)
    def postorder(self,root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.value, end=' ')
    def add(self, root):
        if root is None:
            return 0
        return root.value + self.add(root.left) + self.add(root.right)

    def even(self,root): #even odd difference
        if root is None:
            return 0
        if root.value%2==0:
            return root.value + self.even(root.left) + self.even(root.right)
        else:
            return self.even(root.left) + self.even(root.right) - root.value
    def height(self,root):
        if root is None:
            return -1
        z=self.height(root.left)
        y=self.height(root.right)
        return max(z,y)+1
    def bal(self,root):
        return abs(self.height(root.left) - self.height(root.right))<=1
    def leaf_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.leaf_nodes(root.left) + self.leaf_nodes(root.right)
    def sum_leaf_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.value
        return self.sum_leaf_nodes(root.left) + self.sum_leaf_nodes(root.right)

    def search(self,root,x):
        if(root is None):
            return False
        if(x==root.value):
            return True
        elif(x>root.value):
            return self.search(root.right,x)
        elif(x<root.value):
            return self.search(root.left,x)

    def depth(self,root,x,k):
        if(self.search(root,x)):
            if x==root.value:
                return k
            elif(x>root.value):
                return self.depth(root.right,x,k+1)
            elif(x<root.value):
                return self.depth(root.left,x,k+1)
        else:
            return 0
    def left_view(self,root,c,l1):
        if(root==None):
            return
        if(c not in l1):
            print(root.value,end=' ')
            l1.append(c)
        self.left_view(root.left,c+1,l1)
        self.left_view(root.right,c+1,l1)
    def top_view(self,root):
        d={}
        l1=[]
        c=0
        l1.append([root,root.value,c])
        while(len(l1)>0):
            k=l1.pop(0)
            if k[2] not in d:
                d[k[2]]=k[1]
            if k[0].left:
                l1.append([k[0].left,k[0].left.value,k[2]-1])
            if k[0].right:
                l1.append([k[0].right, k[0].right.value,k[2]+1])
        print(d)
        print(sorted(d.values()))

    def right_view(self,root,c,l1):
        if(root==None):
            return
        if(c not in l1):
            print(root.value,end=' ')
            l1.append(c)
        self.right_view(root.right, c + 1, l1)
        self.right_view(root.left,c+1,l1)

t=tree()
t.root=t.insert(t.root,10)
t.insert(t.root,5)
t.insert(t.root,20)
t.insert(t.root,2)
t.insert(t.root,7)
t.insert(t.root,11)
t.insert(t.root,8)
t.insert(t.root,9)
t.inorder(t.root)
'''print()
t.preorder(t.root)
print()
t.postorder(t.root)
print()
print(t.add(t.root))
print(t.even(t.root))
print(t.height(t.root))
print(t.bal(t.root))
print('leaf',t.leaf_nodes(t.root))
print(t.sum_leaf_nodes(t.root))
print(t.search(t.root,5))
print(t.depth(t.root,9,0))
#print(t.root.value)
print()
t.left_view(t.root,0,[])
print()
t.right_view(t.root,0,[])'''
print()
t.top_view(t.root)