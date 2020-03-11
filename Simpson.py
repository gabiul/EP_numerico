#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:11:12 2019

@author: gabiul
"""

# Constantes utilizadas
a = 0
b = 1

# Funcao usada
def fun(x):
    return (6 - 6*x**5)

# Delta de x
def h(a,b,n):
    return ((b-a)/n)

# xi
def x_i(a,d,n):
    X = [0 for i in range (n)] 
    for i in range (n):
        X[i] = a + i*d
    return (X)
    
# Metodo de Simpson
def Simpson(n):
    
    Dx = h(a,n,b)
    X = x_i(a,Dx,Dx)
    S = [0 for i in range (n+1)]
    for s in range (n+1):
        for i in range (s):
            if i != 0 and i!= n+1 :
                if i%2 == 0:
                    S[s] += (Dx/3)*4*fun(X[i])
                else:
                    S[s] += (Dx/3)*2*fun(X[i])
            else:
                S[s] += (Dx/3)*fun(X[i])
    
    return (S)
