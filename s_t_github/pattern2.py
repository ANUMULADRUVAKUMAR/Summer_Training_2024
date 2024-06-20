n=10
for i in range(n):
    d = ""
    o=97
    z=0
    for j in range(n-i):
        d+='_'
        print('_', end="")
    while(z<i+1):
        d+=(chr(o))
        print(chr(o),end='')
        o+=1
        z+=1
    e=d[:-1]
    print(e[::-1],end="")
    print()