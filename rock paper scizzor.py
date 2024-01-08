import random
while True:
    choices=["rock","paper","scizzor"]
    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock, paper or scizzor: ").lower()
    if player==computer:
        print("computer :",computer)
        print("player :",player)
        print("Draw")
    elif player=="rock":
        if computer=="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You Lose!")
        if computer=="scizzor":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win!")
    elif player=="paper":
        if computer=="scizzor":
            print("computer: ",computer)
            print("player: ",player)
            print("You Lose!")
        if computer=="rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You win!")
    elif player=="scizzor":
        if computer=="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You win!")
        if computer=="rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You Lose!")
    playagain=input("Would you like to play again? (yes/no): ").lower()
    if playagain!= "yes":
        break
print("Bozo")