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
    71:65,
    99:5
}
ladder={
    3:16,
    20:25,
    11:30,
    6:15,
    18:20,
    11:91,
    69:99
}

def dice_throw():
    dice=random.randint(1,6)
    print('you got '+str(dice))
    return dice

def win_conditon(player_pos,d):
    current=player_pos
    player_pos=player_pos+d
    if player_pos >win:
         print('you need to get '+str(win-current)+' to win')
         return current
    elif player_pos==win:
        sys.exit('you have won the game')
    else:
        return player_pos
    

def snake_ladder(player_pos):
    current=player_pos
    if current in snakes:
        player_pos=snakes.get(current)
        print('OOPS you have been bitten by a snake and went from '+str(current)+' to '+str(player_pos))
    elif current in ladder:
        player_pos=ladder.get(current)
        print('YAY you climbed a ladder and went from '+str(current)+' to '+str(player_pos))
    return player_pos

def player():
        player_pos=0
        while True:
            time.sleep(0.5)
            d=dice_throw()
            player_pos=win_conditon(player_pos,d)
            player_pos=snake_ladder(player_pos)
            print('current '+str(player_pos))

player()