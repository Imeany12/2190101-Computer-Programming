import numpy as np
def mult_table(nrows,ncols):
    M = np.ones((nrows,ncols))
    M[:,0] = np.arange(1,nrows+1).T
    M[0,:] = np.arange(1,ncols+1)
    for x in range(1,ncols):
        M[:,x] = M[:,0]*M[0,x]
    return M.astype(int)
exec(input().strip())
