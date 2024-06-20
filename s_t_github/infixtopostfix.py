def push(l1,value):
    l1.append(value)
    return l1

l1=[]

precedence={"(":6, ")":6, "{":6, "}":6, "[":6, "]":6, "^":5, "*":4, "/":4, "+":3, "-":3}

s="K+L-M*N+(O^P)*W/U/V*T+Q"
s1=""
for i in s:
    if i.isnumeric() or i.isalpha():
        s1+=i
    else:
        print(i)
        
        if i=="(":
            push(l1,i)
            continue
        
        if i==")":
            while(l1[len(l1)-1]!="("):
                k=l1.pop()
                s1+=k
            l1.pop()
            continue
        
        if "(" in l1:
            push(l1,i)
            print(l1)
            continue
        
        if len(l1)==0:
            push(l1,i)
            continue
        
        if precedence[i]<precedence[l1[len(l1)-1]]:
            while(precedence[i]<precedence[l1[len(l1)-1]] and len(l1)>0):
               k=l1.pop()
               s1+=k
                
        if len(l1)==0:
            push(l1,i)
            continue
        
        if precedence[i]>precedence[l1[len(l1)-1]]:
            push(l1,i)
            continue
            
        if precedence[i]==precedence[l1[len(l1)-1]]:
            if precedence[i]== "*" or "/" or "+" or "-":
                k=l1.pop()
                s1+=k
                push(l1,i)
                continue
            else:
                push(l1,i)
                continue
for i in range(len(l1)-1,-1,-1):
    s1+=l1[i]
print(s1)
            