def gaussianElimination(n,mat):
	singular_flag = forwardElim(n,mat)
	if (singular_flag != -1):

		print("Singular Matrix.")

		if (mat[singular_flag][n]):
			print("Inconsistent System.")
		else:
			print("May have infinitely many solutions.")
		return
	backSub(n,mat)
	return mat,backSub(n,mat)
def swap_row(n,mat, i, j):
	for k in range(n + 1):
		temp = mat[i][k]
		mat[i][k] = mat[j][k]
		mat[j][k] = temp
def forwardElim(n,mat):
	for k in range(n):	
		i_max = k
		v_max = mat[i_max][k]
		for i in range(k + 1, n):
			if (abs(mat[i][k]) > v_max):
				v_max = mat[i][k]
				i_max = i
		if not mat[k][i_max]:
			return k # Matrix is singular
		if (i_max != k):
			swap_row(n,mat, k, i_max)
		for i in range(k + 1, n):
			f = mat[i][k]/mat[k][k]
			for j in range(k + 1, n + 1):
				mat[i][j] -= mat[k][j]*f
			mat[i][k] = 0
	return -1
def backSub(n,mat):

	x = [None for _ in range(n)] # An array to store solution
	for i in range(n-1, -1, -1):
		x[i] = mat[i][n]
		for j in range(i + 1, n):
			x[i] -= mat[i][j]*x[j]
		x[i] = (x[i]/mat[i][i])
	return x
	