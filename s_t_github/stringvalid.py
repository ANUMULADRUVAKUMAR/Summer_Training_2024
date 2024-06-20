x=int(input())
l1=[]
for i in range(3):
    y=list(input())
    l1.append(y)
s=input()

flag=1
print(l1)
i=0
j=0

while(i<len(s)):
    print(s[i],l1[j],j)
    if(s[i] in l1[j]):
        l1[j].remove(s[i])
        i+=1
        j+=1
    else:
        print('NO')
        flag=0
        break
    if(j==len(l1)):
        j=0
if(flag==1):
    print('yes')