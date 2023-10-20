import math
def bisection(i, xl, xu, eps):
    def f(x):
        return eval(i,{'x':x, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log, 'exp':math.exp})
    step = 0
    xr = 0
    error = 0
    iterations = []
    xl = float(xl)
    xu = float(xu)
    eps = float(eps)
    if f(xl) * f(xu) > 0:
        print('incorrect intervals')
        iterations.append('incorrect intervals')
        xr = 'undefind'
    else:
        condintion = True
        while condintion:
            xr_old = xr
            xr = (xl + xu)/2
            error = abs((xr - xr_old)/xr)*100
            if(step==0):
                print(f'iteration={step}|xl={xl}|f(xl)={f(xl)}|xu={xu}|f(xu)={f(xu)}|xr={xr}|f(xr)={f(xr)}|error=-')
                iterations.append(f'iteration={step}| xl={xl:0,.3f}| f(xl)={f(xl):0,.3f}| xu={xu:0,.3f}| f(xu)={f(xu):0,.3f}| xr={xr:0,.3f}| f(xr)={f(xr):0,.3f}| error=-')
            else:
                print(f'iteration={step}|xl={xl}|f(xl)={f(xl)}|xu={xu}|f(xu)={f(xu)}|xr={xr}|f(xr)={f(xr)}|error={error}')
                iterations.append(f'iteration={step}| xl={xl:0,.3f}| f(xl)={f(xl):0,.3f}| xu={xu:0,.3f}| f(xu)={f(xu):0,.3f}| xr={xr:0,.3f}| f(xr)={f(xr):0,.3f}| error={error:0,.3f}')
            if f(xl) * f(xr) >0:
                xl = xr
            else:
                xu = xr
            step = step + 1
            condintion = error > eps
    print(f'root= {xr}')
    return iterations, xr

# bisection('-0.6*x**2+2.4*x+5.5',5,10,0.5)
def bisection1(i, xl, xu, n):
    def f(x):
        return eval(i,{'x':x, 'sin':math.sin, 'cos':math.cos, 'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log, 'exp':math.exp})
    step = 0
    xr = 0
    error = 0
    iterations = []
    xl = float(xl)
    xu = float(xu)
    n = int(n)
    if f(xl) * f(xu) > 0:
        print('incorrect intervals')
        iterations.append('incorrect intervals')
        xr = 'undefind'
    else:
        if n==0:
            return '',''
        else:
            condintion = True
            while condintion:
                xr_old = xr
                xr = (xl + xu)/2
                error = abs((xr - xr_old)/xr)*100
                if(step==0):
                    print(f'iteration={step}|xl={xl}|f(xl)={f(xl)}|xu={xu}|f(xu)={f(xu)}|xr={xr}|f(xr)={f(xr)}|error=-')
                    iterations.append(f'iteration={step}| xl={xl:0,.3f}| f(xl)={f(xl):0,.3f}| xu={xu:0,.3f}| f(xu)={f(xu):0,.3f}| xr={xr:0,.3f}| f(xr)={f(xr):0,.3f}| error=-')
                else:
                    print(f'iteration={step}|xl={xl}|f(xl)={f(xl)}|xu={xu}|f(xu)={f(xu)}|xr={xr}|f(xr)={f(xr)}|error={error}')
                    iterations.append(f'iteration={step}| xl={xl:0,.3f}| f(xl)={f(xl):0,.3f}| xu={xu:0,.3f}| f(xu)={f(xu):0,.3f}| xr={xr:0,.3f}| f(xr)={f(xr):0,.3f}| error={error:0,.3f}')
                if f(xl) * f(xr) >0:
                    xl = xr
                else:
                    xu = xr
                step = step + 1
                condintion = step < n
            print(f'root= {xr}')
            return iterations, xr
