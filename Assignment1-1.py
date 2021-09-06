import math

print("PLS Enter Angle in Degree")
a=float(input("Pls Enter the First Number: "))
b=float(input("Pls Enter thr Secend Number: "))

while True:
    op=input("Pls Select Operation :\n 1. +  \n 2. -  \n 3. *  \n 4. / \n 5. Radical \n 6. Sin \n 7. Cos \n 8. Tan \n 9. Cot \n 10. Fatorial")
    op=op.lower()

    if op=="1" or op=="+" :
        result=a+b
        print(f"{a}+{b}={result}")
    elif  op=="2" or op=="-" :
        result=a-b
        print(f"{a}-{b}={result}")
    elif op=="3" or op=="*" :
        result=a*b
        print(f"{a}*{b}={result}")
    elif op=="4" or op=="/" :
        if b==0:
            print("Number can not dvide zero")
        else:
            result=a/b
            print(f"{a}/{b}={result}")
    elif op=="5" or op=="radical":
        aa=a**(0.5)
        bb=b**(0.5)
        print(f"{a}**0.5={aa}")
        print(f"{b}**0.5={bb}")
    elif op=="6" or op=="sin" :
        c=a*math.pi/180
        d=b*math.pi/180
        aa=math.sin(a)
        bb=math.sin(b)
        print(f"{a} degree equal {c} Radian & Sin({a})= {aa}")
        print(f"{b} degree equal {d} Radian & Sin({b})= {bb}")
    elif op=="7" or op=="cos" :
        c=a*math.pi/180
        d=b*math.pi/180
        aa=math.cos(a)
        bb=math.cos(b)
        print(f"{a} degree equal {c} Radian & Cos({a})={aa}")
        print(f"{b} degree equal {d} Radian & Cos({b})={bb}")
    elif op=="8" or op=="tan" :
        c=a*math.pi/180
        d=b*math.pi/180
        aa=math.tan(a)
        bb=math.tan(b)
        print(f"{a} degree equal {c} Radian & Tan({a})={aa}")
        print(f"{b} degree equal {d} Radian & Tan({b})={bb}")
    elif op=="9" or op=="cot" :
        c=a*math.pi/180
        d=b*math.pi/180
        aa=math.cos(a)/math.sin(a)
        bb=math.cos(b)/math.sin(b)
        print(f"{a} degree equal {c} Radian & Cot({a})={aa}")
        print(f"{b} degree equal {d} Radian & Cot({b})={bb}")
    elif op=="10" or op=="factorial":
        aa=math.factorial(a)
        bb=math.factorial(b)
        print(f"the factorial of {a} is {aa}")
        print(f"the factorial of {b} is {bb}")
    else:
        print("sth went wrong!pls try again!")
    
    q=input("Do u Want to Continue?Y/N")
    q=q.lower()
    if q=="y":
        continue
    elif q=="n":
        break
    else:
        print("sth went wrong!pls try again!")
        break
