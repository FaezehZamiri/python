a=float(input("Please enter the 1st side of the triangle:"))
b=float(input("Please enter the 2ed side of the triangle:"))
c=float(input("Please enter the 3th side of the triangle:"))

if a+b>c and a+c>b and b+c>a:
    print("this can be triangle")
else:
    print("this can NOT be triangle")
    