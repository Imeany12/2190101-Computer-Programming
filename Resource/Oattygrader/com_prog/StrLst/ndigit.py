i = int(input())
if i > 0:
    a = "positive"
elif i < 0:
    a = "negative"
else:
    a = "zero"
if i%2==0:
    b = "even"
else:
    b = "odd"
print(a)
print(b)