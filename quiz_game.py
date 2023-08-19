print("Welcome to my computer quiz game !!")

playing = input("Do you want to play ?")

if playing.lower() == "yes":
    print("okay! let's play")
else:
    print("Too bad for you")
    quit()
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("This is correct")
    score +=1
else:
    print("This is incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("This is correct")
    score +=1
else:
    print("This is incorrect")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("This is correct")
    score +=1
else:
    print("This is incorrect")

answer = input("What does BIOS stand for? ")
if answer.lower() == "basic input output processor":
    print("This is correct")
    score +=1
else:
    print("This is incorrect")

print("You got " + str(+score) +" questions correct !!")
print("You got " + str((score/4)*100) + "%")