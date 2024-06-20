def split(l1):
    if len(l1)==0:
        return 0
    if len(l1)==1:
        return l1[0]
    if len(l1)==2:
        return max(l1)
    le=l1[0]+split(l1[2:])
    re=l1[1]+split(l1[3:])
    return max(le,re)
print(split([13,9,4,10,5,7]))

'''
l1=[13,9,4,10,5,7]
l2=[]
for i in range(len(l1)):
    m=0
    s = l1[i]
    j=i+2
    while(j<len(l1)):
        print(l1[j],s,m)
        if(m<s+l1[j]):
            m=s+l1[j]
            m1=l1[j]
            index=j
        if(j==len(l1)-1):
            s+=m1
            print(j,'j',index+2,'index',s,'s')
            j=index+1
            m=0
            print('j',j)
        j += 1
    l2.append(s)
print(l2)
print(max(l2))
'''
