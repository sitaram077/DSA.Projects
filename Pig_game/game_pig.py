import random
def roll():
    min_val=1
    max_val=6
    num=random.randint(min_val,max_val)
    return num

while True:
    players=input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Must be between 2-4')
    else:
        print('Invalid, Try again!')

max_score = 100
player_scores = [0 for _ in range(players)]


while max(player_scores) < max_score:
    for idx in range(players):
        print('\n Player number' ,idx+1, 'turn has just started\n')
        current_score = 0

        while True:
            should_roll = input('Hit "y" to roll: ')
            if should_roll.lower() != 'y':
                break

            value=roll()
            if value==1:
                print('You rolled 1 and, your turn is done :( ')
                current_score += 0
                break
            else:
                current_score+=value
                print('You rolled :',value)
            print('Your current score is ', current_score)
        player_scores[idx] += current_score
        print("Your score is ", player_scores[idx])
max_score=max(player_scores)
win=player_scores.index(max_score)
print('The winner is player',win+1)
