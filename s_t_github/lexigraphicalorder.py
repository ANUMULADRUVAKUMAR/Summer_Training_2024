l="polikumnhytgbvfredcxswqaz"
s="abcddb"
l1=[]
for i in s:
    l1.append(l.index(i))
l1.sort()
for i in l1:
    print(l[i],end="")