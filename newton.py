import sympy
import math
def newton(i, x0, e):
    def f(x):
        return eval(i,{'x':x, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log, 'exp':math.exp})
    def g(x):
        drev = sympy.diff(i)
        return eval(str(drev),{'x':x, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log, 'exp':math.exp})
    x0 = float(x0)
    e = float(e)
    iterations = []
    # n = int(n)
    print(f'iteration=0|xi={x0}|f(xi)={f(x0)}|f`(xi)={g(x0)}|error=-')
    iterations.append(f'iteration=0| xi={x0:0,.3f}| f(xi)={f(x0):0,.3f}| f`(xi)={g(x0):0,.3f}| error=-')
    step = 1
    condition = True
    while condition:
        if g(x0) == 0:
            print('can not divide by zero')
            break
        x1 = x0 - f(x0) / g(x0)
        error = abs((x1 - x0) / x1) * 100
        print(f'iteration={step}|xi={x1}|f(xi)={f(x1)}|f`(xi)={g(x1)}|error={error}')
        iterations.append(f'iteration={step}| xi={x1:0,.3f}| f(xi)={f(x1):0,.3f}| f`(xi)={g(x1):0,.3f}| error={error:0,.3f}')
        x0 = x1
        step = step + 1
        condition = error > e
    print(f'root={x1}')
    return iterations, x1
        
# newton('x+cos(x)',-0.5,0)
# newton('-0.9*x**2+1.7*x+2.5',5,0.7)
def newton1(i, x0, n):
    def f(x):
        return eval(i,{'x':x, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log, 'exp':math.exp})
    def g(x):
        drev = sympy.diff(i)
        return eval(str(drev),{'x':x, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log, 'exp':math.exp})
    x0 = float(x0)
    iterations = []
    n = int(n)
    print(f'iteration=0|xi={x0}|f(xi)={f(x0)}|f`(xi)={g(x0)}|error=-')
    iterations.append(f'iteration=0|xi={x0:0,.3f}|f(xi)={f(x0):0,.3f}|f`(xi)={g(x0):0,.3f}|error=-')
    step = 1
    condition = True
    if n==0:
        return '',''
    else:
        while condition:
            if g(x0) == 0:
                print('can not divide by zero')
                break
            x1 = x0 - f(x0) / g(x0)
            error = abs((x1 - x0) / x1) * 100
            print(f'iteration={step}|xi={x1}|f(xi)={f(x1)}|f`(xi)={g(x1)}|error={error}')
            iterations.append(f'iteration={step}|xi={x1:0,.3f}|f(xi)={f(x1):0,.3f}|f`(xi)={g(x1):0,.3f}|error={error:0,.3f}')
            x0 = x1
            step = step + 1
            condition = step < n
        print(f'root={x1}')
        return iterations, x1
