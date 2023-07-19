import numpy as np
X=np.array([[1,2,3]])
A=np.zeros((3,3))
A[:,0]=(X.T*X.T)[:,0]
#all of the A first colum
# print(A)
A[:,1]=X[0]
#all of the A second colum
# print(A)
A[:,2]=1
# print(A)
C=np.array([[1,2,2]])
# print(np.sum(A*C,axis=1))
#multiple first then sum by the row
# print((A*C).dot(np.array([[1],[1],[1]])))
D = np.arange(16).reshape(8,2)
# print(D)
A = np.array([])
arr = np.array([1, 2, 3, 4, 5, 6, 7])
x = arr%2==0
x = abs(x-1)
x = x.astype(bool)
#or this optimized version
arr = arr[np.logical_not(arr % 2 == 0)]
print(arr[x])

