import numpy as np
def toCelsius(f):
    f = (f-32)*5/9
    return f
def BMI(wh):
    w = wh[:,0]
    h = wh[:,1]
    h = h*1/10**2
    BMI = w/(h**2)
    return BMI
def distanceTo(p,Points):
    distance = lambda x,y:((x-p[0])**2+(y-p[1])**2)**0.5
    d = np.array([distance(Points[e][0],Points[e][1]) for e in range(len(Points))])
    return d
exec(input().strip())
