'''def palin(n):
    if(str(n)==str(n)[::-1]):
        return n
    else:
        return palin(n+1)
n=3611
print(palin(n))'''

def palin(n):
    s=''
    if(len(n)%2==0):
        k=len(n)//2
        if int(n[:k]) > int(n[k:]):
            s+=n[:k]
            s+=s[::-1]
        else:
            s=s+str(int(n[:k])+1)
            s += s[::-1]
    else:
        k = len(n) // 2
        if int(n[:k]) > int(n[k+1:]):
            s += n[:k+1]
            s += n[:k][::-1]
        else:
            s=s+n[:k]
            s=s+str(int(n[k])+1)
            s += n[:k][::-1]

    print(s)
palin(str("12345"))