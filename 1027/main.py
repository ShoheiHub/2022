#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------------------------
# main.py
#
#   This is sample program and written by python
#   Practice python coding and 
#     differential and integration.
#
#  author:T.Shohei
#    data:2022.10.22
#---------------------------------------------------------

# <- #(of character ) defines a comment.

# python usually uses some convenience module
import numpy as np # numerical module

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  lesson.1 : differentioal
#    y = cosx -bibun-> dy/dx=-sinx
#
#  dy ~ y[i+1] - y[i-1]
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
N = 21

xmin= 0
xmax= 2*np.pi
x = np.linspace(xmin,xmax,N) # min < x < max : size is N
dx = (xmax-xmin)/(N-1)

y = np.cos(x)

# make empty array
yp = np.zeros(N)

for i in range(1,N-1):
    yp[i] = ( y[i+1]-y[i-1] )/dx*0.5
yp[0]   = (y[1]  -y[0]  )/dx
yp[N-1] = (y[N-1]-y[N-2])/dx

file1="./lesson1.dat"
with open(file1,mode="w") as f:
    f.write("%x y y_prime\n")
    for i in range(N):
        f.write(f"{x[i]:.3f} {y[i]:.3f} {yp[i]:.3f}\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  lesson.2 : integration
#    y = cosx -sekibun-> Y=sinx
#
#  Y[i] = y[i]*dx
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def integration(N2):
    x = np.linspace(xmin,xmax,N2)
    dx = (xmax-xmin)/(N2-1)

    y = np.cos(x)

    Y = np.zeros(N2)
    i=0
    for i in range(1,N2):
        Y[i] = Y[i-1]+y[i]*dx
    return x, Y, y

N2=100
x,Y,y = integration(N2)

# try to output dat file like above!!

file2="./lesson2.dat"
with open(file2,mode="w") as f:
    f.write("%x y Y\n")
    for i in range(N2):
        f.write(f"{x[i]:.3f} {y[i]:.3f} {Y[i]:.3f}\n")


