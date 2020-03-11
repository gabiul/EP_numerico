import math
import matplotlib.pyplot as plt

x0 = -1
dx = 0 
v = dx
h = 0.01
t = 0

# f(t,x,v) = dv/dt
def f(F,t,x,v,g=0.25):
    return (-g*v + x*(1 - x**2)/2 + F*math.cos(t)) #2pi/w = t/n

def rk4(N,F,h,x0,v0,t,g=0.25): #x0 = -1, v0 = 1
    x = x0
    v = v0
    
    for i in range (N):
        
        k1x = h * v
        k1v = h * f(F, t, x, v)
        k2x = h * (v + k1v/2)
        k2v = h * f(F, t+h/2, x + k1x/2,v + k1v/2)
        k3x = h * (v + k2v/2)
        k3v = h * f(F, t+h/2, x + k2x/2,v + k2v/2)
        k4x = h * (v + k3v/2)
        k4v = h * f(F, t+h, x + k3x,v + k3v)
        x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
        v = v + (k1v + 2*k2v + 2*k3v + k4v)/6
        t = t + h
        
    return (x,v,t)

def Poin(x=-1,v=1):
    F = 0.28
    X = []
    V = []

    h = 0.01 * (2*math.pi)
    H = rk4(20000,F,h,x,v,0)
    h = 0.001 * (2*math.pi)
    for i in range (20000): # 20000
        H = rk4(1000,F,h,H[0],H[1],H[2]) #1000
        X.append(H[0])
        V.append(H[1])
    
    plt.scatter(X,V,s=3)
    plt.xlabel('x')
    plt.ylabel('v')
    plt.show()
        