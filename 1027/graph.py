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

plt.plot(x,y ,color="b",marker="o",markersize=2.0,linewidth=0.8,label="$cosx$")
plt.plot(x,yp,color="r",marker="v",markersize=2.0,linewidth=0.8,label="$-sinx$")
plt.legend()
plt.savefig(f"lesson1.png")
plt.clf()

x1=x
y1=y

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  lesson.2 : integration <- try
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
file2="./lesson2.dat"
with open(file2,mode='r') as f:
    header = f.readline()
    data2=f.readlines()

N,=np.shape(data2)

x=[]
y=[]
Y=[]

for i in range(N):
    x.append(float(data2[i].split()[0]))
    y.append(float(data2[i].split()[1]))
    Y.append(float(data2[i].split()[2]))

plt.plot(x,y ,color="b",marker="o",markersize=2.0,linewidth=0.8,label="$cos$")
plt.plot(x,Y,color="g",marker="x",markersize=2.0,linewidth=0.8,label="$sinx$")
plt.legend()
plt.savefig(f"lesson2.png")
plt.clf()


plt.plot(x,y ,color="b",marker="o",markersize=2.0,linewidth=0.8,label="$cos$")
plt.plot(x1,yp,color="r",marker="v",markersize=2.0,linewidth=0.8,label="$-sinx$")
plt.plot(x,Y,color="g",marker="x",markersize=2.0,linewidth=0.8,label="$sinx$")
plt.legend()
plt.savefig(f"lesson1and2.png")
plt.clf()
