import math
import matplotlib.pyplot as plt

x0 = -1
dx = 0 
v = dx
h = 0.01
t = 0

# f(t,x,v) = dv/dt
def f(F,t,x,v,g=0.25):
    return (-g*v + x*(1 - x**2)/2 + F*math.cos(t))

def rk4(T,F,h,x0,v0=1,g=0.25,t=0): #x0 = -1
    x = []
    v = []
    
    for i in range (1,int(T/h)):
        k1x = h * v0
        k1v = h * f(F, t, x0, v0)
        k2x = h * (v0 + k1v/2)
        k2v = h * f(F, t+h/2, x0 + k1x/2,v0 + k1v/2)
        k3x = h * (v0 + k2v/2)
        k3v = h * f(F, t+h/2, x0 + k2x/2,v0 + k2v/2)
        k4x = h * (v0 + k3v/2)
        k4v = h * f(F, t+h/2, x0 + k3x/2,v0 + k3v/2)
        x0 = x0 + (k1x + 2*k2x + 2*k3x + k4x)/6
        v0 = v0 + (k1v + 2*k2v + 2*k3v + k4v)/6
        t = t + h
    
    X = [x[i] for i in range (int((T/2)/h)+1,len(x))]
#    V = [v[i] for i in range (int((T/2)/h),len(v))]
    return (X)


def Bifurca():
    F = 0
    Efe = []
    
    while F <= 0.7:
        h = 0.01 * (2*math.pi)
        x = rk4(400,F,h,-1)
        h = 0.001 * (2*math.pi)
        for i in range (100):
            for j in range (1000):
                X = rk4(8,F,h,x)
        Efe.append(F) 
        F+=0.0005
        
    # plot 
    plt.scatter(F,X,s=3)
    plt.xlabel('x')
    plt.ylabel('F')
    plt.show()
        