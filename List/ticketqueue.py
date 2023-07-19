q = []
ot = []
nt = []
p = []
a = []
z = []
n = int(input())
for k in range(n):
    c = input().split()
    if c[0] == "reset":
        q = []
        q.append(int(c[1]))
    elif c[0] == "new":
        nt.append(int(c[1]))
        print("ticket "+str(q[-1]))
        x = q[-1] + 1
        p.append(q[-1])
        p.append(int(c[1]))
        q.append(x)
    elif c[0] == "next":
        print("call "+str(q[0]))
        z.append(q[0])
        
        q.remove(q[0])
    elif c[0] == "order":

        ot.append(int(c[1]))
        nu = int(p.index(z[-1]))

        w = ot[0]-int(p[nu+1])
        print("qtime "+str(z[-1])+" "+ str(w))

        a.append(w)
        ot.remove(ot[0])
    elif str(c[0]) == "avg_qtime":
        s = sum(a)/int(len(a))
        print("avg_qtime "+str(round(s,4)))
        