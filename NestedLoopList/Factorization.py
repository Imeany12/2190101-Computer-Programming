def factor(N):
    k = []
    s= 2
    t = 0
    n=N
    while s<=N:      
        if n%s == 0:
            n//= s
            t+=1
        elif n%s != 0 and t!=0 :
            k.append([s,t])
            s+=1
            t =0
        else:
            s+=1
    return k
exec(input().strip())