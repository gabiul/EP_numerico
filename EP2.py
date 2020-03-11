#                              EP2 - Calculo numerico
#
# =============================================================================
# vamos resolver o seguinte sistema linear
# |0  5 -1||I1|    |5 |
# |11 0  1||I2| =  |14|
# |1 -1 -1||I3|    |0 |
# =============================================================================

import numpy as np

# b) metodo de Eliminacao de Gauss

A = [[0, 5,-1],
     [11,0, 1],
     [1,-1,-1]]

b = [5,14,0]


# O metodo
def Gauss(A, b):
    n = len(A)
    
    # fazendo uma matriz mais facil de resolver
    for i in range (len(A)):
        A[i].append(b[i])
    #print(A)
    for i in range (n):
        
        # procurando o maior elemento da coluna
        maiEl = abs(A[i][i])
        maiLin = i
        for k in range (i+1, n):
            if abs(A[k][i]) > maiEl:
                maiEl = abs (A[k][i])
                maiLin = k

        # substituindo a atniga pela agora, maior linha
        for k in range (i, n+1):
            tmp = A[maiLin][k]
            A[maiLin][k] = A[i][k]          
            A[i][k] = tmp
        
        # zerando as demais linhas
        for k in range (i+1, n):
            c = - float(A[k][i])/float(A[i][i])
            for j in range (i, n+1):
                A[k][j] += c * float(A[i][j])    
        print('i =',i,A)
    
    # achando as solucoes
    X = []
    for i in range (n):
        X.append(0)
    for i in range(n-1, -1, -1):
        X[i] = A[i][n]/A[i][i]
        for k in range(n-1, -1, -1):
            A[k][n] -= A[k][i] * X[i]
    return (X)

#==============================================================================

# c) Resolvendo pelo metodo de Jacobi

# criterio de parada
erro = 0.001

# funcao main        
def Jacobi(A, b):
    n = len(A)
    
    # permutando as duas primeiras linhas
    A[0], A[1] = A[1], A[0]
    b[0], b[1] = b[1], b[0]

    def erro(A, B):
        C = np.absolute(np.subtract(A , B))
        return (np.amax(C))
            
        
    # criando as matrizes do metodo    
    X = np.zeros(n)
    novo_X = np.zeros(n)
    D = np.diag(A)
    J = A - np.diagflat(D)
    
    # variaveis do laco
    k = 0
    e = 10
    eps = 0.001
    while eps < e:
        X = novo_X
        novo_X = (b - np.dot(J,X))/D
        e = erro(X, novo_X)
        k += 1
        print('k= ', k , 'erro = ', e ,'\n', 'I1= ' , novo_X[0],'\n', 'I2= ' ,
              novo_X[1],'\n', 'I3= ' , novo_X[2])
    return (X)
    
#==============================================================================

# d) Metodo de Gaus-Seidel

# criterio de parada
erro = 0.001

# funcao main        
def Seidel(A, b):
    n = len(A)
    
    # permutando as duas primeiras linhas
    A[0], A[1] = A[1], A[0]
    b[0], b[1] = b[1], b[0]

    # Variaveris necessarias
    X_teste = [0 for i in range(n)]
    X = [0 for i in range(n)]
    e = 10
    erro = 0.001
    k = 0
    
    # O metodo
    while erro < e:
        for i in range (n):
            X_teste[i] = X[i]
            X[i] = b[i]/A[i][i]
            for j in range(0,i):
                if j != i:
                    X[i] -= A[i][j]*X[j]/A[i][i]
        e = abs(X_teste[i]-X[i])
        k += 1
        print('k= ', k , 'erro = ', e ,'\n', 'I1= ' , X_teste[0],'\n', 'I2= ' ,
              X_teste[1],'\n', 'I3= ' , X_teste[2])
    return (X)