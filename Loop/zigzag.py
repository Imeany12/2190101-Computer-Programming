i = int(input())
a = [i]
for x in range(i+1):
    In = input().split()
    a = a + In
    #Join list
if str(a[-1]) == "Zig-Zag":
    Min=[]
    Max=[]
    for x in range(1,int(len(a)-1)):
        if x%4 == 1 or x%4 == 0:
            Min.append(int(a[x]))
        elif x%4 == 2 or x%4 == 3:
            Max.append(int(a[x]))
elif str(a[-1])=="Zag-Zig":
    Min=[]
    Max=[]
    for x in range(1,int(len(a)-1)):
        if x%4 == 1 or x%4 == 0:
            Max.append(int(a[x]))
        elif x%4 == 2 or x%4 == 3:
            Min.append(int(a[x]))
print(Min)
print(str(min(Min))+" "+str(max(Max)))


