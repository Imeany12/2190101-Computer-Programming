"""char = "abcdefghijklmnopqrstuvwxyz"
countchar = {}
for i in char :
    countchar[i] = 0
s = ""
for i in str(input()) :
    if i.isalpha() :
        s += i
s = s.lower()
for i in char :
    for j in s :
        if i == j :
            countchar[i] += 1
res = []
for key in dict(sorted(countchar.items())) :
    res.append([-1*countchar[key],key])
res = sorted(res)
for i in res[::] :
    if i[0] == 0 :
        pass
    else :
        print(i[1] +" -> "+ str(-1*i[0]))"""

"""n = int(input())
iceprice = {}
for i in range(n) :
    x = input().split()
    iceprice[x[0]] = x[1]
sale = int(input())
icesale = {}
for i in range(sale) :
    x = input().split()
    if x[0] not in dict.keys(icesale) :
        icesale[x[0]] = float(x[1])
    else :
        icesale[x[0]] += float(x[1])    
sum = 0
for key in icesale :
    if key in dict.keys(iceprice) :
        sum += float(iceprice[key])*float(icesale[key])
        icesale[key] = float(iceprice[key])*float(icesale[key])
    else : 
        icesale[key] = 0
res = [k for k,v in icesale.items() if v == max(dict.values(icesale))]
if sum == 0 :
    print("No ice cream sales")
else :
    print("Total ice cream sales: "+str(sum))
    print("Top sales: " + ", ".join(sorted(res)))"""

"""n = int(input())
arr = []
for i in range(n) :
    count = 0
    text = str(input())
    for i in text :
        if i == "." :
            count += 1
        elif i != "." :
            break
    arr.append(text[count//2::])
for i in arr:
    print(i)"""
# n = int(input())
# if n == 0 :
#     print("0" + "\n" + "0")
# else :
#     l = []
#     for i in range(n) :
#         l.append({int(e) for e in input().split()})
#     union = l[0]
#     intersection = l[0]
#     for i in range(1,len(l)) :
#         union = union.union(l[i])
#         intersection = intersection.intersection(l[i])
#     print(len(union))
#     print(len(intersection))
def time(a) :
    a = a.split(":")
    total = int(a[0])*60 + int(a[1])
    return total

def timetostring(a) :
    sec = a%60
    a = a//60
    if len(str(sec)) == 1 :
        sec = "0"+str(sec)
    return str(a) + ":" +str(sec)

n = int(input())
data = []
for i in range(n) :
    data.append(tuple(input().split(", ")))
genretime = {}
for i in range(len(data)) :
    if data[i][2] not in dict.keys(genretime) :
        genretime[data[i][2]] = time(data[i][3])
    else :
        genretime[data[i][2]] += time(data[i][3])
rev = {}
for key in dict.keys(genretime) :
    rev[genretime[key]] = key
genretime = sorted(genretime.values())  #dict(sorted(genretime.items(), key=lambda item: item[1], reverse=True))
genretime.reverse()
# timer = sorted(genretime.values()).reverse()
count = 0
for i in genretime :
    if count == 3 : break
    print(rev[i] +" --> " + timetostring(i))
    count += 1
# print(timer)
