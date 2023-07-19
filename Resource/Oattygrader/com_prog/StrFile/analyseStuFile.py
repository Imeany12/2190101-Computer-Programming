i = [x for x in input().split()]
k = []
f = open("data.txt", "r")
for x in f:
    if i[1][-2:] == x[:2]:
        k.append(float(x[-5:]))
if len(k)>0:
    k.sort()
    mi = min(k)
    ma = max(k)
    av = sum(k)/len(k)
    print(str(mi)+" "+str(ma)+" "+str(av))
else:
    print("Nodata")