i = int(input())
p = set()
inter = set()
if i ==0:
    print(0)
    print(0)
else:
    j = set()
    k = [int(e) for e in input().split()]
    k = set(k)
    union = set(k)
    inter = set(k) 
    for x in range(i-1):
        e = [int(b) for b in input().split()]
        e = set(e)
        union = union.union(e)
        inter = inter.intersection(e)
    print(len(union))
    print(len(inter))