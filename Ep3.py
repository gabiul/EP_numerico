#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:53:19 2019

@author: gabiul
"""

'''
EP 3

1) Sendo I = integrer from 0 to 1 of (6 - 6x^5)dx
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#a) Metodo de Simpson

# Constantes utilizadas
a = 0
b = 1

# Funcao usada
def fun(x):
    return (np.float32(6 - 6*x**5))

# Delta de x
def del_x(a,b,n):
    return (np.float32((b-a)/n))

# xi
def x_i(a,n,d):
    X = np.float32([0 for i in range (n)]) 
    for i in range (len(X)):
        X[i] = np.float32(a + i*d)
    return (X)
    
# Metodo de Simpson
def Simpson(n):
    
    Dx = del_x(a,b,n)
    X = x_i(a,n+1,Dx)
    S = 0
    
    for i in range (1,n):
        if i != 0 and i!= n :
            if i%2 == 0:
                S += np.float32((Dx/3)*2*fun(X[i]))
            else:
                S += np.float32((Dx/3)*4*fun(X[i]))
    S += np.float32((Dx/3)*(fun(X[0])+fun(X[n])))
    
    return (S)

# tabela de S
def Ese(n):
    S = [0 for i in range (n)]
    for i in range (n):
        S[i] = Simpson(2**i)
    return (S)

# erro do metodo
def Erro(n,I):
    E = [0 for i in range (n)]
    S = Ese(n)
    for i in range (len(E)):
        E[i] = abs(S[i]-I)
    return (E)


#fazendo a tabela
def Tabela(n,I):
    S = Ese(n)
    p = [i for i in range (n)]
    N = [2**i for i in range (n)]
    erro = Erro(n,I)
    
    data = {'p': p,
        'N': N,
        'I_num': S,
        'erro': erro}
 
    tab = pd.DataFrame(data)
    return (tab)

def fun2(x):
    return (np.float64(6 - 6*x**5))

# Delta de x
def del_x2(a,b,n):
    return (np.float64((b-a)/n))

# xi
def x_i2(a,n,d):
    X = np.float64([0 for i in range (n)])
    for i in range (len(X)):
        X[i] = a + i*d
    return (X)
    
# Metodo de Simpson
def Simpson2(n):
    
    Dx = del_x2(a,b,n)
    X = x_i2(a,n+1,Dx)
    S = 0
    
    for i in range (1,n):
        if i != 0 and i!= n :
            if i%2 == 0:
                S += np.float64((Dx/3)*2*fun2(X[i]))
            else:
                S += np.float64((Dx/3)*4*fun2(X[i]))
    S += np.float64((Dx/3)*(fun2(X[0])+fun2(X[n])))
    
    return (S)

# tabela de S
def Ese2(n):
    S = [0 for i in range (n)]
    for i in range (n):
        S[i] = Simpson2(2**i)
    return (S)

# erro do metodo
def Erro2(n,I):
    E = [0 for i in range (n)]
    S = Ese2(n)
    for i in range (len(E)):
        E[i] = abs(S[i]-I)
    return (E)

# tabela 2
def Tabela2(n,I):
    S = Ese2(n)
    p = [i for i in range (1,n+1)]
    N = [2**i for i in range (1,n+1)]
    erro = Erro2(n,I)
    
    data = {'p': p,
        'N': N,
        'I_num': S,
        'erro': erro}
 
    tab = pd.DataFrame(data)
    return (tab)

def Grafico(n,I):    
        
    X = [i for i in range (n)]
    Y = Erro(n,I)
    plt.yscale('log')
    plt.plot(X,Y)
    
    X2 = [i for i in range (n)]
    Y2 = Erro2(n,I)
    plt.plot(X2,Y2)
    
    plt.xlabel('p')
    plt.ylabel('log(erro)')
    plt.show()
