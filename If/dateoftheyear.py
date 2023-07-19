d = int(input())
m = int(input())
y = int(input())
y -= 543

if (y%400 == 0) or (y%4 == 0 and y%100 != 0):
    f =29
else:
    f =28

if m == 1:
    print(d)
elif m ==2:
    print(d+31)
elif m == 3:
    print(d+31+f)
elif m ==4:
    print(d+31+f+31)
elif m ==5:
    print(d+31+f+31+30)
elif m ==6:
    print(d+31+f+31+30+31)
elif m ==7:
    print(d+31+f+31+30+31+30)
elif m ==8:
    print(d+31+f+31+30+31+30+31)
elif m ==9:
    print(d+31+f+31+30+31+30+31+31)
elif m ==10:
    print(d+31+f+31+30+31+30+31+31+31)
elif m ==11:
    print(d+31+f+31+30+31+30+31+31+31+30)
elif m ==1:
    print(d+31+f+31+30+31+30+31+31+31+30+30)


