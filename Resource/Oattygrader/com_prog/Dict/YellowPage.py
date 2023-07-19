d1 = dict()
d2 =dict()
n1 = int(input())
for x in range(n1):
    a,b,c = [y for y in input().split()]
    d1[str(a)+" "+str(b)]=c
    d2[c] =str(a)+" "+str(b)
n2 = int(input()) 
for x in range(n2):
    i = input()
    if i in d1:
        print(str(i)+" --> "+str(d1[i]))
    elif i in d2:
        print(str(i)+" --> "+str(d2[i]))
    else:
        print(str(i)+" --> Not found")
