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
stack=[]
stack.append(vertex)
l1.append(vertex)

while(len(stack)>0):
    vertex=stack[len(stack)-1]
    for i in range(7):
        if(graph[vertex][i]==1 and visited[i]==0):
            stack.append(i)
            visited[i]=1
            l1.append(i)
            break
        if(i==6):
            k=stack.pop()
print(l1)