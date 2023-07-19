n = []
ids = []
grade = []
Gr = ["A","B+","B","C+","C","D+","D","F"]
while True:
    i = input()
    if i == "q":
        break
    else:
        u = [x for x in i.split()]
        ids.append(u[0])
        grade.append(u[1]) 
uids = input().split()
#the code above are correct
for x in uids:
    y = ids.index(x)#who
    z = Gr.index(grade[y])
    if z>0 :
        grade[y] = Gr[z-1]
for y in range(len(ids)):
    for x in range(len(ids)-1):
        if ids[x]>ids[x+1]:
            ids[x],ids[x+1] = ids[x+1],ids[x]
            grade[x],grade[x+1] = grade[x+1],grade[x]
for x in range(len(ids)):
    print(str(ids[x])+" "+str(grade[x]))

