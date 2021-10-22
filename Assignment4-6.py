num1=int(input("Enter A Integer Number : "))
num2=int(input("Enter An Other Integer Number : "))

def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if ((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


print(f"The Least Common Multiple of {num1} and {num2} is is {lcm(num1,num2)}")