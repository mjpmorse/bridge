from numpy import *
import broyden 

def bridge(x):
    P = zeros((7,2))
    P[0] = [0,0]
    P[6] = [3.053 , .184]
    L = array([1.12, .301,.621,.261,.528,.816])
    M = array([.2226, 0.073, .0581, .0822, .128])
    T = x[len(P)+3:]
    gv = array([0,-1])
    f = zeros(16)

    for k in range(len(P)-2): 
        P[k+1] = [x[2*k] ,x[2*k+1]]
    for i in range(len(P)-1): 
        Pd = P[i+1] - P[i]
        f[i] = linalg.norm(Pd) - L[i] 
    for j in range(1,len(P)-1): 
         f[i+1+2*(j-1)] = T[j-1]*(P[j-1,0]-P[j,0])/L[j-1] + T[j]*(P[j+1,0]-P[j,0])/L[j]
         f[i+2+2*(j-1)] = T[j-1]*(P[j-1,1]-P[j,1])/L[j-1] + T[j]*(P[j+1,1]-P[j,1])/L[j] - M[j-1]*9.81
    
    return f
    
#b0 = identity(16)
#x0 = array([0.5,-2.7,1,-3.8,1.5,-5.3,2.5,-3.8,3,-2.7,5.4537,3.27222,1.09074,1.09074,3.27222,5.4537])

#x = broyden.broyden(x0,bridge,b0,1e-5)
#print x

