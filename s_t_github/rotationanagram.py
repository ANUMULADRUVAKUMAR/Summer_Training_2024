s="school"
l1=['l','r','l']
l2=[2,3,1]
d=""
for i in range(len(l1)):
    if l1[i]=='l':
        d+=s[l2[i]]
    else:
        d+=s[l2[-(i+1)]]
print(d)
d=sorted(d)
i=0
while(i<len(s)-2):
    print(d,sorted(s[i:i+3]))
    if d == sorted(s[i:i+3]):
        print('Yes')
    i+=1
print('No')
