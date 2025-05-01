name=input("type your name")
print("welcome",name,"to this adventure")
answer=input("you are on the dirt road, it has come to an end and you can go left or right.which way you would like to go? ").lower()

if answer=="left":
        answer=input("you come to a river,you can walk around it and swim to swim across:")

        if answer=="swim":
            print("you swim across and were eaten by an alliagator")

        elif answer=="walk":
            print("you walked for many miles,ran out of the water and lost the game")

        else:
            print("not a valid option")

elif answer=="right":
        answer=input("you come to a bridge,it looks wobbly,do you want to cross")

        if answer=="back":
            print("you can go back to the main road")

        elif answer=="cross":
            answer=input("you cross the bridge  and meet the stranger.do you talk to them(yes/no)?")

            if answer=="yes":
                print("you talk to the stranger,they gave you gold and you win")

            elif answer=="no":
                print("you ignore the stranger they offended  and you lose")
                
        else:
            print("not a valid option")

else:
    print("you took an invalid option")

print("thank you for trying",name)