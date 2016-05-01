# -*- coding: utf-8 -*-
"""
Created on Sun May 01 17:24:16 2016

@author: Kaivalya
"""
import pandas as pd
import scipy

data=pd.read_excel("ExamProblem.xlsx","ExamProblemData")
t1=scipy.array(data["Col1"])
ca1=scipy.array(data["Col2"])
cb1=scipy.array(data["Col3"])

#print t1,ca1,cb1

baby=list(zip(t1,ca1,cb1))
#print (baby)

df=pd.DataFrame(data=baby, columns=['time','cA','cB'])
print df

sorted=df.sort_values(['cA'],ascending=False)
a= sorted.head(1)
print a