import numpy as np

a = np.array([1,23,3])
#***** Write youtr codes here *****#
def get_column_from_bottom_to_top(A, c): # one line of code
    return  A[:, c][::-1]

def get_odd_rows(A): # one line of code
    return A[1::2]

def get_even_column_last_row(A) :
    return A[-1,::2]

def get_even_rows_last_column(A): # one line of code
    return A[::2,-1]

def get_diagonal1(A): # A is a square matrix; two lines of code
    return np.diag(A)

def get_diagonal2(A): # A is a square matrix; two lines of code
    return np.diag(np.fliplr(A))


exec(input().strip())
