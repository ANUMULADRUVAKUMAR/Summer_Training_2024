s="abcd"
l1=[[]]
for i in s:
    for j in l1:
        l1=l1+[j+[i]]
print(l1)