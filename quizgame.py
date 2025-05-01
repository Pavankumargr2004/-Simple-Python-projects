print("welcome to my computer quiz")
playing=input("Do u want to play?")
score=0

if playing.lower() != "yes":
    quit()
print("okay let's play :)")
answer=input("what does cpu stand for?")


if answer.lower() =="central processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect ! try once again")
answer=input("what does gpu stand for?")

if answer.lower() =="graphics processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect ! try once again")
answer=input("what does ram stand for?")

if answer.lower() =="random access memory":
    print("correct!")
    score+=1
else:
    print("incorrect ! try once again")
answer=input("what does rom stand for?")

if answer.lower() ==" random other memory":
    print("correct!")
    score+=1
else:
    print("incorrect ! try once again")

print("you got" + str(score) + "questions correct!")
print("you got"+str((score/4)+100)+"%.")

