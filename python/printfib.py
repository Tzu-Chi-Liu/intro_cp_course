def fib(n):
    """ prints out the fibonacci sequence to the nth term """
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        print(a)

print('fibonacci sequence:')
fib(10)        
