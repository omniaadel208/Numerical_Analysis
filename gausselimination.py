import numpy as np
import sys
def gauss(n,a):
    solution = []
    x = np.zeros(n) 
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]
    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\t')
        solution.append(x[i])
    return solution,a
# gauss(3,[[2,1,1,8],[4,1,0,11],[-2,2,1,3]])