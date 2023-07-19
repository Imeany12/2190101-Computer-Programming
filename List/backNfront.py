i = int(input())
setone = []
setthree = []
for x in range(i):
    i = int(input())
    setone.append(i)
settwo = [int(x) for x in input().split()]

if -1 not in settwo:
    while True:
        i = int(input())
        
        if i == -1:
            break
        else:
            setthree.append(i)
s = setone + settwo + setthree
o = []
if int(len(s))%2 == 0:
    for x in range(1,int((len(s))/2)+1):
        o.append(s[-1*(2*x-1)])
    for x in range(int((len(s))/2)):
        o.append(s[(2*x)])
else:
    for x in range(1,int((len(s))/2)+1):
        o.append(s[-1*(2*x)])
    for x in range(int((len(s))/2)+1):
        o.append(s[(2*x)])
    
print(o)