def first_fit(bins, s):
    for b in bins:
        if sum(b)+s <= 100:
            b.append(s)
            return
    bins.append([s])

def best_fit(bins, s):
    min_left = 100
    min_k = -1
    for i in range(len(bins)):
        su = sum(bins[i])
        if 100-su-s >= 0 and 100-su-s < min_left:
            min_left = 100-su-s
            min_k = i
    if min_k == -1:
        bins.append([s])
    else:
        bins[min_k].append(s)

def partition_FF(D):
    L = []
    for e in D:
        first_fit(L, e)
    return L

def partition_BF(D):
    L = []
    for e in D:
        best_fit(L, e)
    return L

exec(input().strip())