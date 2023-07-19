def get_consensus(ss):
    # write your code here.
    ju = []  
    lines = ss.split("\n")
    for x in range(len(lines)):
        lines[x] = lines[x].upper()
    for line in range(len(lines[0])):
        d1= {"A":0,"T":0,"G":0,"C":0}
        d2 = {}
        for x in lines:
            d1[x[line]]+=1
        for x in d1:
            if d1[x] not in d2:
                d2[d1[x]] =[x]
            else:
                d2[d1[x]] +=[x]
        for x in d2:
            d2[x].sort()
        num = [d1[e] for e in d1]
        ju.append("/".join(d2[max(num)]))
    consensus =" ".join(ju)
    return consensus # DO NOT MODIFY THIS LINE
def co(p):
    p.sort()
    d = {}
    d1 = {}
    ju = []
    for x in p:
        if x not in d:
            d[x] = 1
        else:
            d[x] +=1
    for x in d:
        if d[x] not in d1:
            d1[d[x]] = [x]
        else:
            d1[d[x]] +=[x]
    for x in d1:
            d1[x].sort()
    num = [d[e] for e in d]
    ju.append("/".join(d1[max(num)]))
    return ju
        

def get_consensus_generic(ss):
    # write your code here
    line = ss.split("\n")
    d = {}
    k = []
    for x in line:
        for y in range(len(x)):
            if y not in d:
                d[y] =  [x[y].upper()]
            else:
                d[y] +=  [x[y].upper()]
    for x in d:
        k+=co(d[x])
    consensus = " ".join(k)
    return consensus # DO NOT MODIFY THIS LINE

#---------------------------------------
# DO NOTE MODIFY CODE AFTER THIS SECTION
#---------------------------------------

'''ss = ("ATCGATGC\n" +  
      "GTACaCGC\n" +
      "ACTACAGC\n" +
      "CtCAATTC\n" + 
      "CTGgATTC")
print(get_consensus(ss))

ss = ("ATCGATGC\n" +
      "GTACaCCC\n" +
      "ACTACATC\n" + 
      "CtCAATAC")
print(get_consensus(ss))'''

ss = ("YCXBATGZ\n" +
      "YCVBaCGZ\n" +
      "ACXBCTGZ\n" +
      "CtCAATTZ\n" +
      "CTXAATTM")
print(get_consensus_generic(ss))

ss = ("YCXBATGZ\n" +      
     "YCVBaCGZHQ\n" +
     "ACXBCTGZHQ\n" + 
     "CtCAATTZHD\n" + 
     "CTXAATTMFD")
print(get_consensus_generic(ss))

ss = ("YCXBATGZ\n" +      
      "YCVCaCGZHQ\n" +
      "ACXDCTGZHQ\n" + 
      "CtCTATTZHD\n" + 
      "CTXAATTMFD")
print(get_consensus_generic(ss))
