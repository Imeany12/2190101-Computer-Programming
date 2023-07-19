import numpy as np

def read_data() :
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n,4),int)
    for i in range(n) :
        data[i] = [int(e) for e in input().split()]
    return weight,data

def report_lower_than_mean(weight,data) :
    score = data[::,1:]*weight
    total = np.sum(score, axis=1)
    id = data[total < np.mean(total)][::,0]
    if id.shape[0] > 0 :
        print(", ".join([str(e) for e in id]))
    else : print("None")

exec(input().strip())