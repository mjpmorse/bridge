from numpy import *
import broyden2 

def bridge(x):
    P = zeros((7,2))
    P[0] = [0,0]
    P[len(P)-1] = [-0.1 , -1.*(L[0]+L[1]+L[2]+L[3]+L[4]+L[5])]
    T = x[len(P)+1:]
    gv = array([0,-1])
    f = zeros(len(x))
    
    
    
    for k in range(len(P)-2): 
        P[k+1] = [x[2*k] ,x[2*k+1]]
    #print P
    for i in range(len(P)-1): 
        Pd = P[i+1] - P[i]
        f[i] = linalg.norm(Pd) - L[i]
        #print f
    for j in range(len(P)-2): 
         f[i+1+2*j] = T[j]*(P[j+1,0]-P[j,0])/L[j] - T[j+1]*(P[j+2,0]-P[j+1,0])/L[j+1]
         f[i+2+2*j] = T[j]*(P[j+1,1]-P[j,1])/L[j] + T[j+1]*(P[j+2,1]-P[j+1,1])/L[j+1] - M[j]*9.81
    #print f
    return f

    


L = array([1.12, .301,.621,.261,.528,.816])
M = array([.2226, 0.073, .0581, .0822, .128])
x0 = array([-0.02,-1.*L[0],-0.04,-1.*(L[0]+L[1]),-0.06,-1.*(L[0]+L[1]+L[2]),-0.07,-1.*(L[0]+L[1]+L[2]+L[3]),-0.08,
            -1.*(L[0]+L[1]+L[2]+L[3]+L[4]),
            9.81*(M[0]+M[1]+M[2]+M[3]+M[4]),
            9.81*(M[1]+M[2]+M[3]+M[4]),
            9.81*(M[2]+M[3]+M[4]),
            9.81*(M[3]+M[4]),
            9.81*(M[4]), 1e-4])

#b0 = broyden2.fdjac(bridge,x0)
x = broyden2.broyden(x0,bridge,b0,1,1000)
print x
print bridge(x0)
