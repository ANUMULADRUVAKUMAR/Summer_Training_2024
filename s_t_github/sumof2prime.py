def prime(n,i):
    if(i==n-1):
        return True
    if n%i==0:
        return False
    return prime(n,i+1)
n=12
a=n
l1=[]
n-=1
while(n>0):
    print(n)
    if prime(n,2):
        l1.append(n)
        print(l1)
    else:
        n-=1
        continue
    if(len(l1)>2):
        l1.pop(0)
    if(sum(l1)==a):
        print('ans',l1)
        break
    n-=1