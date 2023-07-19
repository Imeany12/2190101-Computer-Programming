def reverse(d):
    k = dict()
    for x in d:
        k[d[x]] =x

    return k

            

def keys(d,v):
    u = []
    for x in d:
        if d[x] == v:
            u.append(x)
    return u
exec(input().strip())
