import random
user_score=0
comp_score=0

options=["rock","paper","scissors"]

while True:   
    user_input=input("Type Rock/Paper/Scissors or Q to quit:").lower()

    if user_input=="q":
        break

    if (user_input  not in ["rock","paper","scissors"]):
        continue

    random_number=random.randint(0,3)
    #rock:1,paper:2,scissor:3
    computer_pick=options(random_number)
    print("computer picked",computer_pick +",")

    if user_input=="rock" and computer_pick=="scissors":
        print("you won")
        user_wins==1

    elif  user_input=="paper" and computer_pick=="rock":
        print("you won")
        user_wins==1

    elif user_input=="scissors" and computer_pick=="paper":
        print("you won")
        user_wins=1
        
    else:
        print("you lost")
        computer_wins+=1
    
print("you won",user_wins,"times")
print("The computer won",computer_wins,"times")
print("goodbye!")
