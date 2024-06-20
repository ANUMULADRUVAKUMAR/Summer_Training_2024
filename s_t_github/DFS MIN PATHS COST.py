def Traversing(d,l1,j,c,m,l2):
    l1.append(j)
    if(j==2):
        if(m>c):
            m=c
            l2=list(l1)
        l1.pop()
        return m,l2
    for i in d[j]:
        if i[0] not in l1:
            c+=i[1]
            m,l2=Traversing(d,l1,i[0],c,m,l2)
            c-=i[1]
    l1.pop()
    return m,l2

d={5:[[7,10],[3,30]], 7:[[5,10],[4,20],[3,50]], 4:[[7,20],[8,60],[2,70]], 2:[[4,70],[8,80]], 8:[[4,60],[2,80],[3,40]], 3:[[5,30],[7,50],[8,40]]}
print(Traversing(d,[],5,0,9999,[]))