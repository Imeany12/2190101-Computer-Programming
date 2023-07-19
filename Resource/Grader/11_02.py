import numpy as np

def toCelsius(f) :
    return (f-32)*(5/9)

def BMI(wh) :
    # print(wh[:,0],wh[:,1])
    w = wh[:,0]
    h = wh[:,1]
    return w/((h/100)**2)

def distanceTo(p,points) :
    dx = points[:,0] - p[0]
    dy = points[:,1] - p[1]
    return (dx**2+dy**2)**0.5

exec(input().strip())