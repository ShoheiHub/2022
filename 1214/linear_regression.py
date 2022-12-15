import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(1) # loc seed

class Data:
    def __init__(self):
        self.dummy=float
        return

    def make(self,func,n=100,save=False):
        x=np.linspace(0,1,n)
        y=np.zeros(n)
        for i in range(n):
            y[i]=func(x[i])

        for i in range(n):
            scale=0.5
            delta_y=random.uniform(-scale,scale)
            delta_x=random.uniform(-scale,scale)
            y[i]=y[i]+delta_y
            x[i]=x[i]+delta_x

        if save==True:
            wpath=rf"data1.txt"
            with open(wpath,mode="w") as f:
                f.write(f"y x\n")
                for i in range(n):
                    f.write(f"{y[i]:.3f} {x[i]:.3f}\n")
            print(f"save as {wpath} => {save}")
        return x,y

def linear(X,slope=1,segment=1):
    return slope*X+segment

def leastsquare(x,y):
    n = len(x)
    x_sum = 0
    y_sum = 0
    print(f"{n} datas")
    for i in range(n):
        x_sum+=x[i]
        y_sum+=y[i]
    x_mean = x_sum/n
    y_mean = y_sum/n

    sxy = 0
    sxx = 0
    for i in range(n):
        sxy+=(x[i]-x_mean)*(y[i]-y_mean)
        sxx+=(x[i]-x_mean)**2
    a=sxy/sxx
    b=y_mean-a*x_mean
    print(f"x_mean={x_mean}")
    print(f"y_mean={y_mean}")
    print(f"sxy={sxy}")
    print(f"sxx={sxx}")
    return a,b

# make data set
x_data,y_data = Data().make(linear,n=1000,save=True)

# estimate coefficient
a, b = leastsquare(x_data,y_data)

x_p = np.linspace(0,1,2)
y_p = linear(x_p,slope=a,segment=b)
y_a = linear(x_p,slope=1,segment=1)

plt.scatter(x_data,y_data,color="r",s=10,alpha=0.5)
plt.plot(x_p,y_a,color="k",ls="--",lw=2,label="answer")
plt.plot(x_p,y_p,color="b",ls="-" ,lw=2,label="least square")
plt.title(f"y={a:.2f}x+{b:.2f}")
plt.legend()
plt.show()
plt.clf()

