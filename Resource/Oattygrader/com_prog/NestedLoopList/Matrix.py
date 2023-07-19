def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x : 
            r.append(float(e))
        m.append(r)
    return m
def mult_c(c,A):
    for e in range(len(A)):
        for o in range(len(A[0])):
            A[e][o] *= float(c)
    return A
def mult(A,B):
    k= []
    v = []
    for e in range(len(A)):
        for o in range(len(B[0])):
            s=0
            for y in range(len(A[0])):
                s += A[e][y]*B[y][o]
            v.append(s)
        k.append(v)
        v=[]
    return k
exec(input().strip())