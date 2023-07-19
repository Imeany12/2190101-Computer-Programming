n1 = int(input())
d1 =dict()
d2 = dict()
d3 =dict()
for y in range(n1):
    a,b = [x for x in input().split()]
    d1[a] = b
n2 = int(input())
for y in range(n2):
    a,b = [x for x in input().split()]
    if a not in d2:
        d2[a] = int(b)
    else:
        d2[a]+=int(b)
for x in d2:
    if x in d1:
        d3[x]=(int(d1[x])*int(d2[x]))
s = []
for x in d3:
    s.append(int(d3[x]))

ts = float(sum(s))
Tps =[x for x in d3 if d3[x] == max(s)]
Tps.sort()
if len(Tps)==0:
    print("No ice cream sales")
else:
    print("Total ice cream sales: "+str(ts))
    print("Top sales: "+str(", ".join(Tps)))




        

   









