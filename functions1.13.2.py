from random import randint
name = input('Hello! What is your name? ')
print('''Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.''')
x = randint(1,20)
flag = False
cnt = 0
while flag == False:
    num = int(input())
    if num< x:
        print('''Your guess is too low.
Take a guess.''')
        cnt+=1
    elif num> x:
        print('''Your guess is too high.
Take a guess.''')
        cnt+=1
    else:
        cnt+=1
        print('Good job, %s! You guessed my number in %d guesses!' %(name, cnt))
        flag = True


    

