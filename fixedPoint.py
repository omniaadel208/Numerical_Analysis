import math
def fixedPoint(i, x0, e):
    def g(x):
        return eval(i,{'x':x, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log, 'exp':math.exp})
    x0 = float(x0)
    e = float(e)
    # N= int(N)
    step = 1
    # flag = 1
    iterations = []
    print(f'iteration=0|xi={x0}|f(xi)={g(x0)}|error=-')
    iterations.append(f'iteration=0| xi={x0:0,.3f}| f(xi)={g(x0):0,.3f}| error=-')
    condition = True
    while condition:
        xi = x0
        x1 = g(xi)
        error = abs((x1 - xi)/x1) * 100 
        print(f'iteration={step}|xi={x1}|f(xi)={g(x1)}|error={error}')
        iterations.append(f'iteration={step}| xi={x1:0,.3f}| f(xi)={g(x1):0,.3f}| error={error:0,.3f}')
        x0 = x1
        step = step + 1
        condition = error > e
    print(f'root={x1}')
    return iterations, x1


# fixedPoint('x**2-1.8*x-2.5','sqrt(1.8*x+2.5)',5,0.2,15)
# fixedPoint('sqrt(1.8*x+2.5)',5,0.2)

def fixed_Point(i, x0, N):
    def g(x):
        return eval(i,{'x':x, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log, 'exp':math.exp})
    x0 = float(x0)
    N= int(N)
    step = 1
    iterations = []
    if N==0:
        return '',''
    else:
        print(f'iteration=0|xi={x0}|f(xi)={g(x0)}|error=-')
        iterations.append(f'iteration=0| xi={x0:0,.3f}| f(xi)={g(x0):0,.3f}| error=-')
        condition = True
        while condition:
            xi = x0
            x1 = g(xi)
            error = abs((x1 - xi)/x1) * 100 
            print(f'iteration={step}|xi={x1}|f(xi)={g(x1)}|error={error}')
            iterations.append(f'iteration={step}| xi={x1:0,.3f}| f(xi)={g(x1):0,.3f}| error={error:0,.3f}')
            x0 = x1
            step = step + 1
            condition = step < N
        print(f'root={x1}')
        return iterations, x1

fixed_Point('sqrt(1.8*x+2.5)',5,5)
