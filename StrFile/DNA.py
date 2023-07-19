i = list(input().strip())
dna = ["A","T","G","C"]
for x in range(len(i)):
    i[x] = i[x].upper()
    
c = input()
f= []
s = 1
m = 0
if c =="R":
    for x in range(1,len(i)+1):
        if i[-x] == "A":
            f.append("T")
        elif i[-x] == "T":
            f.append("A")
        elif i[-x] == "G":
            f.append("C")
        elif i[-x] == "C":
            f.append("G")
    print("".join(f))
elif c=="F":
    i.sort()
    i.append("k")
    for x in range(len(i)-1):
        if i[x] == i[x+1]:
            s += 1
        elif i[x] not in dna:
            print("Invalid DNA")
        else:
            f.append(i[x]+"="+str(s))
            s = 1
    print(f[0]+", "+f[3]+", "+f[2]+", "+f[1])
elif c=="D":
    w = input()
    if i[x] not in dna:
            print("Invalid DNA")
    else:
        for x in range(len(i)):
            if w[0]==i[x-1] and w[1]==i[x]:
                m+=1
        print(m)
        






