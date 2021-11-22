import random
import sys
import time
win=100
snakes={
    11:8,
    20:13,
    10:20,
    31:15,
    47:40,
    90:10,
    71:65
}
ladder={
    3:16,
    20:25,
    11:30,
    6:15,
    18:20,
    11:91,
    69:99,
    1:100
}

def dice_throw():
    print('press E to roll dice, press something else to exit')
    x=input().lower()
    if x=='e':
        dice=random.randint(1,6)
        print('you got '+str(dice))
        return dice
    else:
        sys.exit('Than you for playing')
def win_conditon(player_one,d,x):
    current=player_one
    player_one=player_one+d
    if player_one >win:
         print('you need to get '+str(win-current)+' to win')
         return current
    elif player_one==win:
        sys.exit(str(x)+' you have won the game')
    else:
        return player_one
    

def snake_ladder(player_one):
    current=player_one
    if current in snakes:
        player_one=snakes.get(current)
        print('OOPS you have been bitten by a snake and went from '+str(current)+' to '+str(player_one))
    elif current in ladder:
        player_one=ladder.get(current)
        print('YAY you climbed a ladder and went from '+str(current)+' to '+str(player_one))
    return player_one

def play():
        player_one=0
        player_two=0
        a='player one'
        b='player two'
        while True:
            time.sleep(0.5)
            d=dice_throw()
            player_one=win_conditon(player_one,d,a)
            player_one=snake_ladder(player_one)
            d2=dice_throw()
            player_two=win_conditon(player_two,d2,b)
            player_two=snake_ladder(player_two)
            print('current '+str(player_one)+' for player 1')
            print('current '+str(player_two)+' for player 2')

play()