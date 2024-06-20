a=int(input())
b=int(input())
while(b):
    a,b=b,a%b
if(a==1):
    print('coprime')
else:
    print('not coprime')