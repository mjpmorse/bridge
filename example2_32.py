from numpy import *
import broyden
import math
import time


def equations(x):
    u = x[0]
    v = x[1]
    f = array([ v - u**3 , u**2 + v**2 -1])
    return f


x0 = array([1.,1.])
u = x0[0]
v = x0[1]

b = identity(2)

xold = x0
tol = 1e-10

broyden.broyden(x0,equations,b,tol,1000)
    
    

    
