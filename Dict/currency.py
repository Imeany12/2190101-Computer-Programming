def total(pocket):
    s = 0
    for x in pocket:
        s += int(x)*int(pocket[x])
    return s
def take(pocket,money_in):
    for x in money_in:
        if x not in pocket:
            pocket [x] = money_in[x]
        else:
            pocket[x] += money_in[x]
    return pocket
def pay(pocket,amt):
    if total(pocket)>=amt:
        balance=[e for e in pocket]
        balance.sort(reverse=True)
        give = dict()
        for x in balance:
            if x<= amt and amt> 0:
                pocket[x]-=amt//x
                give[x] = amt//x
                if pocket[x]<0:
                    give[x]+=pocket[x]
                    #give only it exsit
                    pocket[x]+=-1*pocket[x]
                    #return the money that it borrow
                amt -=x*give[x]
        return give
    else:
        return {}
exec(input().strip())