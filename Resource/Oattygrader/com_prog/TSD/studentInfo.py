n = int(input())
d1={}
na = []
for x in range(n):
    name,group,gen,de = input().split()
    d1[name] = (group,gen,de)
    na.append(name)
search = [e for e in input().split()]
ans = [e for e in na if search[0] in d1[e]]
if len(search)>1:
    for x in range(1,len(search)):
        ans = [e for e in ans if search[x] in d1[e]]
if len(ans)!=0:
    for x in sorted(ans):
        r = " ".join(d1[x])
        print(str(x)+" "+str(r))
else:
    print("Not Found")

    

