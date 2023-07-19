name=["Robert","Dick","William","Dick","James","Jim","John","Jack","Margaret","Peggy","Edward","Ed","Sarah","Sally","Andrew","Andy","Anthony","Tony","Deborah","Debbie"]
n = int(input())
na = []
for x in range(n):
    i = input()
    if i in name:
        a = name.index(i)
        if a%2==0:
            na.append(name[a+1])
        elif a%2 == 1:
            na.append(name[a-1])
    elif i not in name:
        na.append("Not found")
for x in range(int(len(na))):
    print(na[x])






