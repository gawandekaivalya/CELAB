# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\smdes\.spyder2\.temp.py
"""
import scipy
import win32com.client
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
'''
x1 = win32com.client.gencache.EnsureDispatch("Excel.Application")
wb= x1.Workbooks('ExamProblem.xlsx')
sheet = wb.Sheets('ExamProblem')

def getdata(sheet,Range):
    data = sheet.Range(Range).Value
    data = scipy.array(data)
    data = data.reshape((1,len(data)))[0]
    return data
'''
data=pd.read_excel("ExamProblem.xlsx","ExamProblemData")
t=scipy.array(data["Col1"])
ca=scipy.array(data["Col2"])
cb=scipy.array(data["Col3"])
'''    
t = getdata(sheet, "A2:A11")
ca = getdata(sheet, "B2:B11")
cb = getdata(sheet, "C2:C11")
'''
p = np.polyfit(t,cb,2)
print p

plt.plot(t,cb,'ro')
cbfit = np.polyval(p,t)
plt.plot(t,cbfit,'y--')
plt.xlabel('t')
plt.ylabel('cb')
plt.show()
def rate(p,t):
    rate = p[0]*2*t + p[1]*t
    return rate
n = len(t)

for i in range (0,n):
    k[i] = rate(p,t)[i]/(ca[i]*cb[i])
    
k_avg = np.average(k)
    
    

