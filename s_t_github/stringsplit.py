ip="hello:5438,car:214,book:8799,apple:2187"
ip=ip.split(',')
print(ip)
s=''
for i in ip:
    l1=i.split(':')
    j=len(l1[0])
    flag=0
    while((j-1)>=0):
        if str(j) in l1[1]:
            flag=1
            s+=l1[0][j-1]
            print(s,j,l1)
            break
        j-=1
    if (flag == 0):
        s += 'x'
print(s)