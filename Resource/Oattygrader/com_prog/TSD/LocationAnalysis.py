n = int(input())
d = dict()
samecity = []
people = []
for x in range(n):
    id,cities = input().strip().split(": ")
    cities = cities.split(", ")
    d[id] = cities
    people.append(id)
keyID = input()
keycity = d[keyID]
for p in range(len(people)):
    for e in d[people[p]]:
        if e in keycity:
            if people[p] not in samecity:
                samecity.append(people[p])  
samecity.remove(keyID)
if len(samecity)!=0:
    for x in samecity:
        print(x)
else:
    print("Not Found")


