graph=[[0,1,0,1,0,0,0],
       [1,0,1,1,0,1,1],
       [0,1,0,1,1,1,0],
       [1,1,1,0,1,0,0],
       [0,0,1,1,0,0,1],
       [0,1,1,0,0,0,0],
       [0,1,0,0,1,0,0]]

visited=[0,0,0,0,0,0,0]

vertex=0
visited[vertex]=1

l1=[]
queue=[]
queue.append(vertex)

while(len(queue)>0):
    print(queue,"queue")
    vertex=queue[0]
    k=queue.pop(0)
    print(queue,"queue atfer pop")
    l1.append(k)
    print(l1,"l1")
    for i in range(7):
        if(graph[k][i]==1 and visited[i]==0):
            queue.append(i)
            visited[i]=1
print(l1)