i = (input())
a = i[3]+i[10]+i[17]+i[24]+i[31]
b = i[7]+i[12]+i[17]+i[22]+i[27]
c = int(a)+int(b)+10000
d = str(c//10**3%10)+str(c//10**2%10)+str(c//10**1%10)


e = int(d[0])+int(d[1])+int(d[2])
e = str(e)
las = e[-1]
e = int(las)
l = ["A","B","C","D","E","F","G","H","I","J"]

print(str(d)+l[e])


