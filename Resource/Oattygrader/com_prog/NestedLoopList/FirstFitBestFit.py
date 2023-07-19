def first_fit(L,e):
    for l in L:
        if sum(l)<=100-e:
            l.append(e)
            return
    L+=[[e]]
def best_fit(L,e):
    k =[]
    if len(L)!=0:
        for x in range(len(L)):
            k.append(sum(L[x]))
        p = [e for e in k]
        while len(k)!=0:
            if max(k)+e>100:
                k.remove(max(k))
        if len(k)!=0:
            f = p.index(max(k))
            L[f].append(e)
        else:
            L.append([e])
    else:
        L.append([e])
    return 
def partition_FF(D):
    p = []
    remian = [x for x in D]
    tmpset = [D[0]]
    D.remove(D[0])
    for e in range(len(D)):
        if sum(tmpset)+int(e)<=100 :
            tmpset.append(e)

    return len(p)
def partition_BF(D):
    p=[]
    l = []
    for a in range(len(D)):
        k = [D[a]]
        p.append(k)
    for y in p:
        best_fit(D,y)

    return l



    
    

exec(input().strip())