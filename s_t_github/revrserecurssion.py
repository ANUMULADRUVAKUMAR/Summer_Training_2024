def r(n,rev):
    if n==0:
        return rev
    rev=rev*10+(n%10)
    return r(n//10,rev)

print(r(123,0))