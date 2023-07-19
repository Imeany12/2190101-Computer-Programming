def add_poly(p1,p2):
    d1 = {}
    degree = []
    for e in p1:
        d1[e[1]] = e[0]
        degree.append(e[1]) 
    for e in p2:
        if e[1] not in d1:
            d1[e[1]] = e[0]
            degree.append(e[1])
        else:
            d1[e[1]]+= e[0] 
    degree.sort(reverse=True)
    sum = [(d1[x],x) for x in degree if d1[x]!=0]
    return sum
def mult_poly(p1,p2):
    degree = []
    d1 ={}
    for a in p1:
        for b in p2:
            newd = a[1]+b[1]
            newco = a[0]*b[0]
            if newd not in degree:
                degree.append(newd)
                d1[newd] = newco
            else:
                d1[newd] += newco
    degree.sort(reverse=True)
    ans = [(d1[x],x) for x in degree]
    return ans
for i in range(3):
    exec(input().strip())