from numpy import *
import broyden2 
import newton_multid as new
def bridge(x):
    P = zeros((7,2))
    P[0] = [0,0]
    P[len(P)-1] = [L[5] , -1.*(L[0]+L[1]+L[2]+L[3]+L[4])]
    T = x[len(P)+1:]
    gv = array([0,-1])
    f = zeros(len(x))
    g = 9.81
    
    
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
s2 = sqrt(2)
t1 = .0581*9.81
h = 0
L = array([1.12, .301,.621,.261,.528,.816])
M = array([h*.2226, h*0.073, .0581, h*.0822, h*.128])
x0 = array([.13,-1.*L[0],
            .26,-1.*(L[0]+L[1]),
            .39,-1.*(L[0]+L[1]+L[2]),
            .53,-1.*(L[0]+L[1]+L[2]+L[3]),
            .67,-1.*(L[0]+L[1]+L[2]+L[3]+L[4]),
            9.81*(M[0]),
            9.81*(M[0]+M[1]),
            9.81*(M[0]+M[1]+M[2]),
            9.81*(M[0]+M[1]+M[2]+M[3]),
            9.81*(M[0]+M[1]+M[2]+M[3]+M[4]),
            1e-5])


'''
x0 = array([0.5,-2.7,1,-3.8,1.5,-5.3,2.5,-3.8,3,-2.7,
            9.81*(M[0]+M[1]/2),
            9.81*(M[1]/2),
            9.81*(M[1]/2),
            9.81*(M[2]+M[1]/2),
            9.81*(M[3]+M[2]+M[1]/2),
            9.81*(M[4]+M[3]+M[2]+M[1]/2)])
        '''
#b0 = eye(16)
b0 = broyden2.fdjac(bridge,x0)
#x = broyden2.broyden(x0,bridge,b0,1,1000)
#print x
print bridge(x0)
#print new.newton(bridge,b0,x0,.001)



