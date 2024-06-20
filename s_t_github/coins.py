c=[1,3,4,5]
n=17
l2=[]
for i in range(len(c)+1):
    l1=[]
    for j in range(n+1):
        l1.append(j)
    l2.append(l1)

print(l2)
for i in range(len(c)):
    for j in range(len(l2[0])):
        if c[i]>l2[0][j]:
            l2[i+1][j]=l2[i][j]
        else:
            k=l2[0][j]-c[i]
            l2[i+1][j]=l2[i+1][k]+1
for i in range(len(c)+1):
    for j in range(n+1):
        print(l2[i][j],end=' ')
    print()

print(l2[len(c)][n])