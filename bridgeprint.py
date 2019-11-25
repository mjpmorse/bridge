from numpy import *
import matplotlib.pyplot as plt
#from scipy.misc import imread

x = array([0,0.84328699, 1.14131493,1.75931642,2.01000149,2.47062908,3.053])
y = array([0,-0.73706652,-0.77926063,-0.71830849,-0.64565869,-0.38757686,.184])
#img = imread("437_537_hw07.jpg")
#plt.imshow(img,zorder=0)
plt.subplot(111,aspect='equal')
plt.plot(x,y,'w')


plt.savefig('demo3.png', transparent=True)
#plt.show()


'''
 0.84328699 -0.73706652  1.14131493 -0.77926063  1.75931642 -0.71830849
  2.01000149 -0.64565869  2.47062908 -0.38757686  3.959602    3.0110531
  2.99578741  3.1039945   3.41737701  4.17733577'''
