from numpy import *
import easybridge9 as eb
import bridge as b
import broyden2 
import newton_multid as new

def H(x):
   return (1-h)*eb.bridge(x) + h*b.bridge(x)


x = array([ 0.16380292, -1.10795695 , 0.27594471, -1.38728689,  0.69585746, -1.84479568,
  2.10960157, -1.80835945,  2.8578852,  -0.60832961,  3.4941983,   1.37167165,
  0.75575966,  0.51120531,  0.96582828,  2.13722923])

'''h =0
b0 = broyden2.fdjac(H,x)
xnew = broyden2.broyden(x,H,b0,1,100)
print xnew'''
for h in linspace(0,1,1e5):
    print h    
    b0 = broyden2.fdjac(H,x)
    xnew = new.newton(H,b0,x,1e-8)
    print xnew
    if math.isnan(linalg.norm(xnew,inf)) == True:
        print x
        print h
        print 'nan break'
        break
    x = xnew
    
print x



'''for h in linspace(0,1,10000):
    b0 = broyden2.fdjac(eb.bridge,x)
    xnew = broyden2.broyden(x,eb.bridge,b0,1,100)
'''

    
    
