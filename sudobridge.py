from numpy import *
import broyden 

def bridge(x):
    P = zeros((7,2))
    P[0] = [0,0]
    P[6] = [3.0, 0]
    T = x[9:]
    gv = array([0,-1])
    f = zeros(16)

    for k in range(5):
        P[k+1] = [x[2*k] ,x[2*k+1]]

    for i in range(6):
        Pd = P[i+1] - P[i]
        f[i] = linalg.norm(Pd) - L[i]                    
#print f
    for j in range(5):
         f[6+2*j] = T[j]*(P[j+1,0]-P[j,0])/L[j] + T[j+1]*(P[j+2,0]-P[j+1,0])/L[j+1]
         f[7+2*j] = T[j]*(P[j+1,1]-P[j,1])/L[j] + T[j+1]*(P[j+2,1]-P[j+1,1])/L[j+1] - M[j]*9.81
#print f
    return f
h=1e-5
L = array([1., .25, .5, .5, .25, 1.])
#M = array([.2226, 0.0822, .0581, .0822, .2226])
#L = array([1.12, .301,.621,.261,.528,.816])
M = array([h*.2226, h*0.073, .0581, h*.0822, h*.128])
x0 = array([0.857143,-0.5714,1.07,-0.643798,1.5,-0.901317,1.93,-0.643798,2.14286,-0.5714,
            (M[0]+M[1]+M[2]/2)*9.81,(M[1]+M[2]/2)*9.81,(M[2]/2)*9.81,
            (M[2]/2)*9.81,(M[3]+M[2]/2)*9.81,(M[3]+M[4]+M[2]/2)*9.81])
b0 = broyden.fdjac(bridge,x0)
x = bridge(x0)
#x = broyden.broyden(x0,bridge,b0,.1,10000)
#print x
