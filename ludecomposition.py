import scipy.linalg as lg
def ludec(A,b):
    lu, piv = lg.lu_factor(A)
    p, l, u = lg.lu(A)
    x = lg.lu_solve((lu, piv), b)
    print(x)
    return x,lu,l,u
# ludec([[2,1,-1],[5,2,2],[3,1,1]],[1,-4,5])
