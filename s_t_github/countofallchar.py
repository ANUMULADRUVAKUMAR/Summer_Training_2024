s="AbcDEFGOIoiE67#@"
d={'lv':0, 'lc':0, 'uv':0, 'uc':0, 'n':0, 's':0}
for i in s:
    if(i.islower()):
        if(i in "aeiou"):
            d['lv']+=1
        else:
            d['lc']+=1
    elif(i.isupper()):
        if (i in "AEIOU"):
            d['uv'] += 1
        else:
            d['uc'] += 1
    elif(i.isnumeric()):
        d['n']+=1
    elif(not i.isalnum()):
        d['s']+=1
for i in d:
    print(i,"-",d[i])