course = input()
teacher = input()
database = input()
d1 =dict()
d2 = dict()
c = open(course)
t = open(teacher)
d = open(database)
for x in c:
    k,v = [e for e in x.strip().split(",")]
    d1[k] =v
for x in t:
    k,v = [e for e in x.strip().split(",")]
    d2[k] =v
for x in d:
    cid, tn = [e for e in x.strip().split(",")]
    if cid in d1 and tn in d2:
        print(d1[cid]+","+d2[tn])
    else:
        print("record error")
