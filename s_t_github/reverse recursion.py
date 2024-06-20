def reverse(n,l1):
    if(n%10===0):
        return l1
    l1.append(n%10)
    return reverse(n//10,l1)
print(reverse(123,[]))