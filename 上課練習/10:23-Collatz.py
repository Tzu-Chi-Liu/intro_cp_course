#Collatz
n=int(input('number='))
a=[n]
while n!=1:
    if n%2==0:
        n=n//2
        a.append(n)
    if n%2==1 and n!=1:
        n=3*n+1
        a.append(n)

print(a)

#fibonacci
def fib(n):
    a=int(input('a='))
    b=int(input('b='))
    seq=[]
    for i in range(n):
        seq.append(a)
        a,b=b,a+b
    print(seq)