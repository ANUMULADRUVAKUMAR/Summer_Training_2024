l1=[4,2,4,4,4,8,8]
    c=1
    w=l1[0]
for i in range(1,len(l1)):
    if w==l1[i]:
        c+=1
    else:
        if(c>1):
            c-=1
        else:
            c=1
            w=l1[i]
print(w)

'''
d={}
        n=len(nums)//2
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for i in d:
            if d[i]>n:
                return i
                break
'''