from tkinter import *
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
import numpy as np
import falsePosition as fa
import newton as ne
import bisection as bi
import fixedPoint as fp
import secant as se
import gausselimination as gss
import gaussPartial as gpp
import gaussJordan as gj
import ludecomposition as ld
import cramer as cr


window = tb.Window(themename='omnia1')
window.title('Numerical Analysis')

note = tb.Notebook(window)
note.grid(row=0,column=0)
tab1 = tb.Frame(note)
tab2 = tb.Frame(note)

iterations_lable = []

label_xl = Label(tab1, text='xl: ')
xl = tb.Entry(tab1, width=45,bootstyle="dark")

label_xu = Label(tab1, text='xu: ')
xu = tb.Entry(tab1, width=45,bootstyle="dark")

label_x0 = Label(tab1, text='x0: ')
x0 = tb.Entry(tab1, width=45,bootstyle="dark")

label_xminus1 = Label(tab1, text='xi-1: ')
x_minus1 = tb.Entry(tab1, width=45,bootstyle="dark")

label_e = Label(tab1, text='e: ')
e = tb.Entry(tab1, width=45,bootstyle="dark")

label_n = Label(tab1, text='n: ')
n = tb.Entry(tab1, width=45,bootstyle="dark")

labelfx = Label(tab1,text="F(x): ").grid(row=1,column=2,padx=5)
f = tb.Entry(tab1,width=45,bootstyle="dark")
f.grid(row=1,column=3,padx=(0,10),pady=10)

labelx = Label(tab1)
label = Label(tab1)
labeli = Label(tab1)

options = ['bisection', 'false position', 'simple fixed point', 'newton', 'secant']
clicked = StringVar()
clicked.set('')
cb1 = tb.Combobox(tab1,values=options,width=30)
cb1.grid(row=2,column=3,padx=(0,10))

def selected(event):
    if cb1.get() == 'bisection' or cb1.get() == 'false position':
        label_xl.grid(row=3,column=2)
        xl.grid(row=3,column=3,padx=(0,10),pady=(1.5,0))
        label_xu.grid(row=4,column=2)
        xu.grid(row=4,column=3,padx=(0,10),pady=(1.5,0))
        label_e.grid(row=5,column=2)
        e.grid(row=5,column=3,padx=(0,10),pady=(1.5,0))
        label_n.grid(row=6,column=2)
        n.grid(row=6,column=3,padx=(0,10),pady=(1.5,0))
        label_x0.grid_forget()
        x0.grid_forget()
        label_xminus1.grid_forget()
        x_minus1.grid_forget()
        # label_n.grid_forget()
        # n.grid_forget()
    elif cb1.get() == 'simple fixed point' or cb1.get() == 'newton':
        label_x0.grid(row=3,column=2)
        x0.grid(row=3,column=3,padx=(0,10),pady=(1.5,0))
        label_e.grid(row=4,column=2)
        e.grid(row=4,column=3,padx=(0,10),pady=(1.5,0))
        label_n.grid(row=5,column=2)
        n.grid(row=5,column=3,padx=(0,10),pady=(1.5,0))
        label_xl.grid_forget()
        xl.grid_forget()
        label_xu.grid_forget()
        xu.grid_forget()
        label_xminus1.grid_forget()
        x_minus1.grid_forget()
    elif cb1.get() == 'secant':
        label_xminus1.grid(row=3,column=2)
        x_minus1.grid(row=3,column=3,padx=(0,10),pady=(1.5,0))
        label_x0.grid(row=4,column=2)
        x0.grid(row=4,column=3,padx=(0,10),pady=(1.5,0))
        label_e.grid(row=5,column=2)
        e.grid(row=5,column=3,padx=(0,10),pady=(1.5,0))
        label_n.grid(row=6,column=2)
        n.grid(row=6,column=3,padx=(0,10),pady=(1.5,0))
        label_xl.grid_forget()
        xl.grid_forget()
        label_xu.grid_forget()
        xu.grid_forget()
    else:
        label_x0.grid(row=3,column=2)
        x0.grid(row=3,column=3)
        label_e.grid(row=4,column=2)
        e.grid(row=4,column=3)
        label_n.grid(row=5,column=2)
        n.grid(row=5,column=3)
        label_xl.grid_forget()
        xl.grid_forget()
        label_xu.grid_forget()
        xu.grid_forget()
        label_xminus1.grid_forget()
        x_minus1.grid_forget()
cb1.bind("<<ComboboxSelected>>", selected)
def root():
    global label, labeli,iterations_lable
    label.destroy()
    
    labeli.destroy()
    for i in iterations_lable:
        i.destroy()
    iterations_lable= []
    try:
        if cb1.get() == 'bisection':
            try:
                iterations, xr = bi.bisection(f.get(), xl.get(), xu.get(), e.get())
                for i in range(0,len(iterations)):
                    labeli = Label(tab1,text=iterations[i],font= ('Times',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            except:
                iterations, xr = bi.bisection1(f.get(), xl.get(), xu.get(), n.get())
                for i in range(0,len(iterations)):
                    labeli = Label(tab1,text=iterations[i],font= ('Times',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            label = tb.Label(tab1,text=f"root= {xr}",bootstyle="success",font= ('Times',12))
            label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        elif cb1.get() == 'false position':
            try:
                iterations, xr = fa.falsePosition(f.get(), xl.get(), xu.get(), e.get())
                for i in range(0,len(iterations)):
                    labeli = Label(tab1,text=iterations[i],font= ('Times',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            except:
                iterations, xr = fa.falsePosition1(f.get(), xl.get(), xu.get(), n.get())
                for i in range(0,len(iterations)):
                    labeli = Label(tab1,text=iterations[i],font= ('Times',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)


            label = tb.Label(tab1,text=f"root= {xr}",bootstyle="success",font= ('Times',12))
            label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        elif cb1.get() == 'simple fixed point':
            try:
                iterations, x1 = fp.fixedPoint(f.get(), x0.get(), e.get())
                for i in range(0,len(iterations)):
                    labeli = Label(tab1,text=iterations[i],font= ('Times',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            except:
                iterations, x1 = fp.fixed_Point(f.get(), x0.get(), n.get())
                for i in range(0,len(iterations)):
                    labeli = Label(tab1,text=iterations[i],font= ('Times',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)


            label = tb.Label(tab1,text=f"root= {x1}",bootstyle="success",font= ('Times',12))
            label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        elif cb1.get() == 'newton':
            try:
                iterations , x1 = ne.newton(f.get(),x0.get(),e.get())
                for i in range(0,len(iterations)):
                    labeli = Label(tab1,text=iterations[i],font= ('Times',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            except:
                iterations , x1 = ne.newton1(f.get(),x0.get(),n.get())
                for i in range(0,len(iterations)):
                    labeli = Label(tab1,text=iterations[i],font= ('Times',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)


            label = tb.Label(tab1,text=f"root {x1}",bootstyle="success",font= ('Times',12))
            label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        elif cb1.get() == 'secant':
            try:
                iterations, x2 = se.secant(f.get(), x_minus1.get(), x0.get(), e.get())
                for i in range(0,len(iterations)):
                    labeli = Label(tab1,text=iterations[i],font= ('Times',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            except:
                iterations, x2 = se.secant1(f.get(), x_minus1.get(), x0.get(), n.get())
                for i in range(0,len(iterations)):
                    labeli = Label(tab1,text=iterations[i],font= ('Times',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)


            label = tb.Label(tab1,text=f"root {x2}",bootstyle="success",font= ('Times',12))
            label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        else:
            lab = Label(tab1,text="Implement the functions",font= ('Times',12))
            lab.grid(row=9,column=3)
            iterations_lable.append(lab)
    except:
        messagebox.showerror("error","check your entries")
# clicked = StringVar()
# clicked.set('')

button = tb.Button(tab1,text='solve',command=root,bootstyle="primary outline").grid(row=7,column=3,padx=(0,10),pady=10)
note.add(tab1,text='Solving Polynomial')

#-----------------------------------------------------------------------------------------------------
n_label = Label(tab2, text='no of var:')
n_label.grid(row=0,column=1)
n_entry = tb.Entry(tab2)
n_entry.grid(row=0,column=1,columnspan=4,pady=10)
labe = tb.Label(tab2,text='')
labe.grid(row=0,column=4)

options = ['Gauss Elimination', 'Gauss Jordan', 'GE with partial pivoting', 'LU Decomposition', 'Cramer']
clicked = StringVar()
clicked.set('')
cb2 = tb.Combobox(tab2,values=options,width=30)
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
    
    # brac = Label(tab2)
    row = int(n_entry.get())
    col = int(n_entry.get()) + 1
    values = []
    
    b = []
    ar = []
    for i in range(row):
        brac = Label(tab2,text='[')
        brac.grid(row=i+2,column=0,padx=(15,0))
        b_label.append(brac)
        for j in range(col):
            mat_entry = Entry(tab2,width=10)
            mat_entry.grid(row=i+2,column=j+1,padx=5,pady=5)
            values.append(mat_entry)
            if j==0 or j<row:
                ar.append(mat_entry)
            elif j==row:
                b.append(mat_entry)
        brac1 = Label(tab2,text=']')
        brac1.grid(row=i+2,column=j+2)
        b_label.append(brac1)

    
    
 
def solve():
    global labeli,sol_label,m_label,b_label
    clearLabel()
    blu = []
    for s in b:
        sa = float(s.get())
        blu.append(sa)


    a = np.zeros((row,col),dtype=np.float64)
    alu = np.zeros((row,row),dtype=np.float64)
    for i in range(row):
        for j in range(row):
            alu[i][j]=ar[i*row+j].get()

    # print(alu)
    # print(blu)
    for i in range(row):
        for j in range(col):
            a[i][j] = values[i*col+j].get()
    # print(a)
    sol_label = []
    m_label = []
    b_label = []
    p = 0
    o = 0
    try:
        if cb2.get() == 'Gauss Elimination':
            sol,ag = gss.gauss(row,a)
            for r in range(len(ag)):
                labelb = Label(tab2,text='[     ',font= ('Times',12))
                labelb.grid(row=8+r,column=p)
                b_label.append(labelb)
                for c in range(len(ag)+1):
                    agg = ag[r][c]
                    labelm = Label(tab2,text=agg,font= ('Times',12))
                    labelm.grid(row=8+r,column=1+c)
                    m_label.append(labelm)
                    p+=1
                labelb1 = Label(tab2,text=']',font= ('Times',12))
                labelb1.grid(row=8+o,column=p+1)
                b_label.append(labelb1)
                p = 0
                o+=1
            for i in range(len(sol)):
                labeli = Label(tab2,text=f'x{i+1}={sol[i]}',font= ('Times',12))
                labeli.grid(row=15,column=1+i)
                sol_label.append(labeli)
        elif cb2.get() == 'Gauss Jordan':
            sol,ag = gj.gaussj(row,a)
            for r in range(len(ag)):
                labelb = Label(tab2,text='[     ',font= ('Times',12))
                labelb.grid(row=8+r,column=p)
                b_label.append(labelb)
                for c in range(len(ag)+1):
                    agg = ag[r][c]
                    labelm = Label(tab2,text=agg,font= ('Times',12))
                    labelm.grid(row=8+r,column=1+c)
                    m_label.append(labelm)
                    p+=1
                labelb1 = Label(tab2,text=']',font= ('Times',12))
                labelb1.grid(row=8+o,column=p+1)
                b_label.append(labelb1)
                p = 0
                o+=1
            for i in range(len(sol)):
                labeli = Label(tab2,text=f'x{i+1}={sol[i]}',font= ('Times',12))
                labeli.grid(row=15,column=1+i)
                sol_label.append(labeli)
        elif cb2.get() == 'GE with partial pivoting':
            agp,xgp = gpp.gaussianElimination(row,a)
            for r in range(len(agp)):
                labelb = Label(tab2,text='[     ',font= ('Times',12))
                labelb.grid(row=8+r,column=p)
                b_label.append(labelb)
                for c in range(len(agp)+1):
                    agn = agp[r][c]
                    labelm = Label(tab2,text=f'{agn:0,.1f}',font= ('Times',12))
                    labelm.grid(row=8+r,column=1+c)
                    m_label.append(labelm)
                    p+=1
                labelb1 = Label(tab2,text=']',font= ('Times',12))
                labelb1.grid(row=8+o,column=p+1)
                b_label.append(labelb1)
                p = 0
                o+=1
            for i in range(len(xgp)):
                labeli = Label(tab2,text=f'x{i+1}={xgp[i]:0,.1f}',font= ('Times',12))
                labeli.grid(row=15,column=1+i)
                sol_label.append(labeli)


        elif cb2.get() == 'LU Decomposition':
            x1,lu_mat,l,u = ld.ludec(alu,blu)
            # print(x1)
            p = 0
            o = 0
            label_lu=Label(tab2,text='LU:',font= ('Times',12))
            label_lu.grid(row=8,column=1)
            b_label.append(label_lu)
            for r in range(len(lu_mat)):
                labelb = Label(tab2,text='[           ',font= ('Times',12))
                labelb.grid(row=8+r,column=p+2)
                b_label.append(labelb)
                for c in range(len(lu_mat)):
                    agl = lu_mat[r][c]
                    labelm = Label(tab2,text=f'{agl:0,.1f}',font= ('Times',12))
                    labelm.grid(row=8+r,column=p+2)
                    m_label.append(labelm)
                    p+=1
                labelb1 = Label(tab2,text=']',font= ('Times',12))
                labelb1.grid(row=8+r,column=p+2)
                b_label.append(labelb1)
                p = 0
                o+=1
            labeld=Label(tab2,text='--------------------------')
            labeld.grid(row=11,column=2,columnspan=5)
            b_label.append(labeld)
            labell=Label(tab2,text='L:',font= ('Times',12))
            labell.grid(row=13,column=1)
            b_label.append(labell)
            for m in range(len(l)):
                labelbr = Label(tab2,text='[           ',font= ('Times',12))
                labelbr.grid(row=11+o,column=p+2)
                b_label.append(labelbr)
                for n in range(len(l)):
                    al = l[m][n]
                    labela = Label(tab2,text=f'{al:0.1f}',font= ('Times',12))
                    labela.grid(row=11+o,column=p+2)
                    b_label.append(labela)
                    p+=1
                labelbr1 = Label(tab2,text=']',font= ('Times',12))
                labelbr1.grid(row=11+o,column=p+2)
                b_label.append(labelbr1)
                p=0
                o+=1
            for i in range(len(x1)):
                labeli = Label(tab2,text=f'x{i+1}={x1[i]:0,.1f}',font= ('Times',12))
                labeli.grid(row=20,column=2+i)
                sol_label.append(labeli)
            o = 0
            p = 0
        elif cb2.get() =='Cramer':
            top_sol,sol1 = cr.cramer(row,alu,blu)
            for j in range(len(top_sol)):
                label_a = Label(tab2,text=top_sol[j],font= ('Times',17))
                label_a.grid(row=8+j,column=3)
                sol_label.append(label_a)
            for i in range(len(sol1)):
                labeli = Label(tab2,text=f'x{i+1}={sol1[i]:0,.1f}',font= ('Times',12))
                labeli.grid(row=20,column=2+i)
                sol_label.append(labeli)
            


            
        else:
            lab1 = Label(tab2,text="choose the rule",font= ('Times',12))
            lab1.grid(row=9,column=3)
            sol_label.append(lab1)
    except:
        messagebox.showerror("error","check entries")

    

gbtn = Button(tab2,command=getmat,text='show matrix')
gbtn.grid(row=0,column=5,padx=10)
sbtn = Button(tab2,command=solve, text='solve')
sbtn.grid(row=30,column=3,pady=5)
cbtn = tb.Button(tab2,text='clear',bootstyle='primary outline',command=clear)
cbtn.grid(row=30,column=4,pady=5)




note.add(tab2,text='solving matrix')



window.mainloop()


#-2+7*x-5*x**2+6*x**3 (0,1,10) bisection
#-26+82.3*x-88*x**2+45.4*x**3-9*x**4+0.65*x**5 (0.5,1,0.2)
#sqrt(1.9*x+2.8) (5,0.7) simple fixed point
#-0.9*x**2+1.7*x+2.5 (5,0.7) newton
#0.95*x**3-5.9*x**2+10.9*x-6 (2.5,3.5,0.5) secant
#[[2,1,-1,1],[5,2,2,-4],[3,1,1,5]] matrix






            

            
            








