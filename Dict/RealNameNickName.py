n = int(input())
d1 = dict()
d2 = dict()
na = []
for x in range(n):
    a,b = [y for y in input().split()]
    d1[a] = b
    d2[b] = a
i = int(input())
for x in range(i):
    c = input()
    if c in d1:
        print(d1[c])
    elif c in d2:
        print(d2[c])
    else:
        print("Not found")
    
    
  
    
        