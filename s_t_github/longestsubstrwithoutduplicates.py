ip="abfgresagtyuiofde"
i=0
d=""
dic={}
l1=[]
while(i<len(ip)):
    if(ip[i] not in d):
        d+=ip[i]
        dic[ip[i]]=i
    else:
        l1.append(len(d))
        d=""
        i=dic[ip[i]]
    i+=1
print(max(l1))