import numpy as np

def mult_table(nrows,ncols) :
    a = np.arange(1,ncols+1)
    b = np.arange(nrows).reshape(nrows,1)
    return a*b

exec(input().strip())