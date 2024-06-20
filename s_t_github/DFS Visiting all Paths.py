def visit(graph,l,j):
    l.append(j)
    print(j)
    for i in graph[j]:
        if i[0] not in l:
            visit(graph,l,i[0])
d={5:[[7,10],[3,30]], 7:[[5,10],[4,20],[3,50]], 4:[[7,20],[8,60],[2,70]], 2:[[4,70],[8,80]], 8:[[4,60],[2,80],[3,40]], 3:[[5,30],[7,50],[8,40]]}
print(visit(d,[],5))