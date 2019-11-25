from numpy import *
import broyden2
from time import sleep

def bridge(x):
    P = zeros((7,2))
    P[0] = [0,0]
    P[len(P)-1] = [6.0, 0.0]
    T = x[len(P)+1:]
    gv = array([0,-1])
    f = zeros(len(x))
    g = 9.81
    print 'T'
    print T
    
    for k in range(len(P)-2): 
        P[k+1] = [x[2*k] ,x[2*k+1]]
    #print P
    for i in range(len(P)-1): 
        Pd = P[i+1] - P[i]
        f[i] = linalg.norm(Pd) - L[i] 

    '''for j in range(1,len(P)-1): 
         f[i+1+2*(j-1)] = T[j-1]*(P[j-1,0]-P[j,0])/L[j-1] + T[j]*(P[j+1,0]-P[j,0])/L[j]
         f[i+2+2*(j-1)] = T[j-1]*(P[j-1,1]-P[j,1])/L[j-1] + T[j]*(P[j+1,1]-P[j,1])/L[j] - M[j-1]*9.81
         print i+2+2*(j-1)
         #print f
    return f
    '''
    f[6]  = T[0]*abs((P[1,0]-P[0,0])/L[0]) - T[1]*abs((P[2,0]-P[1,0])/L[1]) - M[0]*g
    f[7]  = T[0]*abs((P[1,1]-P[0,1])/L[0]) - T[1]*abs((P[2,1]-P[1,1])/L[1])

    f[8]  = T[1]*abs((P[2,0]-P[1,0])/L[1]) - T[2]*abs((P[3,0]-P[2,0])/L[2]) - M[1]*g
    f[9]  = T[1]*abs((P[2,1]-P[1,1])/L[1]) - T[2]*abs((P[3,1]-P[2,1])/L[2])

    f[10] = T[3]*abs((P[3,0]-P[4,0])/L[3]) + T[2]*abs((P[3,0]-P[2,0])/L[2]) - M[2]*g
    f[11] = T[3]*abs((P[3,1]-P[4,1])/L[3]) - T[2]*abs((P[3,1]-P[2,1])/L[2])

    f[12] = T[4]*abs((P[5,0]-P[4,0])/L[4]) - T[3]*abs((P[3,0]-P[4,0])/L[3]) - M[3]*g
    f[13] = T[4]*abs((P[5,1]-P[4,1])/L[4]) - T[3]*abs((P[3,1]-P[4,1])/L[3]) 

    f[14] = T[5]*abs((P[6,0]-P[5,0])/L[5]) - T[3]*abs((P[5,0]-P[4,0])/L[4]) - M[4]*g
    f[15] = T[5]*abs((P[6,1]-P[5,1])/L[5]) - T[3]*abs((P[5,1]-P[4,1])/L[4])
    return f


    



    
h = 1e-20
s2 = (2.)**(1./2)
t1 = 0.806047
L = array([s2, s2, s2, s2, s2, s2])
M = array([h*.2226, h*0.073, .0581, h*.0822, h*.128])
#M = array([h*.2226, h*0.073, 1, h*.0822, h*.128])
x0 = array([1.,-1., 2.,-2., 3.,-3., 4.,-2., 5.,-1.,
            9.81*(M[0]+M[1])+t1,
            9.81*(M[1])+t1,
            t1,
            t1,
            9.81*(M[3])+t1,
            9.81*(M[4]+M[3])+t1])

#b0 = broyden2.fdjac(bridge,x0)
#x = broyden2.broyden(x0,bridge,b0,1,1000)
#print x
print bridge(x0)

