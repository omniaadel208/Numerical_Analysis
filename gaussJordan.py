import numpy as np
import sys
def gaussj(n,a):
    x = np.zeros(n)
    piv = []
    b = []
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
    
    for i in range(len(a)):
        if a[i][i]!=1:
            piv.append(a[i][i])
            b.append(a[i][n])
            for j in range(len(a)):
                a[i][j]=a[i][j]/a[i][i]
                if a[i][j]==(-0.0):
                    a[i][j]=abs(a[i][j])
    for i in range(n):
        a[i][n]=a[i][n]/piv[i]

    #
    for i in range(n):
        x[i] = (a[i][n]/a[i][i])
    
    #Displaying solution
    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\t')
    return x,a
    
