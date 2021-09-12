n=int(input("Pls Enter Number of Students: "))
points=[]
for i in range(n):
    point=float(input(f"Enter Coding point of {i+1}th Student: "))
    points.append(point)

mean=sum(points)/len(points)
maxinum=max(points)
minimum=min(points)

print(f"the Average of points are {mean} , the Maximum point is {maxinum} and Mimimun point is {minimum}")