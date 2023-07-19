i = list(input())
k = []
j = []
l =[]
n = ["-","+"," ","1","2","3","4","5","6","7","8","9","0","*"]
c = 1
for x in i:
    k.append(x.lower())
k.sort()
k.append("น")
for x in range(len(k)-1):
    if k[x] in n:
        pass
    elif k[x] !=k[x+1]:
        j.append(-c)
        j.append(k[x])
        l.append(j)
        c=1
        j = []
    
    else:
        c +=1
l.sort()
for x in range(len(l)):
    l[x][0] = -l[x][0]
    print(str(l[x][1])+" -> "+str(l[x][0]))