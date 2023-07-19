n = int(input())
id = {}
ids = []
for i in range(n) :
    a = input().split(":")
    id[a[0]] = set(a[1].strip().split(", "))
    ids.append(a[0])
check = str(input())
found = False
for i in ids :
    if len(id[check] & (id[i])) > 0 and i != check:
        print(i)
        found = True
if not found :
    print("Not Found")
