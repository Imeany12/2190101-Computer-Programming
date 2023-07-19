import numpy as np
# Write your code for
def sum_2_rows(M) :
    return M[::2] + M[1::2]

def sum_left_right(M):
    return M[:,0:len(M)//2]+M[:,len(M)//2:]

def sum_upper_lower(M) :
    return M[:len(M)//2:,:] + M[len(M)//2::,:]

def sum_4_quadrants(M) :
    return sum_upper_lower(sum_left_right(M))

def sum_4_cells(M) :
    return M[::2,::2] + M[1::2,::2] + \
        M[::2,1::2] + M[1::2,1::2]

def count_leap_years(years) :
    year = years - 543
    return np.sum((year%400==0)|(year%4==0)&(year%100!=0))
exec(input().strip())