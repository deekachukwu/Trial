import random

game_options = ["rock","paper","scissors"]

keep_playing = "true"
while keep_playing == "true":
    
    CPU = random.choice(game_options)
    player = input("make your move: rock, paper, scissors? ")
    print("CPU chose", CPU)
    
    if player == CPU:
        print("Tie")
        
    elif player == "rock" and CPU == "scissors": 
        print("player wins")
    elif player == "rock" and CPU == "paper":
        print("CPU wins")
    elif player == "paper" and CPU == "rock":
        print("player wins")
    elif player == "paper" and CPU == "scissors":
        print("CPU wins")
    elif player == "scissors" and CPU == "rock":
        print("CPU wins")
    elif player == "scissors" and CPU == "paper":
        print("player wins")
     
    
        