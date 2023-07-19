i = [int(x) for x in input().split()]
i.sort()
k = [i[0]]
n = 1
for x in range(len(i)-1):
    if i[x] != i[x+1]:
        k.append(i[x+1])
        n += 1
if len(k)>10:
    k=k[0:10]
print(n)
print(k)