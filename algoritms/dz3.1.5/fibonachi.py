from random import randint

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(5))


#стек: f(5) - f(4) + f(3)          5 -  3  +  2
#               |      |                |     |
#             f(3)    f(2)              2     1
#               +      +                +     +
#             f(2)    f(1)              1     1
#               |                       |
#              f(1)                     1
#               +                       +
#              f(0)                     0