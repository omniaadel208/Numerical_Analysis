import numpy as np 
def cramer(n,a,b):
    b1 = np.reshape(b,(3,1))
    a1 = np.asmatrix(a)
    solution = []
    top_sol = []
    for i in range(n):
        top_of_x = a1.copy()
        top_of_x[:,i] = b1
        top_sol.append(top_of_x)
        det_of_top_of_x = np.linalg.det(top_of_x)
        det_of_a = np.linalg.det(a1)
        x = det_of_top_of_x / det_of_a
        solution.append(round(x))  
    return top_sol,solution

# cramer(3,[[2,1,-1],[5,2,2],[3,1,1]],[1,-4,5])