def m(l1, l2, k, l3):
    f = 0
    for i in range(len(l1)):
        if i != k and l1[k][1] <= l1[i][0]:
            #print('value pre', l1[k], 'value loop', l1[i], i)
            f = 1
            h = k
            o = m(l1, l2, i, [])
            # print(o, l1[h], l2[h])
            l3.append(o + l2[h])
            # print(l3, 'o')
    if f == 0:
        return l2[k]
    else:
        print(l3, 'max return')
        return max(l3)

ma=0
l1 = [[1, 3], [2, 5], [4, 6], [6, 7], [5, 8], [7, 9]]
l2 = [5, 6, 5, 4, 11, 2]
for i in range(len(l1)):
    ma=max(m(l1,l2,i,[]),ma)
print(ma)