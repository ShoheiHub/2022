#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------------------------
# graph.py
#
#   This is sample program and written by python
#   Python can draw great picture.
#
#   graph.py <- input dat files.
#
#  author:T.Shohei
#    data:2022.10.22
#---------------------------------------------------------

# python usually uses some convenience module
import numpy as np # numerical module
import matplotlib.pyplot as plt # graph module

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  lesson.1 : differentioal
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
file1="./lesson1.dat"
with open(file1,mode='r') as f:
    header = f.readline()
    data1=f.readlines()

N,=np.shape(data1)

x=[]
y=[]
yp=[]

for i in range(N):
    x.append(float(data1[i].split()[0]))
    y.append(float(data1[i].split()[1]))
    yp.append(float(data1[i].split()[2]))

plt.plot(x,y ,color="b",marker="o",markersize=2.0,linewidth=0.8,label="$sin$")
plt.plot(x,yp,color="r",marker="v",markersize=2.0,linewidth=0.8,label="$-cosx$")
#plt.axes().set_aspect('equal')
#plt.xlim(x[0],x[N-1])
#plt.ylim(-2,2)
plt.legend()
plt.show()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  lesson.2 : integration <- try
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

