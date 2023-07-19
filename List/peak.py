i = [int(x) for x in input().split()]
p = 0
for x in range(1,int(len(i))-1):
    if i[x-1]<i[x] and i[x]>i[x+1]:
        p += 1
print(p)
print(i)
    