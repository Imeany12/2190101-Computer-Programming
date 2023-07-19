w1 = list(input())
w2 = list(input())
a =[]
b = []
s = 0
for x in w1:
    a.append(x.lower())
for x in w2:
    b.append(x.lower())
while True:
    if " " in a:
        a.remove(" ")
    else:
        break
while True:
    if " " in b:
        b.remove(" ")
    else:
        break
a.sort()
b.sort()
print(a)
print(b)
for x in range(min(len(a),len(b))):
    if a[x] == b[x]:
        s +=1
if s == (max(len(a),len(b))):
    print("YES")
else:
    print("NO")

