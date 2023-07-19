
i = [float(x) for x in input().split()]
for x in range(3):
    if i[0]>i[1]:
        i[0],i[1]=i[1],i[0]
    if i[1]>i[2]:
        i[2],i[1]=i[1],i[2]
    if i[2]>i[3]:
        i[2],i[3]=i[3],i[2]


a = (i[1]+i[2])/2
print(round(a,2))




