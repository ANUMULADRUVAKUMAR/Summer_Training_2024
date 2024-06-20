def island(a,i,j,c):
    if (i<0 or j<0 or j>len(a)-1 or i>len(a)-1 or a[i][j]!=1):
        return c
    if a[i][j]==1:
        c += 1
        a[i][j]=2
    c=island(a,i-1,j,c)
    c=island(a,i+1,j,c)
    c=island(a,i,j+1,c)
    c=island(a,i,j-1,c)
    return c

c=0
m=0
a=[[0,1,0,0,1], [1,0,0,1,1], [0,0,0,0,0], [1,0,0,0,0], [1,0,0,0,1]]
for i in range(len(a)):
    for j in range(len(a)):
        if(a[i][j]==1):
            c+=1
            k=island(a,i,j,0)
            if(m<k):
                m=k

print(a)
print(c,m)
