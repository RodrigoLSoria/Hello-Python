import random

def play():
    user_choice = input(" 'r' for rock, 'p' for paper, and 's' for scissors")
    computer_choice = random.choice(['r', 'p', 's'] )

    if user_choice == computer_choice:
        return 'It\'s a tie'
    
    if is_win(user_choice, computer_choice):
        return  'You won!'
    

def is_win(player, opponent):
    # return true if the player wins 
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True
    
