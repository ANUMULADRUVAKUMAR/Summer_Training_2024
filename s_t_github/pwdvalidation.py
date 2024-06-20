p=input()
d=8-len(p)
l1=[0,0,0,0]
for i in p:
    if(i.islower()):
        l1[0]=1
    if(i.isupper()):
        l1[1]=1
    if(i.isnumeric()):
        l1[2]=1
    if(not i.isalnum()):
        l1[3]=1
print(l1)
z=4-sum(l1)
if(d>0):
    if(d>z):
        print(d)
    else:
        if(len(p)+z<8):
            print(z+(8-(len(p)+z)))
        else:
            print(z)
else:
    print(z)

