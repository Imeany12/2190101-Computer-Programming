import numpy as np
import math
def p(x):
    p = 1/(1+math.e**(-1*(-3.98+0.1*x[:,0]+0.5*x[:,1])))
    return p
exec(input().strip())