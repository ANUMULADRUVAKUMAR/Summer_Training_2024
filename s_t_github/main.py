x=[1,5,8,9]
y=[2, 7, 9, 10, 14]
c=[]
i=0
j=0
while(i<len(x) and j<len(y)):
    if(x[i]<y[j]):
        c.append(x[i])
        i+=1
    else:
        c.append(y[j])
        j+=1
    if(i==len(x)-1):
        c.extend(y[j:])
        break
    if (i == len(y) - 1):
        c.extend(x[i:])
        break
print(c)
