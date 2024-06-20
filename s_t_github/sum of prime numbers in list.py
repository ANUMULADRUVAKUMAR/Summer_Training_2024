def prime(n,i):
    if(i==n//2):
        return True
    if n%i==0:
        return False
    return prime(n,i+1)

l2=[]
l1=[14,16,20,22]
for i in range(len(l1)-1):
    for i in range(l1[i+1]-1,l1[i]-1,-1):
        if prime(i,2)==True:
            l2.append(i)
            break
print(l2)