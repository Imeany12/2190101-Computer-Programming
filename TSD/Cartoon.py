d1= dict()
type = []
while True:
    i = input()
    name= i.split(", ")
    if i =="q":
        break
    elif name[1] not in type:
        d1[name[1]] = name[0]
        type.append(name[1])
    elif name[1] in type:
        d1[name[1]] += ", " +name[0]
        #add the next name after the previous name
for x in type:
    print(x+": "+d1[x])




    

