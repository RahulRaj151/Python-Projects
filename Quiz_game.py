print("this is quiz")
play = input("Do you want to play ")

if play.lower() != "yes":
    print("ok bye")
    quit()
print("game begins")
score = 0
answer = input("what is the full form of UFO")
if answer.lower() == "unidentified flying object":
    print("Correct")
    score += 1
else:
    print("wrong")

answer = input("what is the full form of UFO").lower()
if answer == "unidentified flying object":
    print("Correct")
    score += 1
else:
    print("wrong")

print("you got "+ str(score) + " Question correct")