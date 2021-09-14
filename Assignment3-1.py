import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

word = random.choice(words) # clock
joon = 10
count=0
print('- ' * len(word)) # - - - - -
while joon > 0:

    user_character = input("Enter Character : ") # s
    user_character=user_character.lower()

    if user_character in word:
        count=count+1
        print('yes')
    else:
        joon = joon - 1
        print('no')
    if count==len(word) or user_character==word:
        print("You Win ... \U0001f600")
        break
    if joon==0:
        print("Game Over ... \U0001f620")
        break

    if count==0:
        print('- ' * len(word)) # - - - - -
    else:
        for i in range(len(word)):
            if user_character==word[i]:
                print('- '*(i)+word[i]+' '+'- '*(len(word)-i-1))
                

