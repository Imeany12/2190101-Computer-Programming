def knows(R,x,y):
    if x in R:
        if y in R[x]:
            return True 
        else:
            return False
    else:
        return False
def is_celeb(R,x):
    other = [e for e in R if e !=x]
    for key in R:
        for name in R[key]:
            if name not in other:
                other.append(name)
    if x in other:
        other.remove(x)
    for pp in other:
        if knows(R,x,pp)==True:
            return False
        elif knows(R,pp,x) ==False:
            return False
    return True
def find_celeb(R):
    other = [e for e in R]
    for key in R:
        for name in R[key]:
            if name not in other:
                other.append(name)
    for x in other:
        if is_celeb(R,x) ==True:
            return x
    return None

def read_relations():
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1 : break
        elif d[0] in R:
            R[d[0]].add(d[1])
        else:
            R[d[0]] = {d[1]}
    return R
def main():
    R = read_relations()
    c = find_celeb(R)
    if c ==None:
        print("Not Found")
    else:
        print(c)
exec(input().strip())
# R = read_relations()
# print(is_celeb(R,"G"))

        
        
    
    
