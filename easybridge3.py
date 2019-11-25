#sudo bridge 3
from numpy import *
import broyden2
from time import sleep
import newton_multid as new

def bridge(x):

    h = 1.
    s2 = (2.)**(1./2)
    t1 = 0.806047
    L = array([s2, s2, s2, s2, s2, s2])
    M = array([h*.2226, h*0.073, .0581, h*.0822, h*.128])
    


    P = zeros((7,2))
    P[0] = [0,0]
    P[len(P)-1] = [6.0, 0.0]
    T = x[len(P)+3:]
    gv = array([0,-1])
    f = zeros(len(x))
    g = 9.81
    #print T
    
    for k in range(len(P)-2): 
        P[k+1] = [x[2*k] ,x[2*k+1]]
    #print P
    for i in range(len(P)-1): 
        Pd = P[i+1] - P[i]
        f[i] = linalg.norm(Pd) - L[i] 

    for j in range(1,len(P)-1): 
         f[i+1+2*(j-1)] = T[j-1]*(P[j-1,0]-P[j,0])/L[j-1] + T[j]*(P[j+1,0]-P[j,0])/L[j]
         f[i+2+2*(j-1)] = T[j-1]*(P[j-1,1]-P[j,1])/L[j-1] + T[j]*(P[j+1,1]-P[j,1])/L[j] - M[j-1]*9.81
         #print i+2+2*(j-1)
         #print f
    return f




x0 = array([ 0.49371527,-1.32523403,1.57620047,-2.23530315,2.95255255,-2.56034921,
  4.32614317,-2.2238246,5.3639315,-1.26309812,3.39307124, 1.54756028,
  1.21713849,  1.21958542,  1.61421268,  2.63369606])
print bridge(x0)


#print bridge(x0)
b0 = broyden2.fdjac(bridge,x0)
xnew = broyden2.broyden(x0,bridge,b0,.00001,1000)
print xnew
'''
'''
x = array([1.,-1., 2.,-2., 3.,-3., 4.,-2., 5.,-1.,
            9.81*(M[0]+M[1])+t1,
            9.81*(M[1])+t1,
            t1,
            t1,
            9.81*(M[3])+t1,
            9.81*(M[4]+M[3])+t1])



for i in linspace(0,1,1e5):
    
    h = i
    b0 = broyden2.fdjac(bridge,x)
    xnew = new.newton(bridge,b0,x,1e-10)
    x = xnew
    print x

    if math.isnan(linalg.norm(xnew,inf)) == True:
        print i
        print x
        print 'nan break'
        break
print xnew
'''




