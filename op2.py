# from tkinter import *
# import ttkbootstrap as tb
# import numpy as np
# import gausselimination as gs

# root = tb.Window(themename='superhero')
# root.title('Numerical Matrix')

# def process():
#     values = [e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get()]

#     a = np.zeros((3,4),dtype=np.float64)
    
#     for i in range(3):
#         for j in range(4):
#             a[i][j] = values[i*4+j]
#     print(a)
#     sol = gs.gauss(3,a)
#     print(sol)
#     sol_label = []
#     for i in range(len(sol)):
#         labeli = Label(root,text=f'x{i+1}={sol[i]}')
#         labeli.grid(row=5,column=1+i)
#         sol_label.append(labeli)
    
# def clear():
#     e1.delete(0,'end')
#     e2.delete(0,'end')
#     e3.delete(0,'end')
#     e4.delete(0,'end')
#     e5.delete(0,'end')
#     e6.delete(0,'end')
#     e7.delete(0,'end')
#     e8.delete(0,'end')
#     e9.delete(0,'end')
#     e10.delete(0,'end')
#     e11.delete(0,'end')
#     e12.delete(0,'end')

    


# e1 = Entry(root)
# e2 = Entry(root)
# e3 = Entry(root)
# e4 = Entry(root)
# e5 = Entry(root)
# e6 = Entry(root)
# e7 = Entry(root)
# e8 = Entry(root)
# e9 = Entry(root)
# e10 = Entry(root)
# e11 = Entry(root)
# e12 = Entry(root)

# e1.grid(row=1,column=1)
# e2.grid(row=1,column=2)
# e3.grid(row=1,column=3)
# e4.grid(row=1,column=4)
# e5.grid(row=2,column=1)
# e6.grid(row=2,column=2)
# e7.grid(row=2,column=3)
# e8.grid(row=2,column=4)
# e9.grid(row=3,column=1)
# e10.grid(row=3,column=2)
# e11.grid(row=3,column=3)
# e12.grid(row=3,column=4)


# b = Button(root,text='Process',command=process)
# b.grid(row=4,column=5,columnspan=4,sticky=E+W)
# b2 = Button(root,text='clear',command=clear)
# b2.grid(row=6,column=5)
# root.mainloop()
from itertools import islice
N = 3
def slice(mat):

	# list of length in which we have to split
	length_to_split = [4,4,4]
	# Using islice
	matt = iter(mat)
	Output = [list(islice(matt, elem))
           for elem in length_to_split]
	gaussianElimination(Output)
	return gaussianElimination(Output)

# function to get matrix content
def gaussianElimination(mat):
	singular_flag = forwardElim(mat)
	# if matrix is singular
	if (singular_flag != -1):

		print("Singular Matrix.")

		if (mat[singular_flag][N]):
			print("Inconsistent System.")
		else:
			print("May have infinitely many solutions.")
		return

	backSub(mat)
	return mat,backSub(mat)
# function for elementary operation of swapping two rows
def swap_row(mat, i, j):

	for k in range(N + 1):

		temp = mat[i][k]
		mat[i][k] = mat[j][k]
		mat[j][k] = temp

# function to reduce matrix to r.e.f.
def forwardElim(mat):
	for k in range(N):
	
		# Initialize maximum value and index for pivot
		i_max = k
		v_max = mat[i_max][k]

		# find greater amplitude for pivot if any
		for i in range(k + 1, N):
			if (abs(mat[i][k]) > v_max):
				v_max = mat[i][k]
				i_max = i
		#print(mat)
		# if a principal diagonal element is zero,
		# it denotes that matrix is singular, and
		# will lead to a division-by-zero later.
		if not mat[k][i_max]:
			return k # Matrix is singular

		# Swap the greatest value row with current row
		if (i_max != k):
			swap_row(mat, k, i_max)
   
		for i in range(k + 1, N):

			# factor f to set current row kth element to 0,
			# and subsequently remaining kth column to 0 */
			f = mat[i][k]/mat[k][k]

			# subtract fth multiple of corresponding kth
			# row element*/
			for j in range(k + 1, N + 1):
				mat[i][j] -= mat[k][j]*f

			# filling lower triangular matrix with zeros*/
			mat[i][k] = 0
	#print(mat)
	return -1

# function to calculate the values of the unknowns
def backSub(mat):

	x = [None for _ in range(N)] # An array to store solution

	# Start calculating from last equation up to the
	# first */
	for i in range(N-1, -1, -1):

		# start with the RHS of the equation */
		x[i] = mat[i][N]

		# Initialize j to i+1 since matrix is upper
		# triangular*/
		for j in range(i + 1, N):
		
			# subtract all the lhs values
			# except the coefficient of the variable
			# whose value is being calculated */
			x[i] -= mat[i][j]*x[j]

		# divide the RHS by the coefficient of the
		# unknown being calculated
		x[i] = (x[i]/mat[i][i])
	return x
	print("\nSolution for the system:")
	for i in range(N):
		print("{:.8f}".format(x[i]))