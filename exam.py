# -*- coding: utf-8 -*-
"""
Created on Sun May 01 14:30:26 2016

@author: BCS
"""
import scipy
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
import numpy as np
import scipy.optimize as optimization
t=array([0,9,18,26,35,44,53,62,71,80])
ca=array([49.44,41.17,33.54,27.54,20.96,14.93,10.02,7.71,4.8,1.88])
cb=array([0,1.14,0.88,3.44,4.13,4.48,4.75,5.57,4.75,5.8])
a=0.1
b=0.01
m1=1
m2=1
A0=[a,b]
ydat=array([ca,cb])
ydata=np.transpose(ydat)
print ydata
def error(t,A0):
    def derivate(y,t):
        dca=-a*y[0]**m1+b*y[1]**m2
        dcb=+a*y[0]**m1-b*y[1]**m2
        return array([dca,dcb])
    yinitial=([49.44,0])
    y=odeint(derivate,yinitial,t)
    yout1= array(y)
    return [yout1]
errr=error(t,A0)   
([ans,err])=scipy.optimize.curve_fit(errr,t,ydata)
print ans




