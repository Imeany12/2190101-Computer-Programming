i = (input())
a = [i[0]]
b = 1
for x in range(0,int(len(i)-1)): 
    if i[x]== i[x+1]:
        b +=1
    elif i[x] != i[x+1]:
        a.append(b)
        a.append(i[x+1])
        b = 1
a.append(b)
b = " ".join(list(map(str,a))) 
print(b)

        

