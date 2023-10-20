from tkinter import *
# from tkinter import ttk
import ttkbootstrap as tb
from tkinter import messagebox
import falsePosition as fa
import newton as ne
import bisection as b
import fixedPoint as fp
import secant as se
window = tb.Window(themename='omnia1')
iterations_lable = []
window.title('Numerical Analysis')
label_xl = Label(window, text='xl: ')
xl = tb.Entry(window, width=45,bootstyle="dark")

label_xu = Label(window, text='xu: ')
xu = tb.Entry(window, width=45,bootstyle="dark")

label_x0 = Label(window, text='x0: ')
x0 = tb.Entry(window, width=45,bootstyle="dark")

label_xminus1 = Label(window, text='xi-1: ')
x_minus1 = tb.Entry(window, width=45,bootstyle="dark")

label_e = Label(window, text='e: ')
e = tb.Entry(window, width=45,bootstyle="dark")

label_n = Label(window, text='n: ')
n = tb.Entry(window, width=45,bootstyle="dark")

labelfx = Label(window,text="F(x): ").grid(row=1,column=2,padx=5)
f = tb.Entry(window,width=45,bootstyle="dark")
f.grid(row=1,column=3,padx=(0,10),pady=10)

labelx = Label(window)
label = Label(window)
labeli = Label(window)

options = ['bisection', 'false position', 'simple fixed point', 'newton', 'secant']
clicked = StringVar()
clicked.set('')
cb1 = tb.Combobox(window,values=options,width=30)
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
                iterations, xr = b.bisection(f.get(), xl.get(), xu.get(), e.get())
                for i in range(0,len(iterations)):
                    labeli = Label(window,text=iterations[i],font= ('Helvetica bold',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            except:
                iterations, xr = b.bisection1(f.get(), xl.get(), xu.get(), n.get())
                for i in range(0,len(iterations)):
                    labeli = Label(window,text=iterations[i],font= ('Helvetica bold',12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            label = tb.Label(window,text=f"root= {xr}",bootstyle="success",font= (12))
            label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        elif cb1.get() == 'false position':
            try:
                iterations, xr = fa.falsePosition(f.get(), xl.get(), xu.get(), e.get())
                for i in range(0,len(iterations)):
                    labeli = Label(window,text=iterations[i],font= (12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            except:
                iterations, xr = fa.falsePosition1(f.get(), xl.get(), xu.get(), n.get())
                for i in range(0,len(iterations)):
                    labeli = Label(window,text=iterations[i],font= (12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)


            label = tb.Label(window,text=f"root= {xr}",bootstyle="success",font= (12))
            label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        elif cb1.get() == 'simple fixed point':
            try:
                iterations, x1 = fp.fixedPoint(f.get(), x0.get(), e.get())
                for i in range(0,len(iterations)):
                    labeli = Label(window,text=iterations[i],font= (12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            except:
                iterations, x1 = fp.fixed_Point(f.get(), x0.get(), n.get())
                for i in range(0,len(iterations)):
                    labeli = Label(window,text=iterations[i],font= (12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)


            label = tb.Label(window,text=f"root= {x1}",bootstyle="success",font= (12))
            label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        elif cb1.get() == 'newton':
            try:
                iterations , x1 = ne.newton(f.get(),x0.get(),e.get())
                for i in range(0,len(iterations)):
                    labeli = Label(window,text=iterations[i],font= (12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            except:
                iterations , x1 = ne.newton1(f.get(),x0.get(),n.get())
                for i in range(0,len(iterations)):
                    labeli = Label(window,text=iterations[i],font= (12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)


            label = tb.Label(window,text=f"root {x1}",bootstyle="success",font= (12))
            label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        elif cb1.get() == 'secant':
            try:
                iterations, x2 = se.secant(f.get(), x_minus1.get(), x0.get(), e.get())
                for i in range(0,len(iterations)):
                    labeli = Label(window,text=iterations[i],font= (12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)
            except:
                iterations, x2 = se.secant1(f.get(), x_minus1.get(), x0.get(), n.get())
                for i in range(0,len(iterations)):
                    labeli = Label(window,text=iterations[i],font= (12))
                    labeli.grid(row=(8+i),column=3,padx=(0,15),pady=2.5)
                    iterations_lable.append(labeli)


            label = tb.Label(window,text=f"root {x2}",bootstyle="success",font= (12))
            label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        else:
            lab = Label(window,text="Implement the functions",font= (12))
            lab.grid(row=9,column=3)
            iterations_lable.append(lab)
    except:
        messagebox.showerror("error","check your entries")
# clicked = StringVar()
# clicked.set('')

button = tb.Button(window,text='solve',command=root,bootstyle="primary outline").grid(row=7,column=3,padx=(0,10),pady=10)

window.mainloop()




            


            

            
            








