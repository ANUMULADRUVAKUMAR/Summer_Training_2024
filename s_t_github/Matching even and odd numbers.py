def match(l1,l2,i,j,l3,k):
    if(i==len(l1)-1 and k):
        return
    if(j==len(l1)-1):
        return
    if(k):
        i+=1
        match(l1,l1,i,j,l3,True)
    if(l1[i]%2!=0):
        j+=1
        match(l1,l2,i,j,l3,False)
        if(l2[j]%2==0):
            l3.append(l1[i]+l2[j])
    return l3

print(match([3,2,4,5,6,7], [1,2,3,4,5,6], -1,-1,[],True))