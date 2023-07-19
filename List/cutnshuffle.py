c = [x for x in input().split()]
d = list(input())
n = int((len(c))/2)
for x in range(len(d)):
    if d[x] == "C":
        f = c[0:n]
        l = c[n:]
        c = l + f
    elif d[x] == "S":
        s = []
        f = c[0:n]
        l = c[n:]
        for y in range(n):
            s.append(f[y])
            s.append(l[y])
        c = s
print(c)
    
