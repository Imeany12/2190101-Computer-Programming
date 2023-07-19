def row_number(t,e):
    for x in range(len(t)):
        if e in t[x]:
            return x
def flatten(t):
    k = []
    for x in t :
        for y in x:
            if y != 0:
                k.append(y)
    return k
def inversions(x):
    s = 0
    for u in range(len(x)):
        for v in range(u+1,len(x)):
            if x[u] >x[v]:
                s+=1
    return s
def solvable(t):
    if len(t)%2 !=0 and inversions(flatten(t))%2==0:
        return True
    elif len(t)%2 ==0 and inversions(flatten(t))%2!=0 and row_number(t,0)%2==0:
        return True 
    elif len(t)%2 ==0 and inversions(flatten(t))%2==0 and row_number(t,0)%2!=0:
        return True
    else:
        return False
exec(input().strip())
