u = input()
u = u[1:-1].split(", ")
u = list(map(float, u))
v = input()
v = v[1:-1].split(", ")
v = list(map(float, v))
s = [u[0]+v[0],u[1]+v[1],u[2]+v[2]]
print(str(u)+" + "+str(v)+" = "+str(s))








