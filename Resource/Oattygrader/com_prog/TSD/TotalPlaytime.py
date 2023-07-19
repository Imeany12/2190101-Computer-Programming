n = int(input())
d1 = dict()
d2 =dict()
genre = []
time = []
for x in range(n):
    a,b,c,d = [e for e in input().strip().split(", ")]
    sec = (int(d[:-3])*60)+int(d[-2:])
    if c in d1:
        d1[c] += sec
    else :
        d1[c] = sec
for k,v in d1.items():
    d2[v] = k
    time.append(v)
time.sort()
def sec(x):
    k = x-(int(x)//60)*60
    if len(str(k)) ==2:
        return k
    else:
        return "0"+str(k)
if len(time)>=3:
    print(d2[time[-1]]+" --> "+str(time[-1]//60)+":"+str(sec(time[-1])))
    print(d2[time[-2]]+" --> "+str(time[-2]//60)+":"+str(sec(time[-2])))
    print(d2[time[-3]]+" --> "+str(time[-3]//60)+":"+str(sec(time[-3])))
elif len(time)==2:
    print(d2[time[-1]]+" --> "+str(time[-1]//60)+":"+str(sec(time[-1])))
    print(d2[time[-2]]+" --> "+str(time[-2]//60)+":"+str(sec(time[-2])))
else:
    print(d2[time[-1]]+" --> "+str(time[-1]//60)+":"+str(sec(time[-1])))

