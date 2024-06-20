
s = "aaabbcccd"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


z=""
k=0
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        k+=1
    else:
        z+=s[i]
        z+=str(k+1)
        k=0
z+=s[i+1]
z+=str(k+1)
print(z)
