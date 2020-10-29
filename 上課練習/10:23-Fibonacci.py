def fib(n):
    a=int(input('a='))
    b=int(input('b='))
    seq=[]
    for i in range(n):
        seq.append(a)
        a,b=b,a+b
    print(seq)