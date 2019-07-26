import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(func.__name__  + ' took ' + str(stop-start) + "secs")
        return res
    
    return wrapper

@timer
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
factorial(444)

@timer
def fib_lin(x):
    a, b = 0, 1
    for i in range(x+1):
        a, b = b, a + b
    return a
fib_lin(1000)
