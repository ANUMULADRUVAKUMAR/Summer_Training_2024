c=[1,3,5]
n=6
l2=[]
for i in range(len(c)+1):
    l1=[]
    for j in range(n+1):
        l1.append(j)
    l2.append(l1)
print(l2)

current=1
for i in range(len(c)):
    for j in range(len(l2[0])):
        if i==0:
            if l2[0][j] == 0:
                l2[i+1][j]=1
            if l2[0][j] == c[i]:
                l2[i+1][j]=1
            else:
                l2[i + 1][j] = 0
        else:
            s=l2[0][j]-c[i]
            if(s==0):
                l2[i+1][j]=1
            elif s>0:
                if l2[current][s]!=0:
                    l2[i+1][j]=l2[current][s]+1
                else:
                    l2[i+1][j]=l2[i][j]
            else:
                l2[i + 1][j] = l2[i][j]
    current=i+1


for i in range(len(c)+1):
    for j in range(n+1):
        print(l2[i][j],end=' ')
    print()