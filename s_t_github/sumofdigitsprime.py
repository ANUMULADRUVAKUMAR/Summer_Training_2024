n=9
k=n
z=True
while(z):
    n=k
    print(n,'number')
    while(n%10!=n):
        d=0
        for i in str(n):
            d+=int(i)

        n=d
        print(n,'sum')
    if n in [1,2,3,5,7]:
        print(k)
        z=False
    else:
        k+=1




