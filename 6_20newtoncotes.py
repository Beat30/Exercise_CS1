# Ex. 6.20
# Newton Cotes


import numpy as np
from numpy import matrix
from scipy import fft, linalg
from scipy.linalg import solve
from fractions import Fraction

    
M=matrix( ((0.5,1,1), (0,4, 16), (0,16,256) ) )
b=matrix( [[5],[25],[625]])
x=solve(M,b)

print([[Fraction(float(x[0]))],[Fraction(float(x[1]))],[Fraction(float(x[2]))]])
