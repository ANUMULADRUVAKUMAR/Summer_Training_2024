def paths(i,j,l1,l2):
    if [i,j] in l2:
        return l1
    l2.append([i,j])
    if i==3 and j==7:
        print(l2)
        l2.pop()
        l1.append(1)
        return l1
    if i<3:
        l1=paths(i+1,j,l1,l2)
    if j<7:
        l1=paths(i,j+1,l1,l2)
    if i>0:
        l1=paths(i-1,j,l1,l2)
    if j>0:
        l1=paths(i,j-1,l1,l2)
    #print(l1)
    l2.pop()
    return l1
print(len(paths(0,0,[],[])))