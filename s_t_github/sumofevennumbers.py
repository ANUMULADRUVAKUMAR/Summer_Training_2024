def even_odd(a,b,x,s,e):
    if(x==len(a)):
        return (s,e)
    if(a[x]%2==0):
        s+=a[x]
    if(b[x]%2!=0):
        e+=b[x]
    return even_odd(a,b,x+1,s,e)



a=[3,8,5,4,3]
b=[5,0,9,3,2]
print(even_odd(a,b,0,0,0))