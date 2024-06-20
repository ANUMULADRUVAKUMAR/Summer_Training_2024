s="xyzabcde"
j=0
i=0
l1=[]
k=0
while(i<len(s)-1):
    j=i+1
    print(s[i],s[j],i,j)
    if(ord(s[i]) == ord(s[j])-1):
        i+=1
    else:
        l1.append(j-k)
        i=j
        k=i
        print(l1,k)
l1.append((j-k)+1)
print(max(l1))