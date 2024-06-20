def add(x):
    if(x==0):
        return 0
    return x+add(x-2)

n=int(input())
if(n%2==0):
    print(add(n))
else:
    print(add(n-1))