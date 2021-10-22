def counter(): 
    sentence=input("Enter your Sentence : ")
    count=0
    for i in range(len(sentence)):
        if sentence[i]== " ":
            count=count+1

    print(f"the '{sentence}' has {count+1} words")

counter()