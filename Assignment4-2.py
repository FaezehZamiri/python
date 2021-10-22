import math

def solve():
    a=float(input("a = "))
    b=float(input("b = "))
    c=float(input("c = "))
    delta=math.sqrt(b**2-4*a*c)
    x1=(-1*b+delta)//(2*a)
    x2=(-1*b-delta)//(2*a)

    print(f"Quadratic Equation is {a} X ^2 + {b} X + {c} \n X1 = {x1} \n X2 = {x2} ")

solve()