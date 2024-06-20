s=input()
l1=list(map(eval,s.split(' ')))
e=0
o=0
d=0.0
for i in l1:
    if(i%1==0):
        if(i%2==0):
            e+=i
        elif(i%2==1):
            o+=i
    else:
        d+=i
print(e,o,d)