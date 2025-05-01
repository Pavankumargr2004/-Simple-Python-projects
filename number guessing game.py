import random
top_of_range=input("type a number:")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        
        print("please type a number larger than 0next time")
        quit()
else:
    print("please try once again")
    quit()
random_number=random.randrange(0,top_of_range) #random.randint also we can use
guesses=0

while True:
    guesses+=1
    user_guess=input("make a guess")

    if user_guess.isdigit():
        user_guess=int(user_guess)

    else:
        print("please type a number next time")
        continue

    if user_guess== random_number:
        print("you got it!")
        break

    else:
        if user_guess>random_number:
            print("you were above the number!")

        else:
            print("you are below the number!")
            
print("you got it in",guesses,"guesses")