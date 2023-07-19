import numpy as np
def get_column_from_bottom_to_top(A,c):
    A = A[::-1,c]
    return A 
def get_odd_rows(A):
    A = A[1::2]
    return A
def get_even_column_last_row(A):
    A = A[-1,::2]
    return A
def get_diagonal1(A):
    g=[]
    for x in range(len(A)):
        g.append(A[x][x])
    A = np.array(g)
    return A
def get_diagonal2(A):
    g = []
    for x in range(len(A)):
        g.append(A[x][(x+1)*-1])
    A = np.array(g)
    return A
exec(input().strip())

