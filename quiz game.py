print ("hello welcome to quiz game")
playing=input("do u want to play?")

if playing.lower() !="yes":
    quit()

print("great lets start! ")

score = 0

answer=input("what does CPU stand for? ")
if answer.lower() == "computer processing unit" :
    print ("correct")
    score += 1
else:
    print("incorrect")   

answer=input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print ("correct")
    score += 1
else:
    print("incorrect")   


answer=input("what does RAM stand for? ")
if answer.lower() == "random acces memory" :
    print ("correct")
    score += 1
else:
    print("incorrect")   

print("you got "+str(score) +" questions correct")
print("thank u for playing with us")


