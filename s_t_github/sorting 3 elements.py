l1=[4,9,8,2,14,3,5,6]
l2=[]
i=0
while(i<len(l1)-2):
    if(l1[i]>l1[i+1]):
        l1[i], l1[i+1]=l1[i+1], l1[i]
    if(l1[i+1]>l1[i+2]):
        l1[i+1], l1[i+2]=l1[i+2], l1[i+1]
    if(l1[i]>l1[i+1]):
        l1[i], l1[i+1]=l1[i+1], l1[i]
    i+=1
print(l1)