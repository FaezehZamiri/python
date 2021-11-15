n=int(input("Enter a Number : "))
if n%2==0:
    for i in range(1,n+2,2):
        print((n+1-i)//2*' ',end='')
        print(i*'*')
    for i in range(n-1,0,-2):
        print((n+1-i)//2*' ',end='')
        print(i*'*')
else:
    for i in range(1,n,2):
        print((n-i)//2*' ',end='')
        print(i*'*')
    for i in range(n,0,-2):
        print((n-i)//2*' ',end='')
        print(i*'*')
