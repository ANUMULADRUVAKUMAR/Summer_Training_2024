def Three_pairs(l, i, j, k):
    if i == len(l) - 2:
        return
    # for k in range(j + 1, len(l)):
    #     print(l[i], l[j], l[k])
    if k == len(l) :
        i += 1
        j = i + 1
        k = j + 1
        return Three_pairs(l, i, j, k)
    print(l[i], l[j], l[k])
    Three_pairs(l, i, j, k + 1)



l = list(map(int, input().split(" ")))
Three_pairs(l, 0, 1, 2)



'''
l1=[3,2,5,4,1,6,8]
for i in range(len(l1)-2):
    j=i+1
    k=j+1
    while(k<len(l1)):
        print([l1[i],l1[j],l1[k]])
        k+=1
        if(k==len(l1)):
            j+=1
            k=j+1

'''