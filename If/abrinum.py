i = int(input())
if i > 10**10:
    a = int(round(i/10**9,0))
    print(str(a)+"B")
elif i > 10**9:
    a =(round(i/10**9,1))
    print(str(a)+"B")
elif i > 10**7:
    a = int(round(i/10**6,0))
    print(str(a)+"M")
elif i > 10**6:
    a =(round(i/10**6,1))
    print(str(a)+"M")
elif i > 10**4:
    a = int(round(i/10**3,0))
    print(str(a)+"K")
elif i > 10**3:
    a = (round(i/10**3,1))
    print(str(a)+"K")
else:
    print(i)


