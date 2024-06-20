def burning(a,i,j):
    if (i<0 or j<0 or j>len(a)-1 or i>len(a)-1):
        return
    if(a[i][j]!=1):
        return
    if a[i][j]==1:
        a[i][j]=2
    burning(a,i-1,j)
    burning(a,i+1,j)
    burning(a,i,j+1)
    burning(a,i,j-1)
    return a

a=burning([[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]],3,5)
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j],end=' ')
    print()



