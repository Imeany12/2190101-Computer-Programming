nd = int(input())
de = {}
book = {}
stu = []
result = []
for x in range(nd):
    d,no = input().split()
    de[d] = int(no)
ns = int(input())
for x in range(ns):
    id,s,d1,d2,d3,d4 = input().split()
    book[id] = (d1,d2,d3,d4)
    stu.append((float(s),int(id)))
stu.sort(reverse=True)
for sco in stu:
    if de[book[str(sco[1])][0]]!=0:
        result.append((str(sco[1])+" "+book[str(sco[1])][0]))
        de[book[str(sco[1])][0]]-=1
    elif de[book[str(sco[1])][1]]!=0:
        result.append((str(sco[1])+" "+book[str(sco[1])][1]))
        de[book[str(sco[1])][1]]-=1
    elif de[book[str(sco[1])][2]]!=0:
        result.append((str(sco[1])+" "+book[str(sco[1])][2]))
        de[book[str(sco[1])][2]]-=1
    else:
        result.append((str(sco[1])+" "+book[str(sco[1])][3]))
        de[book[str(sco[1])][3]]-=1
for x in sorted(result):
    print(x)





