station = {}
ans=[]
sec = []
while True:
    i = input().split()
    if len(i)==1:
        firststa = i[0]
        ans.append(firststa)
        break
    if i[0] in station:
        station[i[0]].append(i[1])
    else:
        station[i[0]] = [i[1]]
    if i[1] in station:
        station[i[1]].append(i[0])
    else:
        station[i[1]] = [i[0]]
for key in station:
    if key == firststa:
        for x in station[key]:
            if x not in ans:
                ans.append(x)
sec += ans
for s in ans:
    if firststa not in station:
        break
    if len(station)!=0:
        for x in station[s]:
            if x not in sec:
                sec.append(x)
for x in sorted(sec):
    print(x)
    
