import math
i = int(input())
b = []
id = 1
for x in range(i):
    c = []
    k = [float(x) for x in input().split()]
    x = math.sqrt(k[0]**2+ k[1]**2)
    c.append(x)
    c.append(id)
    c =c+k
    b.append(c)
    id +=1
b.sort()
cor = b[2]
print("#"+str(i)+": ("+str(round(cor[2],2))+", "+str(round(cor[3],2))+")")


