i = [str(x) for x in input().split()]
def In(n1, n2):
    sum = int(n1,2)+int(n2,2)
    print(bin(sum)[2:])
In(i[0],i[1])
