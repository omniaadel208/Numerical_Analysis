from tkinter import *
from tkinter import messagebox
import ttkbootstrap as tb
import numpy as np
import gausselimination as gee
import gaussPartial as gp
import gaussJordan as gj
import sys
import ludecomposition as ldd
import cramer as crr

root = tb.Window(themename='superhero')
root.title('Numerical Matrix')
n_label = Label(root, text='no of var:')
n_label.grid(row=0,column=1)
n_entry = tb.Entry(root,bootstyle="warning")
n_entry.grid(row=0,column=1,columnspan=4,pady=10)
labe = tb.Label(root,text='')
labe.grid(row=0,column=4)

options = ['Gauss Elimination', 'Gauss Jordan', 'GE with partial pivoting', 'LU Decomposition', 'Cramer']
clicked = StringVar()
clicked.set('')
cb2 = tb.Combobox(root,values=options,width=30)
cb2.grid(row=1,column=2,columnspan=3,padx=(0,10),pady=5)
sol_label = []

m_label = []
b_label = []
values = []
def deletemat():
    global values
    [widget.grid_forget() for widget in values if isinstance(widget, Entry)]


def clear():
    global values
    [widget.delete(0, END) for widget in values if isinstance(widget, Entry)]

def clearLabel():
    global sol_label,m_label,b_label
    [widget.destroy() for widget in sol_label if isinstance(widget, Label)]
    [widget.destroy() for widget in m_label if isinstance(widget, Label)]
    [widget.destroy() for widget in b_label if isinstance(widget, Label)]

def getmat():
    deletemat()
    clearLabel()
    global values,mat_entry,b,ar,row,col
    
    # brac = Label(root)
    row = int(n_entry.get())
    col = int(n_entry.get()) + 1
    values = []
    # [widget.grid_forget() for widget in values if isinstance(widget, Entry)]
    
    b = []
    ar = []
    for i in range(row):
        brac = Label(root,text='[')
        brac.grid(row=i+2,column=0,padx=(15,0))
        b_label.append(brac)
        for j in range(col):
            mat_entry = Entry(root,width=10)
            mat_entry.grid(row=i+2,column=j+1,padx=5,pady=5)
            values.append(mat_entry)
            if j==0 or j<row:
                ar.append(mat_entry)
            elif j==row:
                b.append(mat_entry)
        brac1 = Label(root,text=']')
        brac1.grid(row=i+2,column=j+2)
        b_label.append(brac1)

    
    
 
def solve():
    global labeli,sol_label,m_label,b_label
    clearLabel()
    val = []
    # luval = []
    blu = []
    # for l in ar:
    #     ma = float(l.get())
    #     luval.append(ma)

    for s in b:
        sa = float(s.get())
        blu.append(sa)

    # for value in values:
    #     m = float(value.get())
    #     val.append(m)

    a = np.zeros((row,col),dtype=np.float64)
    alu = np.zeros((row,row),dtype=np.float64)
    for i in range(row):
        for j in range(row):
            alu[i][j]=ar[i*row+j].get()

    print(alu)
    print(blu)
    for i in range(row):
        for j in range(col):
            a[i][j] = values[i*col+j].get()
    print(a)
    sol_label = []
    m_label = []
    b_label = []
    p = 0
    o = 0
    try:
        if cb2.get() == 'Gauss Elimination':
            sol,ag = gee.gauss(row,a)
            for r in range(len(ag)):
                labelb = Label(root,text='[     ')
                labelb.grid(row=8+r,column=0)
                b_label.append(labelb)
                for c in range(len(ag)+1):
                    agg = ag[r][c]
                    labelm = Label(root,text=agg)
                    labelm.grid(row=8+r,column=1+c)
                    m_label.append(labelm)
                    p+=1
                labelb1 = Label(root,text=']')
                labelb1.grid(row=8+o,column=p+1)
                b_label.append(labelb1)
                p = 0
                o+=1
            for i in range(len(sol)):
                labeli = Label(root,text=f'x{i+1}={sol[i]}')
                labeli.grid(row=15,column=1+i)
                sol_label.append(labeli)
        elif cb2.get() == 'Gauss Jordan':
            sol,ag = gj.gaussJordan(row,a)
            for r in range(len(ag)):
                labelb = Label(root,text='[     ')
                labelb.grid(row=8+r,column=p)
                b_label.append(labelb)
                for c in range(len(ag)+1):
                    agg = ag[r][c]
                    labelm = Label(root,text=agg)
                    labelm.grid(row=8+r,column=1+c)
                    m_label.append(labelm)
                    p+=1
                labelb1 = Label(root,text=']')
                labelb1.grid(row=8+o,column=p+1)
                b_label.append(labelb1)
                p = 0
                o+=1
            for i in range(len(sol)):
                labeli = Label(root,text=f'x{i+1}={sol[i]}')
                labeli.grid(row=15,column=1+i)
                sol_label.append(labeli)

        elif cb2.get() == 'GE with partial pivoting':
            # agp,xgp = gp.slice(row,val)
            agp,xgp = gp.gaussianElimination(row,a)
            for r in range(len(agp)):
                labelb = Label(root,text='[     ')
                labelb.grid(row=8+r,column=p)
                b_label.append(labelb)
                for c in range(len(agp)+1):
                    agn = agp[r][c]
                    labelm = Label(root,text=f'{agn:0.1f}')
                    labelm.grid(row=8+r,column=1+c)
                    m_label.append(labelm)
                    p+=1
                labelb1 = Label(root,text=']')
                labelb1.grid(row=8+o,column=p+1)
                b_label.append(labelb1)
                p = 0
                o+=1
            for i in range(len(xgp)):
                labeli = Label(root,text=f'x{i+1}={xgp[i]:0.1f}')
                labeli.grid(row=15,column=1+i)
                sol_label.append(labeli)


        elif cb2.get() == 'LU Decomposition':
            x1,lu_mat,l,u = ldd.ludec(alu,blu)
            print(x1)
            p = 0
            o = 0
            label_lu=Label(root,text='LU:')
            label_lu.grid(row=8,column=1)
            b_label.append(label_lu)
            for r in range(len(lu_mat)):
                labelb = Label(root,text='[           ')
                labelb.grid(row=8+r,column=p+2)
                b_label.append(labelb)
                for c in range(len(lu_mat)):
                    agl = lu_mat[r][c]
                    labelm = Label(root,text=f'{agl:0,.1f}')
                    labelm.grid(row=8+r,column=p+2)
                    m_label.append(labelm)
                    p+=1
                labelb1 = Label(root,text=']')
                labelb1.grid(row=8+r,column=p+2)
                b_label.append(labelb1)
                p = 0
                o+=1
            labeld=Label(root,text='--------------------------')
            labeld.grid(row=11,column=2,columnspan=5)
            b_label.append(labeld)
            labell=Label(root,text='L:')
            labell.grid(row=13,column=1)
            b_label.append(labell)
            for m in range(len(l)):
                labelbr = Label(root,text='[           ')
                labelbr.grid(row=11+o,column=p+2)
                b_label.append(labelbr)
                for n in range(len(l)):
                    al = l[m][n]
                    labela = Label(root,text=f'{al:0.1f}')
                    labela.grid(row=11+o,column=p+2)
                    b_label.append(labela)
                    p+=1
                labelbr1 = Label(root,text=']')
                labelbr1.grid(row=11+o,column=p+2)
                b_label.append(labelbr1)
                p=0
                o+=1
            for i in range(len(x1)):
                labeli = Label(root,text=f'x{i+1}={x1[i]:0,.1f}')
                labeli.grid(row=20,column=2+i)
                sol_label.append(labeli)
            o = 0
            p = 0
        elif cb2.get() =='Cramer':
            top_sol,sol1 = crr.cramer(row,alu,blu)
            for j in range(len(top_sol)):
                label_a = Label(root,text=top_sol[j],font = (12))
                label_a.grid(row=8+j,column=3)
                sol_label.append(label_a)
            for i in range(len(sol1)):
                labeli = Label(root,text=f'x{i+1}={sol1[i]:0,.1f}')
                labeli.grid(row=20,column=2+i)
                sol_label.append(labeli)
            


            
        else:
            lab1 = Label(root,text="choose the rule")
            lab1.grid(row=9,column=3)
            sol_label.append(lab1)
    except:
        messagebox.showerror("error","check entries")

    # for i in sol_label:
    #     i.destroy()
    # l = labeli.grid_info()['column']
    # widgets = labeli.master.grid_slaves(column=l)
    # for widget in widgets:
    #     if isinstance(widget,Label):
    #         widget.destroy()

    # for i in sol_label:
    #     i.destroy()
    

gbtn = Button(root,command=getmat,text='get matrix')
gbtn.grid(row=0,column=5,padx=10)
sbtn = Button(root,command=solve, text='solve')
sbtn.grid(row=30,column=3,pady=5)
cbtn = tb.Button(root,text='clear',bootstyle='primary outline',command=clear)
cbtn.grid(row=30,column=4,pady=5)


root.mainloop()
