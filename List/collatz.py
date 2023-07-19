n = int(input())
k = [n]
while n != 1:
    if n%2 == 0:
        n = n/2
        k.append(int(n))

    else:
        n = 3*n+1
        k.append(int(n))
k = k[-15:]
k = list(map(str,k))
print("->".join(k))
