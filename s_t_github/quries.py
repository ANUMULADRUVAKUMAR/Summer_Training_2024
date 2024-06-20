n = int(input())
l1 = []
for j in range(n):
    z = input()
    if z[0] == '1':
        if z[2:] not in l1:
            l1.append(z[2:])
    elif z[0] == '2':
        if z[2:] in l1:
            print(True)
        else:
            print(False)
    elif z[0] == '3':
        o = 0
        for i in l1:
            k = len(z[2:])
            if len(i) >= k:
                if z[2:] == i[:k]:
                    o += 1
        else:
            print(o)
    elif z[0] == '4':
        if z[2:] in l1:
            l1.remove(z[2:])
            print(l1)
        else:
            print('False')
