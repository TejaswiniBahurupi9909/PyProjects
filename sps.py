import random
print("Rules")
print("stone vs paper -> paper ")
print("stone vs Scissor -> stone ")
print(" Scissor vs paper -> Scissor ")
n = "Continue"
computer = 0
user = 0
l1 = ['stone','paper','scissor']
while(n == 'Continue'):
    i = input("Please Enter your choice:")
    a = random.choice(l1)
    print("Computer's choice is ",a)
    if (a == 'stone' and i == 'paper') or (a == 'paper' and i == 'scissor') or (a=='scissor' and i == 'stone'):
        print("You won")
        user = user+1
    if (a == 'paper' and i == 'stone') or (a == 'scissor' and i == 'paper') or (a=='stone' and i == 'scissor'):
        print("Computer Won")
        computer += 1
    if (a == i):
        print("Tie")
        
    n = input("Enter Continue to Continue:")
if computer > user:
    print("Computer won by ", computer ,"-",user ,"points")
if computer < user:
    print("You won by ", user ,"-", computer,"points")
if computer == user:
    print("It's a tie ", user ,"-", computer,"points")