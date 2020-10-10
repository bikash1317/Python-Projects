# FInd the n term in FIbonacci numbers using Formula
def Fibonacci(n):
    Phi = 1.618
    phi = 0.618

    Fib = int(((Phi**n)-((-phi)**n))/2.236067977)
    return (Fib+1)

number = int(input())
print(Fibonacci(number))
