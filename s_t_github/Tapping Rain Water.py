l1=[4,3,4,5,6,1,0,6,7]
s=0
for i in range(1,len(l1)-1):
    o=min(max(l1[:i]), max(l1[i+1:]))
    print(l1[i],o,o-l1[i])
    if(o-l1[i]>0):
        s=s+(o-l1[i])
print(s)