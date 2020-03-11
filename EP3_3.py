#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:19:42 2019

@author: gabiul
"""
import numpy as np
import pandas as pd

#def ctes
a = 16807
m = 2147483647
def Random(k):
    a = 16807
    m = 2147483647
    f = ((a*k)%m)
    return (f)

def fun(x):
    return (np.sqrt(1-x**2))

def MonteCarlo(x,y,n=100):
    dentro = 0
    total = 0 
    for i in range (n):
        x = Random(x)
        y = Random(y)
        if  y <= m*fun(x/m):
            dentro += 1
        total += 1
    I = 4*(dentro/total)
    return (I)


def Ieme(x,y,N,n=100):
    I = [0 for i in range(1,N+1)]
    Im = 0
    for i in range (len(I)):
        I[i] = MonteCarlo(x,y,n)/N
        x += 1
        y += 1  
        Im += I[i]

    return (I,Im)

def Sigma(x,y,N,n=100):
    I = Ieme(x,y,N,n)[0]*N
    Im = Ieme(x,y,N,n)[1]
    sig = 0
    sigm = 0

    for i in range (N):
        sig += ((I[i]-Im)**2)/(N-1)
    
    sig = np.sqrt(sig)
    sigm = sig/np.sqrt(N) 
    return (sig,sigm)


def Tabela(x,y,j,n=100):
    N = [2**i for i in range(1,j+1)]
    Im = [0 for i in range(1,j+1)]
    sig =  [0 for i in range(1,j+1)]
    sigm = [0 for i in range(1,j+1)]
    
    for i in range (len(N)):
        Im[i] = Ieme(x,y,N[i])[1]
        sig[i] = Sigma(x,y,N[i])[0]
        sigm[i] = Sigma(x,y,N[i])[1]

    
    data = {'N_tent': N, 
            'I_m': Im, 
            'sig': sig, 
            'sig_m': sigm}
 
    tab = pd.DataFrame(data)
    return (tab)
    
        


    
            