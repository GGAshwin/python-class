import random
player=100
opponent=100
def opp_atk():
    return random.randint(1,5)
def player():
    player =100
    opponent=100
    action=int(input("Enter the action:"))
    print('''
             1.Attack
             2.Bag
             3.Party
             4.Run''')
    if action==1:
        attack(player,opponent)
#action functions
def attack(player,opponent):
    print('''
             1.Tackle
             2.Heal
             3.Buff attack
             4.Buff defense
             5.Gun ''')
    attackCh=input()
    if attackCh==1:
        opponent=opponent-20
        return opponent

def game():
    player()
    print(opponent)

game()