from numpy import *
import broyden2

def function(x):
    f = zeros(3)
    f[0] = 3.*x[0] + x[1] - x[2] - 4.
    f[1] = 2.*x[0] + 4.*x[1] + x[2] - 1.
    f[2] = -1.*x[0] + 2.*x[1] + 5.*x[2] - 1.
    return f

b0 = identity(3)
x0 = array([0,0,0])
print broyden2.broyden(x0,function,b0,1e-5,4000)
    
