graph=[[999,4,999,999,999,999,999,8,999],
       [4,999,8,999,999,999,999,11,999],
       [999,8,999,7,999,8,999,999,2],
       [999,999,7,999,9,14,999,999,999],
       [999,999,999,9,999,10,999,999,999],
       [999,999,8,14,10,999,2,999,999],
       [999,999,999,999,999,2,999,1,6],
       [8,11,999,999,999,999,1,999,7],
       [999,999,2,999,999,999,6,7,999]]

m=graph[0][0]

for i in range(9):
    for j in range(9):
        if m>graph[i][j]:
            m=graph[i][j]
            a=i
            b=j

visited=[0,0,0,0,0,0,0,0,0]
l1=[]
l2=[]
l2.append([a,b,m])
l1.append(a)
l1.append(b)
visited[a]=1
visited[b]=1



while(len(l1)!=9):
    m=9999
    for i in l1:
        for j in range(9):
            if graph[i][j]!=999 and visited[j]==0:
                if m>graph[i][j]:
                    m=graph[i][j]
                    a=i
                    b=j
    l2.append([a,b,m])
    print(l2,"l2")
    l1.append(b)
    print(l1,"l1")
    visited[b]=1
    print(visited,"visited")
print(l2)
print(l1)
        