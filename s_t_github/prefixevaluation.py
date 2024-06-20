s=list(input("Enter the postfix expression: ").split(" "))  
s=s[::-1]
l1=[]
for i in s:
    print(l1)
    if i.isnumeric():
        l1.append(int(i))
    else:
        a=l1.pop()
        b=l1.pop()
        if i=="+":
            l1.append(a+b)
        elif i=="-":
            l1.append(a-b)
        elif i=="*":
            l1.append(a*b)
        elif i=="/":
            l1.append(a/b)
        elif i=="^":
            l1.append(a^b)
print(l1)