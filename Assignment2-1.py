lists=[]
NewList=[]
while True:
    a=input('Enter a "Number" to continue or "EXIT" to exit : ')
    a.lower()
    lists.append(a)
    if str(a)=="exit":
        if len(lists)==1:
            break
        for i in range(len(lists)-1):
            NewList.append(float(lists[i]))
        m=sum(NewList)/len(NewList)
        print(f"Numbers are {NewList}\nThe Average of Numbers is {m} ")
        break  
    else:
        try:
            float(a)
            continue
        except ValueError:
            print("Sth Went Wrong!Try Again!!")
            break
        

