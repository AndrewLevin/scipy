import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import math
import time

def func(x,a,b,c,d):
#    return d*scipy.special.erf((max(c,x)-a)/(math.sqrt(2)*b))+d
    return d*scipy.special.erf((np.maximum(c,x)-a)/(math.sqrt(2)*b))+d

xdata = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99])

ydata = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.1,0.5,0.9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

plt.plot(xdata, ydata, 'b-', label='data')

t0 = time.time()

scipy.optimize.curve_fit(func, xdata, ydata)

t1 = time.time()

print t1 - t0 
