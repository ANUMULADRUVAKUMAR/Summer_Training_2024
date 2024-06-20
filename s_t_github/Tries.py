class Node:
    def __init__(self):
        self.d={}
        self.flag=0

class tries:
    def __init__(self):
        self.root=Node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=Node()
            t = t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        if t.flag==1:
            return True
        else:
            return False

    def prefix(self,str):
        l1=[]
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    def printpref(self,s):
        def fun(t,s1):
            if t.flag==1:
                print(s1)
                return
            for i in t.d:
                fun(t.d[i],s1+i)
        t = self.root
        s1=''
        for i in s:
            if i in t.d:
                s1=s1+i
                t = t.d[i]
            else:
                return s1
        fun(t,s1)


t1=tries()
t1.insert('world')
t1.insert('word')
t1.insert('wood')
t1.insert('apple')
t1.insert('woo')
print(t1.search('word'))
t1.printpref('wor')
