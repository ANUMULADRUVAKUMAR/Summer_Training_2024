d={5:[[3,1],[1,2],[6,3]], 1:[[2,1],[5,2]], 2:[[1,1],[6,2]], 6:[[2,2],[3,3],[5,3]], 3:[[5,1],[6,3]]}

c={5:0, 1:9999, 2:9999, 3:9999, 6:9999}

l1=[]
v=[]
l1.append(5)

while(len(l1)>0):
    m=999
    for i in l1 :
        if(m>c[i]):
            m=c[i]
            x=i
    print(l1,x)
    for i in d[x]:
        if i[0] not in v:
            l1.append(i[0])
            if(c[i[0]] > c[x]+i[1]):
                c[i[0]]=c[x]+i[1]
    l1.remove(x)
    v.append(x)
    print(l1,v)
print(v)
print(d)
print(c)