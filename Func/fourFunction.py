def make_int_list(x):
    x = [y for y in x.strip("\'").split()]
    x = ", ".join(x)
    return "["+x+"]"
def is_odd(e):
    if e%2 == 0:
        return False
    else:
        return True
def odd_list(alist):
    l = []
    for s in alist:
        if s%2 != 0:
            l.append(s)
    return l
def sum_square(alist):
    l = []
    for s in alist:
        s *= s
        l.append(s)
    k = sum(l)
    return k

exec(input().strip())