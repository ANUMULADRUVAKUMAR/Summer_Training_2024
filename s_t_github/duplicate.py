l1=[2,3,1,3,4,3,2]
i=0
l2=[]
l3=[]
l4=[]
k=0
j=0
while(i<len(l1)):
    if i not in l4:
        if l1[i] not in l2:
            l2.append(l1[i])
            l4.append(i)
        elif l1[i] in l2 and k==0:
            j=i
            k=1
        if(i==len(l1)-1):
            l3.append(l2)
            l2=[]
            i=j-1
            k=0
    i+=1
if len(l2)>0:
    l3.append(l2)
print(l3)
