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
    k = len(x)
    return k*(k-1)//2
def solvable(t):
    if len(t)%2 !=0 and inversions(t)%2==0:
        return False
    elif len(t)%2 ==0 and inversions(t)%2!=0 and row_number(t,0)%2==0:
        return False
    elif len(t)%2 ==0 and inversions(t)%2==0 and row_number(t,0)%2!=0:
        return False
    else:
        return True
exec(input().strip())