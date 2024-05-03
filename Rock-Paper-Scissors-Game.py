import random

while True:
    chos = ["rock", "paper", "scissors"]
    comp = random.choice(chos)
    player = None

    while player not in chos:
        player = input("Rock, Paper, Scissors? :").lower()

    if player == comp:
        print("Computer:", comp)
        print("Player:", player)
        print("Tie!")
    elif player == "rock":
        if comp == "paper":
            print("Computer:", comp)
            print("Player:", player)
            print("You Lose!")
        elif comp == "scissors":
            print("Computer:", comp)
            print("Player:", player)
            print("You win!")
    elif player == "scissors":
        if comp == "rock":
            print("Computer:", comp)
            print("Player:", player)
            print("You Lose!")
        elif comp == "paper":
            print("Computer:", comp)
            print("Player:", player)
            print("You win!")
    elif player == "paper":
        if comp == "scissors":
            print("Computer:", comp)
            print("Player:", player)
            print("You Lose!")
        elif comp == "rock":
            print("Computer:", comp)
            print("Player:", player)
            print("You win!")

    play_again = input("Play again? (yes/no) : ").lower()

    if play_again != "yes":
        break

print("Bye, thanks for playing the game!")
