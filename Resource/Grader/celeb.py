def knows(R,x,y) :
    if R[x] == y :
        return True
    else : return False

def is_celeb(R,x) :
    if R[x]-{x} != set() : return False
    for person in R:
        if x not in R[person] and person != x:
            return False
    return True

def find_celeb(R) :
    for i in dict.keys(R) :
        if is_celeb(R,i) :
            return i
    return None

def read_relations() :
    R = dict()
    s = set()
    while True:
        d = input().split()
        if len(d) == 1: break
        s.add(d[0]) ; s.add(d[1])
        if d[0] not in R:
            R[d[0]] = set()
        R[d[0]].add(d[1])
    for person in s: 
        if person not in R:
            R[person] = set()
    return R

def main():
    R=read_relations()
    c=find_celeb(R)
    if c == None:
        print('Not Found')
    else:
        print(c)
exec(input().strip())