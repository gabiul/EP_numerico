#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:12:40 2019

@author: gabiul
"""
# 2) Metodo do Trapezio
import math
import pandas as pd
import matplotlib.pyplot as plt

# limite de integracao
b = math.pi/2
a = 0

# Delta de x
def h(a,b,n):
    return ((b-a)/n)

# xi
def x_i(a,d,n):
    X = [0 for i in range (n)] 
    for i in range (n):
        X[i] = a + i*d
    return (X)

# o theta_0
def Theta(m):       # m = quantidade de thetas
    return (x_i(0,h(0,math.pi,m),m))

# funcao usada
def fun(theta_0,phi):
    k2 = (1 - math.cos(theta_0))/2
    return (1/(1-k2*math.sin(phi)**2))

# O metodo do Trepezio
def Trapezio(n,m):
    
    Dx = h(a,b,n)
    O = Theta(m)
    X = x_i(a,Dx,n+1)
    S = [0 for i in range (len(O))]
    for o in range (len(O)):
        for i in range (n+1):
            if i != 0 and i!= n+1 :
                S[o] += (Dx/2)*2*fun(O[o],X[i])
            else:
                S[o] += (Dx/2)*fun(O[o],X[i])
    # admitindo raiz(l/g) = 1
    T = [4*S[i] for i in range(len(S))]
    return (T)

def Tabela(n,m):
    
    data = {'Theta_0': Theta(m),
        'T':Trapezio(n,m)}
 
    # Create DataFrame
    df = pd.DataFrame(data)
    return (df)

def Grafico(n,m):    
    Y = [Trapezio(n,m)[i]/(2*math.pi) for i in range (len(Trapezio(n,m)))]
    X = Theta(m)
    
    plt.ylim(0,100)
    plt.plot(X,Y)
    plt.xlabel('theta_0 (rad)')
    plt.ylabel('T/T_Galileu')
    