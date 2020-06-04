import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import math
import time
import ROOT as r
import matplotlib.pyplot as plt

def func(x,a,b,c,d):
#    return d*scipy.special.erf((max(c,x)-a)/(math.sqrt(2)*b))+d
    return d*scipy.special.erf((np.maximum(c,x)-a)/(math.sqrt(2)*b))+d

list_xdata = []
list_ydata = []
list_tf1 = []
list_th1d = []

for i in range(0,1001):
    xdata = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99])
    list_xdata.append(xdata)
    ydata = func(xdata,50.,5.,0.,1.)
    ynoise = 0.2 * np.random.normal(size=xdata.size)
#    ydata = ydata + ynoise
    list_ydata.append(ydata)

    list_tf1.append(r.TF1('scurve','[3]*TMath::Erf((TMath::Max([2],x)-[0])/(TMath::Sqrt(2)*[1]))+[3]'))
    list_th1d.append(r.TH1D('th1d','th1d',100,-0.5,99.5))
    for j in range(len(ydata)):
        list_th1d[len(list_th1d)-1].SetBinContent(j+1,ydata[j])
        list_th1d[len(list_th1d)-1].SetBinError(j+1,0.1)

#plt.plot(xdata, ydata, 'b-', label='data')

for i in range(0,1001):

    if i == 1:
        t0 = time.time()

    popt, pcov = scipy.optimize.curve_fit(func, list_xdata[i], list_ydata[i])

    print popt

#plt.plot(xdata, func(xdata, *popt), 'r-',label='scurve')
#plt.show()

t1 = time.time()

print (t1 - t0)/1000

for i in range(0,1001):
    if i == 1:
        t0 = time.time()

    list_tf1[i].SetParameter(0,50)    
    list_tf1[i].SetParameter(1,5)    
    list_tf1[i].SetParameter(2,0)    
    list_tf1[i].SetParameter(3,1)    

    list_th1d[i].Fit(list_tf1[i],'SQ')

t1 = time.time()

print (t1 - t0)/1000

raw_input()
