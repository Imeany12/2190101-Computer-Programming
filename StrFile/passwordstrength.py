t = list(input())
num = ["0","1","2","3","4","5","6","7","8","9",]
sym = ["!","@","#","$","%","^","&","*","(",")",]
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def no_lowercase(t):
    l = []
    for x in t:
        if x.islower() == True:
            l.append(x)
    if len(l)> 0:
        return False
    else:
        return True    
def no_uppercase(t):
    u = []
    for x in t:
        if x.isupper() == True:
            u.append(x)
    if len(u)> 0:
        return False
    else:
        return True    
def no_number(t):
    n = []
    for x in t:
        if x in num:
            n.append(x)
    if len(n)> 0:
        return False
    else:
        return True 
def no_symbol(t):
    n = []
    for x in t:
        if x in sym:
            n.append(x)
    if len(n)> 0:
        return False
    else:
        return True 
def character_reptition(t):
    r = []
    for x in range(len(t)-3):
        if t[x]==t[x+1] and t[x+1]==t[x+2] and t[x+2]==t[x+3]:
            r.append(t[x])
    if len(r)>0:
        return True
    else:
        return False
def number_sequence(t):
    n= []
    for x in t:
        if x in num:
            n.append(x)
    y = num.index(n[0])
    if n[0] == num[y] and n[1] == num[y+1]  and n[2] == num[y+2] and n[3] == num[y+3]  :
        return True
    elif n[0] == num[y] and n[1] == num[y-1]  and n[2] == num[y-2] and n[3] == num[y-3]  :
        return True
    else:
        return False
def letter_sequence(t):
    n= []
    for x in range(len(t)):
        t[x] = t[x].lower()
        if t[x] in al:
            n.append(t[x])
    y = al.index(n[0])
    if n[0] == al[y] and n[1] == al[y+1]  and n[2] == al[y+2] and n[3] == al[y+3]  :
        return True
    elif n[0] == al[y] and n[1] == al[y-1]  and n[2] == al[y-2] and n[3] == al[y-3]  :
        return True
    else:
        return False

 

print(letter_sequence(t))
