n = int(input())
d1 = dict()
d2 =dict()
win=[]
for e in range(n):
    w,l= [x for x in input().split()]
    d1[w] = l
    d2[l] = w
for k,v in d1.items():
    if k not in d2:
        win.append(k)
print(sorted(win))


    