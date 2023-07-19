i = input()
k = []
m = ""
n = ["\"","\'","-",",","(",")","."]
for x in i:
    if x in n:
        x = " "
    m += x
o = m.split()
for x in o:
    k.append(x[0].upper())
    k.append(x[1:].lower())
l = "".join(k)

print(str(l[0].lower())+l[1:])
    
    

    

