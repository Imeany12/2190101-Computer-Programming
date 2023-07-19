def row_number(t, e) :
    for i in range(len(t)):
        if e in t[i] : return i
    return -1

def flatten(t):
    return [e for a in t for e in a if e != 0]

def inversions(x):
    return sum([1 for i in range(len(x))
                    for j in range(i+1,len(x))
                       if x[i]>x[j]])
def solvable(t):
    ninvs = inversions(flatten(t))
    if len(t)%2 == 1:
        if ninvs % 2 == 0 : return True
    else:
        row_of_0 = row_number(t,0)
        if row_of_0 % 2 == 0 and ninvs % 2 == 1 or \
           row_of_0 % 2 == 1 and ninvs % 2 == 0 :
            return True
    return False
        

exec(input().strip())
