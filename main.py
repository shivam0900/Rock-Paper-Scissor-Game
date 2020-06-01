import random

game=['ROCK','PAPER','SCISSORS']

def random_generator():
    return random.choice(game)

user_choice=input('Enter your choice (Rock,Paper,Scissors): ')

answer= random_generator()

if user_choice.upper()==game[0]:
    if answer== game[2]:
        print('\n\nYour answer is correct . You WIN')
    
    elif answer==user_choice.upper():
        print('\n\nGame is DRAW')
    else:
        print(f'\n\nYOu LOSE .\nThe correct answer is {answer}')



elif user_choice.upper()==game[1]:
    if answer== game[0]:
        print('\n\nYour answer is correct . You WIN')

    elif answer==user_choice.upper():
        print('\n\nGame is DRAW')
    
    else:
        print(f'\n\nYOu LOSE .\nThe correct answer is {answer}')



elif user_choice.upper()==game[2]:
    if answer== game[1] :
        print('\n\nYour answer is correct . You WIN')

    elif answer==user_choice.upper():
        print('\n\nGame is DRAW')
    
    else:
        print(f'\n\nYOu LOSE .\nThe correct answer is {answer}')

else:
    print('\n\nWRONG CHOICE')