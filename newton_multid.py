from numpy import *



def newton( F, DF, x, tol):
	while True:
		Fx = F(x)
		DFx = DF
		s = linalg.solve(DFx, -Fx)
		x += s
		if linalg.norm(s) <= tol: 
			return x
			













