from numpy import *
import broyden 

def bridge(x):
    P = zeros((5,2))
    P[0] = [0,0]
    P[len(P)-1] = [1. , 0.]
    T = x[len(P)-1:]
    gv = array([0,-1])
    f = zeros(len(x))
    
    for k in range(len(P)-2):
        P[k+1] = [x[2*k] ,x[2*k+1]]

    for i in range(len(P)-1):
        Pd = P[i+1] - P[i]
        f[i] = linalg.norm(Pd) - L[i]                    

    for j in range(len(P)-2):
         f[4+2*j] = T[j]*(P[j+1,0]-P[j,0])/L[j] + T[j+1]*(P[j+2,0]-P[j+1,0])/L[j+1]
         f[5+2*j] = T[j]*(P[j+1,1]-P[j,1])/L[j] + T[j+1]*(P[j+2,1]-P[j+1,1])/L[j+1] - M[j]*9.81
    return f



L = array([0.5,0.5,0.5,0.5])
M = array([5.,1e-13,1e-13])
#x0 = array([0.5,-0.866,5*9.81/2,5*9.81/2])
#x0 = array([0.5,-0.866,5*9.81/2,5*9.81/2])
x0 = array([0.25,-0.5,0.5,-0.866,0.75,-0.5,5*9.81/2,5*9.81/2,5*9.81/2,5*9.81/2])
b0 = broyden.fdjac(bridge,x0)
#b0 = identity(4)
#print bridge(x0) 
x = broyden.broyden(x0,bridge,b0,1e-5,1000)
#print x
