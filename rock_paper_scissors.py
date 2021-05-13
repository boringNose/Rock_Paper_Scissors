import random


def winner_user(c, u):
    print("Computer chose {} and You chose {}. You Win!".format(c, u))
    print("computer_wins:", winningDict["computer_wins"], ", player_wins:", winningDict["player_wins"])


def winner_computer(c, u):
    print("Computer chose {} and you chose {}. Computer Wins!".format(c, u))
    print("computer_wins:", winningDict["computer_wins"], ", player_wins:", winningDict["player_wins"])


def winner(comp, user):
    if comp == user:
        print("You chose: {} and computer chose: {}".format(user, comp))
        print("Match Tied.\n", "computer_wins:", winningDict["computer_wins"], ", player_wins:", winningDict["player_wins"])
    elif comp == "r":
        if user == "p":
            winningDict["player_wins"] += 1
            winner_user(comp, user)
        else:
            winningDict["computer_wins"] += 1
            winner_computer(comp, user)
    elif comp == "p":
        if user == "s":
            winningDict["player_wins"] += 1
            winner_user(comp, user)
        else:
            winningDict["computer_wins"] += 1
            winner_computer(comp, user)
    else:
        if user == "r":
            winningDict["player_wins"] += 1
            winner_user(comp, user)
        else:
            winningDict["computer_wins"] += 1
            winner_computer(comp, user)


winningDict = {
                "computer_wins": 0,
                "player_wins": 0
            }
options = ("r", "p", "s")  # tuple to store options
user_choice = ""
computer_choice = ""

while user_choice != "n":
    computer_choice = options[random.randrange(3)]  # variable to store computer's choice randomly
    user_choice = input("Choose Rock(r), Paper(p) or Scissors(s): ")     # variable to store user's choice
    winner(computer_choice, user_choice)
    user_choice = input("Do you want to play again? (y/n): ")

print("Thanks for playing: Computer won {} times and You won {} times".format(winningDict["computer_wins"], winningDict["player_wins"]))