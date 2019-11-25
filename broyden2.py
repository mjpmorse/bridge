from numpy import *
import math
import time

def jacobianUpdate(bi,dx,df):
    dxt = transpose(dx)
    bdf = dot(bi,df)
    inside = dx - bdf
    num = dot(inside,dxt)
    num = dot(num,bi)
    den = dot(bi,df)
    den = dot(dxt,den)
    bip1 = bi + num/den
    return bip1


def guessUpdate(xi,bi,f):
    bif = dot(bi,f)
    xip1 = xi - bif
    return xip1
    
def broyden(x0,f,b,tol,lim):
    xold = x0
    i = 0
    while True:
        i += 1
        #print i
        fold = f(xold)
        xnew = guessUpdate(xold,b,fold)
        fnew = f(xnew)
        dx = transpose(array([xnew - xold]))
        df = transpose(array([fnew - fold]))
        bnew = jacobianUpdate(b,dx,df)
        #print bnew
        #bnew = fdjac(f,xnew)
        error = abs(xnew) - abs(xold)
        error = linalg.norm(error,inf)
        xold = xnew.copy()
        fold = fnew.copy()
        b = bnew.copy()
        #print xnew
        if(error < tol):
            #print 'xnew: ' , xnew 
            #print 'xold: ' , xold
            #print 'i: ' ,i
            return xnew
            break
        if math.isnan(linalg.norm(xnew,inf)) == True:
            break
        if i > lim:
            print 'i: ' , i
            print 'f: ' , fnew
            break
    return xnew

def fdjac(f,x):    # approximate jacobian matrix of partial derivatives of f at x by difference quotients
    eps = finfo( type(x[0]) ).eps    # machine epsilon from numpy
    delta = eps**(1.0/3.0)*linalg.norm(x,inf);
    xplus = x.copy()
    xminus= x.copy()
    n = x.shape[0]
    df = empty((n,n))
    for i in range(n):
        xplus[i] += delta;
        xminus[i]-= delta; 
        fplus  = f(xplus);
        fminus = f(xminus);
        df[:,i] = (fplus-fminus)/(2.*delta);
        xplus[i] = x[i]
        xminus[i]= x[i] 
    return df



