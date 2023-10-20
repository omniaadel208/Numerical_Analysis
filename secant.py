import math
def secant(i, xmin1, x0, e):
    def f(x):
        return eval(i,{'x':x, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log, 'exp':math.exp})
    xmin1 = float(xmin1)
    x0 = float(x0)
    e = float(e)
    iterations = []
    step = 1
    print(f'iteration=0|xi-1={xmin1}|f(xi-1)={f(xmin1)}|xi={x0}|f(xi)={f(x0)}|error=-')
    iterations.append(f'iteration=0| xi-1={xmin1:0,.3f}| f(xi-1)={f(xmin1):0,.3f}| xi={x0}| f(xi)={f(x0):0,.3f}| error=-')
    condition  = True
    while condition:
        if f(xmin1) == f(x0):
            print('can not divide by zero')
            break
        xr = x0 - ((f(x0) * (xmin1 - x0)) / (f(xmin1) - f(x0)))
        error = abs((xr - x0) / xr) * 100
        print(f'iteration={step}|xi-1={x0}|f(xi-1)={f(x0)}|xi={xr}|f(xi)={f(xr)}|error={error}')
        iterations.append(f'iteration={step}| xi-1={x0:0,.3f}| f(xi-1)={f(x0):0,.3f}| xi={xr:0,.3f}| f(xi)={f(xr):0,.3f}| error={error:0,.3f}')
        xmin1 = x0
        x0 = xr
        step = step + 1
        condition = error > e
    print(f'root={xr}')
    return iterations, xr
# secant('0.95*x**3-5.9*x**2+10.9*x-6',2.5,3.5,0.5,15)
def secant1(i, xmin1, x0, n):
    def f(x):
        return eval(i,{'x':x, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log, 'exp':math.exp})
    xmin1 = float(xmin1)
    x0 = float(x0)
    # e = float(e)
    n = int(n)
    iterations = []
    step = 1
    if n==0:
        return '',''
    else:
        print(f'iteration=0|xi-1={xmin1}|f(xi-1)={f(xmin1)}|xi={x0}|f(xi)={f(x0)}|error=-')
        iterations.append(f'iteration=0|xi-1={xmin1:0,.3f}|f(xi-1)={f(xmin1):0,.3f}|xi={x0}|f(xi)={f(x0):0,.3f}|error=-')
        condition  = True
        while condition:
            if f(xmin1) == f(x0):
                print('can not divide by zero')
                break
            xr = x0 - ((f(x0) * (xmin1 - x0)) / (f(xmin1) - f(x0)))
            error = abs((xr - x0) / xr) * 100
            print(f'iteration={step}|xi-1={x0}|f(xi-1)={f(x0)}|xi={xr}|f(xi)={f(xr)}|error={error}')
            iterations.append(f'iteration={step}|xi-1={x0:0,.3f}|f(xi-1)={f(x0):0,.3f}|xi={xr:0,.3f}|f(xi)={f(xr):0,.3f}|error={error:0,.3f}')
            xmin1 = x0
            x0 = xr
            step = step + 1
            condition = step < n
        print(f'root={xr}')
        return iterations, xr
