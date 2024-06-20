s='tu5g2k1h8g5g8gd6h3'
s=set(s)
s1=''
m=99
for i in s:
    if i.isdigit():
        if(int(i)%2==0):
            if m>int(i):
                m=int(i)
        s1+=i
if m==99:
    print(int(''.join(sorted(s1)[::-1]))+1)
else:
    s1=s1.replace(str(m),'')
    print(''.join(sorted(s1)[::-1])+str(m))