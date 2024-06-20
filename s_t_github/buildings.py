l1=[3,5,9,6,8,10]
l2=[3,0,0,0,0,0]
l3=[0,0,0,0,0,10]
for i in range(len(l1)-1):
    if l2[i]>l1[i+1]:
        l2[i+1]=l2[i]
    else:
        l2[i+1]=l1[i+1]
for i in range(len(l1)-1,-1,-1):
    if l3[i]>l1[i-1]:
        l3[i-1]=l3[i]
    else:
        l3[i-1]=l1[i-1]
print(len(set(l2)),len(set(l3)))
