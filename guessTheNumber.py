import random

secretNumber=random.randint(1,10)


def game(secretNumber):
    for i in range(1,5):
        left=5-i
        print('No of atempts left:'+str(left))
        print('take a guess')
        guess=int(input())
        if guess<secretNumber:
            print('Guessed number is lower than the secrect number')
        elif guess>secretNumber:
            print('guessed number is higher than the secrect number')
        else:
            break
    if guess==secretNumber:
        print('Corredct!! The number you guessed is:'+str(secretNumber))
    else:
        print('Try again')

game(secretNumber)