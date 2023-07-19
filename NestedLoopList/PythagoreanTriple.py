def gcd(a,b):
    while b != 0 :
        a,b = b,a%b
    return a
def is_coprime(a,b,c):
    x = [e for e in range(1,a+1) if a%e == 0]
    y = [e for e in range(1,b+1) if b%e == 0]
    z = [e for e in range(1,c+1) if c%e == 0]
    k = z[1:]+x[1:]+y[1:]
    k.sort()
    k.append("q")
    y=[]
    for e in range(len(k)-1):
        if k[e] ==k[e+1] and k[e+1]==k[e+2]:
            y.append(1)
    if len(y)>0:
        return False
    else:
        return True
            
def primitive_Pythagorean_triples(max_len):
    triple = []
    for a in range(3,max_len+1):
        for b in range(a+1,max_len+1):
            c = (a**2+b**2)**0.5
            if c%1 == 0 and int(c)<= max_len and is_coprime(a,b,int(c)) :
                c = int(c)
                k = [a,b,c]
                triple.append(k)
        for x in range(len(triple)):
            triple[x][0],triple[x][2]=triple[x][2],triple[x][0]
        triple.sort()
        for x in range(len(triple)):
            triple[x][0],triple[x][2]=triple[x][2],triple[x][0]
        for x in range(len(triple)-1):
            if triple[x][2] == triple[x+1][2] and triple[x][0]>triple[x+1][0]:
                triple[x],triple[x+1]=triple[x+1],triple[x]
    return triple
exec(input().strip())



