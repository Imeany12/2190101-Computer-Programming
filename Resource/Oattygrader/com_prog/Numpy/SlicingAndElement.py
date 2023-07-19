import numpy as np
def sum_2_rows(M):
    A = M[::2]
    B = M[1::2]
    return A+B
def sum_left_right(M):
    left = M[:,:len(M)//2]
    right = M[:,len(M)//2:]
    return left+right
def sum_upper_lower(M):
    upper = M[:len(M)//2]
    lower = M[len(M)//2:]
    return upper+lower
def sum_4_quadrants(M):
    q2 = M[:len(M)//2,:len(M[0])//2]
    q1 = M[:len(M)//2,len(M[0])//2:]
    q3 = M[len(M)//2:,:len(M[0])//2]
    q4 = M[len(M)//2:,len(M[0])//2:]
    return q1+q2+q3+q4
def sum_4_cells(M):
    ul = M[::2,::2]+M[::2,1::2]+M[1::2,::2]+M[1::2,1::2]
    #This divide the matrix in to 4 viriable then sum it together to mimick the sum of the 4 qudrant
    return ul
def count_leap_years(years):
    c = 0
    for x in years:
        x -=543
        if (x%400 == 0) or (x%4 == 0 and x%100 != 0): 
            c+=1
    return c
exec(input().strip())