import numpy as np
def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n,4),int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight,data
def report_lower_than_mean(weight,data):
    av = np.sum(np.sum(data[:,1:],axis =1),axis=0)//len(data)//3
    k=[]
    for x in range(len(data)):
        if np.sum(data[x,1:],axis=0)//3<av:
            k.append(str(data[x,0]))
    if len(k)==0:
        return print("None")
    else:
        return print(", ".join(k))
exec(input().strip())


