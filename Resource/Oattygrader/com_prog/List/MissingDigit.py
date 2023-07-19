i = list(input())
num = [0,1,2,3,4,5,6,7,8,9]
num = list(map(str,num))
for x in i :
    if x in num:
        num.remove(x)
if len(num) == 0:
    print("None")
else:
    print(",".join(num))







