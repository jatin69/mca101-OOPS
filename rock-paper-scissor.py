import random

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def human_choice():
    while True:
        choice = input("Enter r for rock, p for paper, s for scissors: ")
        if choice.lower() in ['r','rock']:
            return 'rock'
        elif choice.lower() in ['p','paper']:
            return 'paper'
        elif choice.lower() in ['s','scissors']:
            return 'scissors'
        else:
            print("Please enter a valid option.")

def round_winner(computer_choice, human_choice):
    #print(computer_choice,human_choice)
    if computer_choice == 'rock':
        if human_choice == 'rock':
            return 'tie'
        elif human_choice == 'paper':
            return 'lose'
        else:
            return 'win'
    elif computer_choice == 'paper':
        if human_choice == 'rock':
            return 'win'
        elif human_choice == 'paper':
            return 'tie'
        else:
            return 'lose'
    else:
        if human_choice == 'rock':
            return 'lose'
        elif human_choice == 'paper':
            return 'win'
        else:
            return 'tie'


human_choice = human_choice()
computer_choice = computer_choice()
print("Your choice :",human_choice)
print("Computer choice :",computer_choice)
print("Result : ",round_winner(computer_choice, human_choice))
